from datetime import datetime
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)


from app.database import User


@app.route("/")
def home():
    out = {
        "status": "ok",
        "message": "Success",
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return render_template("home.html", data=out)


@app.route("/users")
def get_all_users():
    out = {
        "status": "ok",
        "message": "Success",
    }
    # out ["body"] = scan()
    users = User.query.all()                        #returns all users in user table
    out["body"] = []                                #create an empty list
    for user in users:                              #loop: for each user in users
        user_dict = {}                              #create a new temp dictionary
        user_dict["id"] = user.id                   #map each user attribute to its corresponding key in the user_dict.
        user_dict["first_name"] = user.first_name
        user_dict["hobbies"] = user.hobbies
        user_dict["active"] = user.active
        out["body"].append(user.dict)               #append temporary dictionary empty list

    return render_template("user_list.html", data=out)              
    
                      


@app.route("/users/<int:pk>")
def get_single_user(pk):  
    user = User.query.filter_by(id=pk).first()
    if user:  
        return render_template("user_detail.html", user=user)
    return render_template("404.html"), 404


   
@app.route("/users", methods=["POST"])
def create_user():
    out = {
        "status": "Good",
        "message": "Success"
    }
    user.data = request.json

    return out, 201





@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404