from flask import Flask,json,request,jsonify,make_response,send_file
from flask_cors import CORS
from datetime import datetime
app= Flask(__name__)
app.config['DEBUG']=True
CORS(app)
from connection import DB_Connector
from user_controller import get_donors,add_user as a_user, update_user as u_user, delete_user as d_user, get_user_details as user_details, search_donor as s_donor , user_login 


connector=DB_Connector()


def upload_file(data):
    uniquefilename= str(datetime.now().timestamp()).replace(".","")
    filename=str(data.filename).split(".")
    extension=filename[len(filename)-1]
    file_location=f"uploads/{uniquefilename}.{extension}"
    return file_location

def final_dict(request):
    data=request.form
    image=request.files['image']
    dict={}
    file_location=upload_file(data=image)
    for key in data:
        dict[key]=data[key]
    if image.filename!="":
        dict['image']=f"{request.scheme}://{request.host}/{file_location}"
    return {"main":dict,"file":file_location}



@app.route("/login",methods=["POST"])
def login():
    data=request.form
    return user_login(cursor=connector.cursor,data=data)

@app.route("/user/<int:id>")
def get_user_details(id):
    return user_details(connector.cursor,id)



@app.route("/uploads/<filename>")
def get_file(filename):
    return send_file(f"../uploads/{filename}")
    

@app.route("/add-user", methods=["POST"])
def add_student():
    img=request.files['image']
    final=final_dict(request=request)
    res=a_user(connector,final["main"])
    if res.status=="201 CREATED" and img.filename!="":
        img.save(final["file"])
    return res

@app.route('/search-user',methods=["POST"])
def search_donor():
    return s_donor(connector=connector, data=request.form)


@app.route("/update-user/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.form
    image = request.files.get('image')

    
    if not data.get('password') or not data['password'].strip():
        return make_response({"error": "Old password is required to update any information."}, 400)

    try:
        query = f"SELECT * FROM users WHERE password = '{data['password']}' AND id = {id}"
        connector.cursor.execute(query)
        user = connector.cursor.fetchone()
        if not user:
            return make_response({"error": "Your old password is incorrect."}, 400)
    except Exception as e:
        return make_response({"error": f"Database error: {e}"}, 500)

    
    update_fields = {}

    
    if data.get('new_pass') and data['new_pass'].strip():
        update_fields['password'] = data['new_pass']

   
    if data.get('division') and data['division'].strip():
        if not (data.get('district') and data.get('upazila')):
            return make_response({"error": "Division, district, and upazila must all be provided if updating division."}, 400)
        update_fields.update({
            "division": data['division'],
            "district": data['district'],
            "upazila": data['upazila']
        })

  
    for key in ['name', 'mobile_number', 'last_donate']:
        if key in data and data[key].strip():
            update_fields[key] = data[key]

    
    if image and image.filename.strip():
        try:
            file_location = upload_file(data=image)
            update_fields['image'] = f"{request.scheme}://{request.host}/{file_location}"
        except Exception as e:
            return make_response({"error": f"Image upload failed: {e}"}, 500)

    
    if update_fields:
        try:
            query = "UPDATE users SET " + ", ".join(f"{key}='{value}'" for key, value in update_fields.items()) + f" WHERE id={id}"
            connector.cursor.execute(query)
            connector.connection.commit()
            if 'image' in update_fields:
                image.save(file_location)
            return make_response({"message": "Successfully updated.", "data": update_fields}, 200)
        except Exception as e:
            return make_response({"error": f"Database error: {e}"}, 500)

    return make_response({"message": "No fields to update."}, 400)




@app.route("/contact", methods=["POST"])
def save_contact():
    data = request.form
    name = data.get('name')
    email = data.get('email')
    number = data.get('number')
    message = data.get('msg')
    
    if not name or not email or not number or not message:
        return make_response({"error": "All fields are required."}, 400)
    
    try:
        query = "INSERT INTO contacts (name, email, number, message) VALUES (%s, %s, %s, %s)"
        connector.cursor.execute(query, (name, email, number, message))
        connector.connection.commit()
        return make_response({"message": "Message sent successfully."}, 200)
    except Exception as e:
        return make_response({"error": f"Database error: {e}"}, 500)



@app.route("/delete-student/<int:id>",methods=["DELETE"])
def delete_student(id):
    return (d_user(connector,id))


    

if __name__=="__main__":
    app.run()