from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

todo_list = []

@app.route("/")
def index():
	return render_template("base.html", title="home", list=todo_list)

@app.route("/about")
def about():
	return "A todo list created by Diane and Hoang"

@app.route("/add", methods=["POST"])
def add():
	todo_item = request.form.get("todo")
	todo_list.append(todo_item)
	print(todo_list[-1])

	return redirect(url_for("index"))


if __name__ == "__main__":
	app.run(debug=True) 