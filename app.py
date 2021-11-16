from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import enum

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "todo.db"))
SQLAlchemy.create_engine(database_file)

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)




# class and methods
class Priority(enum.Enum):
    aHIGH = 0
    bMEDIAN = 1
    cLOW = 2
tag_db={}

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    text = db.Column(db.Text)
    priority = db.Column(db.Enum(Priority))
    done = db.Column(db.Boolean,default=False)
    dateTime = db.Column(db.Text, default= datetime.now().strftime("%m/%d/%Y, %H:%M"))
    tag = db.Column(db.Text,default="")

def create_item(text, priority):
    item = Item(text = text, priority = priority)
    db.session.add(item)
    db.session.commit()
    db.session.refresh(item)
    
def read_items():
    return db.session.query(Item).order_by(Item.priority).all()


def update_tag(item_id,tags):
    tags_list=tags.strip().split(",")
    tags_list=[tag.strip().replace(" ","_") for tag in tags_list]
    tag_db[item_id]=tags_list

def update_item(item_id, text, done,priority,tag):
    update_tag(item_id,tag)
    db.session.query(Item).filter_by(id = item_id).update({
		"text": text,
        "done": True if done=="1" else False,
        "priority": priority,
        "tag": tag
	})
    db.session.commit()

def delete_item(item_id):
    db.session.query(Item).filter_by(id=item_id).delete()
    db.session.commit()

# app
@app.route("/", methods = ["POST", "GET"])
def view_index():
    if request.method == "POST":
        create_item(request.form['text'], request.form['priority'])
    return render_template("base.html", items = read_items())

@app.route("/about")
def about():
    return("TODO by Diane and Hoang")

# edit 
@app.route("/edit/<item_id>", methods = ["POST", "GET"])
def edit_item(item_id):
    if request.method == "POST":
        update_item(item_id, text=request.form['text'], done=request.form.get('done')
        ,priority=request.form.get('priority'),tag=request.form.get('tag'))
 
    return redirect("/", code=302)



@app.route("/delete/<item_id>", methods = ["POST", "GET"])
def delete(item_id):
    if request.method == "POST":
        delete_item(item_id)
    return redirect("/", code=303)

 
@app.template_filter()
def to_string(obj):
    if isinstance(obj, enum.Enum):
        return obj.value

    # For all other types, let Jinja use default behavior
    return obj

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)