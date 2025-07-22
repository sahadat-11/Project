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
        if data.get('con_pass') != data['new_pass']:
            return make_response({"error": "New password and confirm password do not match."}, 400)
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



@app.route("/delete-student/<int:id>",methods=["DELETE"])
def delete_student(id):
    return (d_user(connector,id))



@app.route("/change-password/<int:id>", methods=["POST"])
def change_password(id):
    data = request.form

    # Validate required fields
    if not data.get("password") or not data.get("new_pass"):
        return make_response({"error": "Current password and new password are required."}, 400)

    try:
        # Check if the current password matches the user's password in the database
        query = f"SELECT * FROM users WHERE id = {id} AND password = '{data['password']}'"
        connector.cursor.execute(query)
        user = connector.cursor.fetchone()

        if not user:
            return make_response({"error": "Current password is incorrect."}, 400)

        # Update password
        query = f"UPDATE users SET password = '{data['new_pass']}' WHERE id = {id}"
        connector.cursor.execute(query)
        connector.connection.commit()

        return make_response({"message": "Password changed successfully."}, 200)

    except Exception as e:
        return make_response({"error": f"Database error: {e}"}, 500)
    


import re

@app.route("/submit-contact", methods=["POST"])
def submit_contact():
    data = request.form

    if not all(key in data and data[key].strip() for key in ["name", "email", "mobile_number", "message"]):
        return make_response({"error": "All fields are required."}, 400)

    mobile_number = data["mobile_number"]

    # Check if the number starts with "01"
    if not mobile_number.startswith("01"):
        return make_response({"error": "Mobile number must start with '01'."}, 400)

    # Check if the number has exactly 11 digits
    if not re.fullmatch(r"01\d{9}", mobile_number):
        return make_response({"error": "Mobile number must be exactly 11 digits."}, 400)

    try:
        query = """
        INSERT INTO contact_messages (name, email, mobile_number, message)
        VALUES (%s, %s, %s, %s)
        """
        values = (data["name"], data["email"], mobile_number, data["message"])

        cursor = connector.cursor
        cursor.execute(query, values)
        connector.connection.commit()

        return make_response({"message": "Message sent successfully!"}, 201)
    except Exception as e:
        return make_response({"error": f"Database error: {e}"}, 500)


from datetime import timedelta
app.secret_key = "your_super_secret_key"  # Ensure this key is properly set
app.config["SESSION_COOKIE_HTTPONLY"] = True  # Optional: restricts access to session cookie from JavaScript
app.config["SESSION_COOKIE_SECURE"] = False  # Make sure it's False if you’re using HTTP (non-HTTPS) for local dev
app.config["SESSION_PERMANENT"] = True
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=2)  # Extend session time


from flask import request
from request_blood_controller import add_request_blood_controller,search_request_blood_controller,update_request_blood_controller,delete_request_blood_controller

from flask import request, session, make_response


# @app.route("/login", methods=["POST"])
# def login():
#     data = request.form
#     return user_login(cursor=connector.cursor, data=data)

@app.route("/login", methods=["POST"])  
def login():
    print("Login route hit!")  # Debugging
    data = request.form
    print("Received data:", data)  # Debugging
    return user_login(connector.cursor, data)


from flask import request, make_response
from request_blood_controller import add_request_blood_controller,get_request_blood_controller

@app.route("/add-request-blood", methods=["POST"])
def add_request_blood():
    user_id = request.form['user_id']
    print(request.form)
    if not user_id:
        return make_response({"error": "User ID is required"}, 400)

    return add_request_blood_controller(connector, request.form)


@app.route("/get-request-blood", methods=["GET"])
def get_request_blood():
    cursor = connector.cursor
    return get_request_blood_controller(cursor)


@app.route("/search-request-blood", methods=["POST"])
def search_request_blood():
    data = request.form
    return search_request_blood_controller(connector, data)

@app.route("/update-request-blood/<int:id>", methods=["PUT"])
def update_request_blood(id):
    data = request.form
    return update_request_blood_controller(connector, data, id)

@app.route("/delete-request-blood/<int:id>", methods=["DELETE"])
def delete_request_blood(id):
    return delete_request_blood_controller(connector, id)



import random
import smtplib


# Email Configuration (Use App Password)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "sahadatfahim999@gmail.com"  # Replace with your Gmail
EMAIL_PASSWORD = "hgtj jrmb bmuj dkyc"  # Use the generated App Password

otp_storage = {}  # Temporary storage for OTPs

@app.route('/send-otp', methods=['POST'])
def send_otp():
    data = request.json
    # print(data)
    email = data['email']
    print(email)
    if not email:
        return jsonify({"error": "Email is required"}), 400
    query=f"select * from users where email='{email}'"
    print(query)
    try:
        connector.cursor.execute(query)
        data=connector.cursor.fetchone()
        if data is not None:
            otp = str(random.randint(100000, 999999))  # Generate OTP
            otp_storage[email] = otp  # Store OTP temporarily

            subject = "Your OTP Code"
            body = f"Your OTP code is {otp}. Use this to reset your password."
            message = f"Subject: {subject}\n\n{body}"

            try:
                server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.sendmail(EMAIL_ADDRESS, email, message)
                server.quit()

                return jsonify({"message": "OTP sent successfully"}), 200
            except Exception as e:
                return jsonify({"error": f"Failed to send email: {str(e)}"}), 500
        else:
            return jsonify({"error":"No user found corresponding to this email"}),400
    except Exception as e:
        print(e)
        return jsonify({"error":e}),500    


@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.json
    email = data.get('email')
    user_otp = data.get('otp')

    if email in otp_storage and otp_storage[email] == user_otp:
        del otp_storage[email]  # OTP is used, delete it
        return jsonify({"message": "OTP verified successfully"}), 200
    else:
        return jsonify({"error": "Invalid OTP"}), 400
    




@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.form
    print(data)
    new_pass = data.get('new_pass')
    con_pass = data.get('con_pass')

    if not new_pass or not con_pass:
        return jsonify({"error": "New password and confirm password are required"}), 400

    if new_pass != con_pass:
        return jsonify({"error": "Passwords do not match"}), 400

    update_query = f"UPDATE users SET password = '{new_pass}' where email='{data['email']}'"
    try:
        # Update password for ALL users (Modify as needed)
        connector.cursor.execute(update_query)
        connector.connection.commit()

        return jsonify({"message": "Password reset successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500

    

if __name__ == '__main__':
    app.run(debug=True)
