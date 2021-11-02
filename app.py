from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

todo_list = []
accomplished_list = []

@app.route("/")
def index():
	return render_template("base.html", title="home", todo_list=todo_list, accomplished_list = accomplished_list)

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