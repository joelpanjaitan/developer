from flask import request, Flask,  jsonify

indexData = Flask(__name__)

accountUsers = {
    "john":"john1234"
}

listItems = [
    {
        "itemid":1,
        "item_name":"book",
        "category":"tools",
    },{
        "itemid":2,
        "item_name":"pencil",
        "category":"tools",
    },{
        "itemid":3,
        "item_name":"mango",
        "category":"tools",
    }
]

@indexData.route('/v1/login',methods=["POST"])
def authentication():
    username = request.form.get("username")
    password  = request.form.get("password")
    if username not in accountUsers :
        return jsonify({"status":"failed","description":"wrong username"})
    elif username in accountUsers and accountUsers[username] == password:
        return jsonify({"status":"success","description":"ok"})
    else:
        return jsonify({"status":"failed","description":"wrong password"})
    
@indexData.route("/v1/item", methods=["GET"])
def fetchItem():
    username = request.args.get("username")
    items = request.args.get("item")
    if username in accountUsers:
        return jsonify({"status":"success","item":listItems})
    else:
        return jsonify({"status":"failed","description":"wrong username"})

if __name__ == "__main__":
    indexData.run(host="localhost", port=8000, debug=True)
