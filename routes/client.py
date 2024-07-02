from loader import *
from  sqliteMode import *



@app.route('/registrations', methods=['POST'])
def registrations():
    """route for  register users"""
    try:
        clientID = GenerateAlfNumStr(10)
        INNSI = f'"{clientID}", "{request.json["tg_id"]}", "{request.json["name"]}", "{request.json["email"]}", "{request.json["phone"]}"'

        check = InsertData('clients', INNSI)
        con.commit()
        if len(check) > 1:
            return jsonify({"action": "success", "id": clientID})
        else:
            return jsonify({"action": "errorDataASDSA"})
    except Exception as e:
        log_error(e)
        print(e)
        return jsonify({"action": "errorData"})


@app.route('/client/profile/change_info', methods=['POST'])
def profile_change_info():
    """route for change user info"""
    try:
        tg_id = request.json['tg_id']
        client_name = request.json['name']
        client_email = request.json['email']
        client_phone = request.json['phone']
        updateable_table = "('name', 'email', 'phone')"
        values = f'"{client_name}", "{client_email}", "{client_phone}"'
        check = UpdateData("clients", updateable_table, values, "tg_id", tg_id)
        if len(check) > 1:
            return jsonify({"action": "success"})
        return jsonify({"action": "errorData"})
    except Exception as e:
        log_error(e)
        return jsonify({"action": "errorData"})

        
@app.route('/admin/get_all', methods=['POST'])
def AdminGetAll():
    """
        Admin route for retrieving all users.
        """
    try:
        # Example of retrieving data from your database (modify as per your database structure):
        user_data = SelectAllData("users", "*")
        if user_data:
            return jsonify({"action": "success", "data": user_data})
        else:
            return jsonify({"action": "errorData", "data": "error"})
    except Exception as e:
        log_error(e)
        return jsonify({"action": "errorData"})


@app.route('/client/profile', methods=['POST'])
def ProfileCommand():
    """
        Admin route for retrieving all users.
    """
    request_id = request.json["tg_id"]
    try:
        # Example of retrieving data from your database (modify as per your database structure):
        user_data = SelectData("clients", "tg_id", request_id)
        if user_data:
            return jsonify({"action": "success", "data": user_data})
        return jsonify({"action": "errorData", "data": f"error"})
    except Exception as e:
        log_error(e)
        return jsonify({"action": "errorData"})



@app.route('/client/get_orders', methods=['POST'])
def get_orders():
    """route for get all orders of client"""
    request_id = request.json["client_id"]
    try:
        orders_data = SelectData("orders", "client_id", request_id)
        if orders_data:
            return jsonify({"action": "success", "data": orders_data})
        return jsonify({"action": "errorData", "data": f"error"})
    except Exception as e:
        log_error(e)
    request_id = request.json["id_tg"]
    try:
        # Example of retrieving data from your database (modify as per your database structure):
        user_data = SelectData("users", "id_tg", request_id)
        if user_data:
            return jsonify({"action": "success", "data": user_data})
        else:
            return jsonify({"action": "errorData", "data": "error"})
    except Exception as e:
        log_error(e)
        return jsonify({"action": "errorData"})

