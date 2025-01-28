# from flask import make_response, jsonify


# def sahadat(obj):
#     query = "insert into donor values('Hossain', 'A-', 'Dhaka')"
#     try:
#         obj.cur.execute(query)
#         obj.con.commit()
#         return "Insert Successful"
#     except Exception as e:
#         return f"{e}"
    

# def new_user(obj, data):
#     query = "insert into new_user ("
#     for key in data.keys() :
#         query += f"{key} ,"
#     query = query[:-1]+") values("
#     for key in data.keys() :
#         query += f"'{data[key]}' ,"
#     query = query[:-1]+")"
#     print(query)
#     try:
#         obj.cur.execute(query)
#         obj.con.commit()
#         print("done")
#         return make_response({"message":"Insertion Successul"},201)
#     except Exception as e:
#         return make_response({"message":f"{e}"},400)

# def getusers(obj):
#     query = "select * from new_user"
#     try:
#         obj.cur.execute(query)
#         getting = obj.cur.fetchall()
        
#         return f"{getting}"
#     except Exception as e:
#         return f"{e}"


# def update_user(obj, data):
#     query = "update users set " 
    
#     for key in data.keys() :
#         query+= f"{key}='{data[key]}',"
#     query=query[:-1]
#     query=query+" where name='sahadat'"
    
#     try:
#         obj.cur.execute(query)
#         obj.con.commit()
#         return "Update Successfully"
#     except Exception as e:
#         return f"{e}"

# def delete_users(obj, data):
#     query = f"delete from users where name = '{data}'" 
#     print(query)
#     try:
#         obj.cur.execute(query)
        
#         return "Update Successfully"
#     except Exception as e:
#         return f"{e}"
    
# def get_db_connection(obj, data):
#     query = '''SELECT user_name, mobile, blood_group, division, district, upazila
#                FROM donors
#                WHERE blood_group = ? AND division = ? AND district = ? AND upazila = ?'''
#     obj.cursor.execute(query, (blood_group, division, district, upazila))

#     donors = obj.cursor.fetchall()
#     get_db_connection.close()

#     return jsonify([dict(row) for row in donors])
    
# def user_upload_avatar_controller(obj, uid, filepath):
#     obj.cur.execute("Update users set avatar = '{filelpath}' where id = {uid}")

from flask import make_response
from queries import add_query,update_query,delete_query, search_query

def get_donors(cursor):
    query="select name, mobile_number, division, district, upazila from users"

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
        elif key!="name" and key!="image" and key!="password":
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
    query=f"select image, name, email, username, session, role_id from Users where id={id}"
    try:
        cursor.execute(query)
        student=cursor.fetchone()
        print(student)
        if student is not None:
            data={
                "message":"Successfull",
                "data":student
            }
            if student["role_id"]==3:
                student["role_id"]="admin"
            elif student["role_id"]==1:
                student["role_id"]="student"
            else:
                student["role_id"]="teacher"
            return make_response(data,200)
        else:
            return make_response({},204)
    except Exception as e:
        data={
            "message":f"{e}",
        }
        return data
    
def user_login(cursor, data):
    query=f'select id, name, image from users where email="{data['email']}" and password="{data['password']}"'
    print(query)
    print(data)
    try:
        print("hello")
        cursor.execute(query)
        user=cursor.fetchone()
        
        if user is not None:
            data={
                "message":"Successful",
                "data":user
            }
            return make_response(data,200)
        return make_response({"error":"invalid email or password"},200)
    except Exception as e:
        print(e)
        return make_response({"error":f'{e}'},500)
