from flask import Flask,json,request,jsonify,make_response,send_file
from flask_cors import CORS
from datetime import datetime
app= Flask(__name__)
app.config['DEBUG']=True
CORS(app)
from connection import DB_Connector
from user_controller import get_donors,add_user as a_user, update_user as u_user, delete_user as d_user, get_user_details as user_details, search_donor as s_donor , user_login 
from course_controller import add_course as a_course , update_course as u_course, get_courses as g_courses, get_course_details as course_details,delete_course as d_course

connector=DB_Connector()

# Convention Starts

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

# Convention Ends



@app.route("/login",methods=["POST"])
def login():
    data=request.form
    return user_login(cursor=connector.cursor,data=data)

def get_user_details(id):
    return user_details(connector.cursor,id)

@app.route("/uploads/<filename>")
def get_file(filename):
    return send_file(f"uploads/{filename}")
    

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
    data=request.form
    image=request.files['image']
    if data['new_pass']!="":
        query=f"select * from users where password = '{data["password"]}' and id = {id}"
        try:
            connector.cursor.execute(query)
            result=connector.cursor.fetchone()
            if result is not None:
                new_dict={}
                for key in data:
                    if key=='password' :
                        continue
                    elif key == 'new_pass':
                        new_dict['password']=data[key]
                    else:
                        new_dict[key]=data[key]
                if image.filename!="":
                    file_location=upload_file(data=image)
                    new_dict['image']=f"{request.scheme}://{request.host}/{file_location}"
                res=u_user(connector=connector,data=new_dict,id=id)
                if res.status=="200 OK" and image.filename!="":
                    image.save(file_location)
                return res
            else:
                return make_response({"error":"your old password is incorrect"},400)
        except Exception as e:
            return make_response({"error":f"{e}"},500)
    else:
        final=final_dict(request=request)
        image=request.files['image']
        res=u_user(connector,final['main'],id)
        if res.status=="200 OK" and image.filename!="":
            image.save(final['file'])
        return res

@app.route("/delete-student/<int:id>",methods=["DELETE"])
def delete_student(id):
    return (d_user(connector,id))

if __name__=="__main__":
    app.run()