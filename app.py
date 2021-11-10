from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "todo.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

# class and methods
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    text = db.Column(db.Text)
    priority = db.Column(db.Enum)
    done = db.Column(db.Boolean)
    dateTime = db.Column(db.DateTime, default=datetime.now())
    
def create_item(text):
    item = Item(text = text)
    db.session.add(item)
    db.session.commit()
    db.session.refresh(item)
        
def read_items():
    return db.session.query(Item)
    
def update_item(item_id, text, done):
    db.session.query(Item).filter_by(id = item_id).update({
		"text": text,
		"done": True if done == "on" else False #checkbox
	})
    db.session.commit()
def update_item_priority(item_id,priority):
    db.session.query(Item).filter_by(id = item_id).update({
		"priority": priority
	})
    db.session.commit()        
def delete_item(item_id):
    db.session.query(Item).filter_by(id=item_id).delete()
    db.session.commit()

# app
@app.route("/", methods = ["POST", "GET"])
def view_index():
    if request.method == "POST":
        create_item(request.form['text'])
    return render_template("base.html", items = read_items())

@app.route("/about")
def about():
    return("TODO by Diane and Hoang")

# edit 
@app.route("/edit/<item_id>", methods = ["POST", "GET"])
def edit_note(item_id):
    if request.method == "POST":
        update_item(item_id, text=request.form['text'], done=request.form['done'])

    #elif request.method == "GET":
    #    delete_item(item_id)
    return redirect("/", code=302)

# delete 
@app.route("/delete/<item_id>", methods = ["POST", "GET"])
def edit_note(item_id):
    if request.method == "GET":
       delete_item(item_id)
    return redirect("/", code=302)

@app.route("/priority/<item_id>",methods=["POST","GET"])
def edit_priority(item_id):
    if request.method=="POST":
        update_item_priority(item_id,request.form['priority'])

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)