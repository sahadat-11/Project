def add_query(data,table):
    query=f"insert into {table} ("
    for key in data.keys():
        query+=key+","
    query=query[:-1]+") values("
    for key in data.keys():
        if type(data[key])==str:
            query+=f"'{data[key]}',"
        else:
            query+=f"{data[key]},"
    query=query[:-1]+")"

    return query


def search_query(data, table):
    query = f"select name, mobile_number, blood_group, division, district, upazila, last_donate from users where "
    for key in data.keys():
        query+=f"{key}='{data[key]}' and "
    query=query[:-4]
    return query


def update_query(data,table,id):
    query=f"UPDATE {table} SET "
    for key in data.keys():
        query+=f"{key}='{data[key]}',"
    query=query[:-1]+f" WHERE id={id}"
    return query


def update_password_query(new_pass, id):
    return f"UPDATE users SET password = '{new_pass}' WHERE id = {id}"


def delete_query(table,id):
    query=f"delete from {table} where id={id}"
    return query

