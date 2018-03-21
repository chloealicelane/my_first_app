from flask import Flask, render_template, request
# import = import library NB: capital F!
# render_template() = pass arguments through to tell Flask what HTML page to display
# in Flask a template = HTML file
app = Flask("myApp")
# defining flask application called MyApp
@app.route("/")
# @app.route is a decorator - before you call this method, do this code, and after finishes, do this other code 
# a decorator always starts with the @ sign
# route is a path/route/at this location
def hello():
	return "Hello World, here I am!"

@app.route("/idontexist")
def exist():
	return "Do I even exist tho?"

@app.route("/Chloe")
def chloe():
	return "Thats ma name bish"

@app.route("/<name>")
def hello_someone(name):
	return render_template("hello.html", name=name.title())
# <> = allows you to pass a variable in URL - can only use once

@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form
# now accessing a variable called request (in Flask), so we need to import it to use it - see top of page
	print form_data["email"]
	return "All OK"

app.run(debug=True)
# to run the application
#debug=True == will tell you in the browser what the problem is
# to see in your browser, copy httlp address in terminal (http://127.0.0.1:5000/)
# or use localhost:<number> ie localhost:5000
# ctrl c = close web server
