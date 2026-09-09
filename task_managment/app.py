from flask import Flask,redirect,render_template,request,url_for,session,flash
from task_manager import User,Task,Category,Comment,Tag,session  as db_session
app=Flask(__name__)
app.secret_key="My_secreate_key"

@app.route("/",methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        username=request.form["username"]
        email=request.form["email"]
        password=request.form["password"]
        if not username or not email or not password:
            return "Please enter valid details!"
        elif '@' not in email :
            return "Please enter a valid email address."
        elif len(password)<8:
            return "Please set a 8 character password"
        else:
            db_session.add(User(username=username,email=email,password=password))
            db_session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
     username=request.form["username"]
     email=request.form["email"]
     password=request.form["password"]
 
     if '@' not in email:
         return "Please enter a valid email address."
 
     if len(password) < 8:
         return "Please set an 8 character password."
 
     user = db_session.query(User).filter_by(
         username=username,
         email=email
     ).first()

 
     if not user:
         return "Login unsuccessful!"
 
     if user.password != password:
         return "Login unsuccessful!"

     session["user_id"] = user.id
     session["username"] = user.username
 
     return redirect(url_for("home"))
    return render_template("login.html")


@app.route("/logout",methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/create_task",methods=["GET","POST"])
def create_task():
    if request.method=="POST":
        title=request.form["title"]
        description=request.form["description"]
        category=request.form["category"]
        tag=request.form["tag"]
        if not title:
            flash("Please give title to the task!")
            return render_template(url_for("create_task"))
        if not description:
            flash("Please give description to the task!")
            return render_template(url_for("create_task"))
        if not category:
            flash("Please give category to the task!")
            return render_template(url_for("create_task"))
        if not tag:
            flash("Please give tag to the task!")
            return render_template(url_for("create_task"))
        

        db_session.add(Task(title=title,description=description,categories=category,tags=tag,user_id=session["user_id"]))
        db_session.commit()



    return render_template("create_task.html")

if __name__=="__main__":
    app.run(debug=True)