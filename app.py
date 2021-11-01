from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

todo_list = []

@app.route("/")
def index():
	return render_template("base.html", title="home")

@app.route("/about")
def about():
	return "About us: Naser and the cool kids from CS321"

@app.route("/add", methods=["POST"])
def add():
	todo_item = request.form.get("todo")
	todo_list.append(todo_item)
	print(todo_list[-1])

	return redirect(url_for("index"))


if __name__ == "__main__":
	app.run(debug=True) 