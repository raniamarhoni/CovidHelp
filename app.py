import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
import datetime
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route('/home')
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # check if email already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        if existing_email:
            flash("Email already exists")
            return redirect(url_for("register"))

        # check if the passwords match
        if request.form.get(
          "password") != request.form.get("confirm_password"):
            flash("Passwords don't match")
            return redirect(url_for("register"))

        register = {
            "type-of-help": request.form.get("type_of_help"),
            "email": request.form.get("email"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))
        else:
            # invalid password match
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    return render_template("log_in.html")


@app.route("/log_out")
def log_out():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("log_in"))


@app.route("/manage_posts/<username>", methods=["GET", "POST"])
def manage_posts(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        posts = mongo.db.posts.find({"user": username})
        return render_template(
            "manage_posts.html", username=username, posts=posts)

    return redirect(url_for("log_in"))


@app.route("/add_a_post/<username>", methods=["GET", "POST"])
def add_a_post(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        if request.method == "POST":
            post = {
                "type_of_help": request.form.get("type_of_help"),
                "user": session["user"],
                "title": request.form.get("title"),
                "description": request.form.get("description"),
                "date_posted":  datetime.datetime.now(),
                "email": mongo.db.users.find_one(
                    {"username": session["user"]})["email"]
            }
            mongo.db.posts.insert_one(post)
            flash("Post Successfully Added")
            return redirect(url_for(
                'manage_posts', username=session['user']))
        return render_template("add_a_post.html", username=username)

    return redirect(url_for("log_in"))


@app.route("/edit_post/<username>/<post_id>", methods=["GET", "POST"])
def edit_post(username, post_id):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    if session["user"]:
        if request.method == "POST":
            submit = {
                "type_of_help": request.form.get("type_of_help"),
                "user": session["user"],
                "title": request.form.get("title"),
                "description": request.form.get("description"),
                "date_posted": mongo.db.posts.find_one(
                    {"_id": ObjectId(post_id)})["date_posted"],
                "email": mongo.db.users.find_one(
                    {"username": session["user"]})["email"]
            }
            mongo.db.posts.update({"_id": ObjectId(post_id)}, submit)
            flash("Post Successfully Updated")
            return redirect(url_for('manage_posts', username=session['user']))

        return render_template("edit_post.html", username=username, post=post)
    return redirect(url_for("log_in"))


@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    if session["user"]:
        mongo.db.posts.remove({"_id": ObjectId(post_id)})
        flash("Post Successfully Deleted")
        return redirect(url_for('manage_posts', username=session['user']))
    return redirect(url_for("log_in"))


@app.route('/posts')
def posts():
    posts = mongo.db.posts.find()
    return render_template("posts.html", posts=posts)


@app.route("/view_post/<post_id>")
def view_post(post_id):
    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template("view_post.html", post=post)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    posts = list(mongo.db.posts.find({"$text": {"$search": query}}))
    return render_template("posts.html", posts=posts)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
