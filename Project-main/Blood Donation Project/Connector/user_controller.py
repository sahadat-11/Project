from flask import make_response
from queries import add_query,update_query,delete_query, search_query

def get_donors(cursor):
    query="select name, mobile_number, division, district, upazila, last_donate from users"

    try:
        cursor.execute(query)
        donors=cursor.fetchall()
        if len(donors)>0:
            data={
                "message":"Successfull",
                "data":donors
            }
            return make_response(data,200)
        else:
            return make_response({},204)
    except Exception as e:
        data={
            "message":f"{e}",
            "data":""
        }
        return data

def add_user(connector,data):
    print(data)
    curso=connector.cursor
    query=add_query(data=data,table="users")
    print(query)
    try:
        curso.execute(query)
        connector.connection.commit()
        return make_response({'message':"Successfull"},201)
    except Exception as e:
        print(e)
        return make_response({'message':f'{e}'},400)

def search_donor(connector, data):
    print(data)
    curso=connector.cursor
    query=search_query(data=data,table="users")
    print(query)
    try:
        curso.execute(query)
        donors=curso.fetchall()
        print(donors)
        if len(donors)>0:
            data={
                "message":"Successfull",
                "data":donors
            }
            return make_response(data,200)
        else:
            return make_response({
                "message":"no data",
            },200)
    except Exception as e:
        data={
            "message":f"{e}",
            "data":""
        }
        return data

def update_user(connector,data,id):
    print(data)
    cursor=connector.cursor
    for key in data.keys():
        if  key=="email" or key=="id":
            message={"message":f"you can't update your {key}"}
            return make_response(message,400)
        elif key!="name" and key!="image" and key!="password" and key!="division" and key!="district" and key!="upazila" and key!="last_donate" and key!="mobile_number":
            message={"message":f"unknown field name {key}"}
            return make_response(message,400)
    query=update_query(data=data,table="users",id=id)
    try:
        cursor.execute("SET SQL_SAFE_UPDATES=0;")
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"Successfully updated."},200)
    except Exception as e:
        print(e)
        return make_response({'message':f'{e}'},400)
    
def delete_user(connector,id):
    cursor=connector.cursor
    query=delete_query(table="users", id=id)
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"Successfully Deleted!"},200)
    except Exception as e:
        print(e)
        return {'message':f'{e}'}


def get_user_details(cursor,id):
    query=f"select image, name, email, last_donate, division, district, upazila, registration_date, mobile_number from users where id={id}"
    try:
        cursor.execute(query)
        student=cursor.fetchone()
        print(student)
        if student is not None:
            data={
                "message":"Successfull",
                "data":student
            }
            return make_response(data,200)
        else:
            return make_response({},204)
    except Exception as e:
        data={
            "message":f"{e}",
        }
        return data
    

    
def user_login(cursor, data):
    try:
        # Check if the email exists
        email_query = f'SELECT id, name, image, password FROM users WHERE email="{data["email"]}"'
        cursor.execute(email_query)
        user = cursor.fetchone()

        if user is None:
            # Email does not exist
            return make_response({"error": "Email not found"}, 404)

        # Check if the password matches
        if user["password"] != data["password"]:
            return make_response({"error": "Incorrect password"}, 401)

        # Successful login
        response_data = {
            "id": user["id"],
            "name": user["name"],
            "image": user["image"],
        }
        return make_response({"message": "Login successful", "data": response_data}, 200)

    except Exception as e:
        print(e)
        return make_response({"error": f"Server error: {e}"}, 500)
