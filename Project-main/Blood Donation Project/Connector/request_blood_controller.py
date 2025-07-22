from flask import make_response
from queries import add_request_blood, update_request_blood, delete_request_blood, search_request_blood,add_query


def add_request_blood_controller(connector, data):
    print(data)
    cursor = connector.cursor

    # Check if the user_id exists in the users table
    cursor.execute(f"SELECT id FROM users WHERE id ={data['user_id']}")
    user = cursor.fetchone()
    if not user:
        return make_response({'error': "User ID does not exist"}, 400)

    query = add_query(data=data, table="request_blood")
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({'message': "Blood request submitted successfully"}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)


import datetime
def get_request_blood_controller(cursor):
    today = datetime.date.today()
    query = """
        SELECT name, blood_group, no_of_bags, mobile_number, donation_date, cause, hospital, upazila, district, division
        FROM request_blood
        WHERE donation_date >= CURDATE()  -- Only fetch upcoming requests
        ORDER BY blood_group ASC, donation_date ASC   -- Show the soonest requests first
    """
    try:
        cursor.execute(query)
        reqs = cursor.fetchall()
        
        # Debugging: Log the result to confirm it's returning the correct data
        print("Fetched Data: ", reqs)

        if reqs:
            data = {
                "data": reqs,
                "message": "successful"
            }
            return make_response(data, 200)
        else:
            return make_response({"error": "No requests"}, 200)
    except Exception as e:
        return make_response({"error": str(e)}, 500)



def update_request_blood_controller(connector, data, id):
    cursor = connector.cursor
    query = update_request_blood(data, id)
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message": "Successfully updated."}, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

def delete_request_blood_controller(connector, id):
    cursor = connector.cursor
    query = delete_request_blood(id)
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message": "Successfully deleted."}, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    





def search_request_blood_controller(connector, data):
    cursor = connector.cursor
    query = search_request_blood(data=data, table="request_bloods")
    try:
        cursor.execute(query)
        donors = cursor.fetchall()
        if donors:
            return make_response({"message": "Successful", "data": donors}, 200)
        else:
            return make_response({"message": "No data found"}, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)


    
