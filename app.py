from typing_extensions import NotRequired
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
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
	return "A todo list created by Diane and Hoang"

@app.route("/add", methods=["POST"])
def add():
	todo_item = request.form.get("todo")
	todo_list.append(todo_item)

	return redirect(url_for("index"))

@app.route("/remove/<string:item>")
def remove(item):
	todo_list.remove(item)
	return redirect(url_for("index"))

@app.route("/complete/<string:item>")
def complete(item):
    accomplished_list.append(item)
    todo_list.remove(item)
    return redirect(url_for("index"))

if __name__ == "__main__":
	app.run(debug=True)