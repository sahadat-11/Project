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


def add_request_blood(data, table):
    keys = ",".join(data.keys())
    placeholders = ",".join(["%s"] * len(data))
    values = tuple(data.values())

    query = f"INSERT INTO {table} ({keys}) VALUES ({placeholders})"
    return query, values




def search_request_blood(data):
    query = search_query(data, 'request_bloods')
    return query

def update_request_blood(data, id):
    query = update_query(data, 'request_bloods', id)
    return query

def delete_request_blood(id):
    query = delete_query('request_bloods', id)
    return query

