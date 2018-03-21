from flask import Flask, render_template
# import = import library NB: capital F!
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
def name():
	return "Thats ma name bish"

app.run(debug=True)
# to run the application
#debug=True == will tell you in the browser what the problem is
# to see in your browser, copy httlp address in terminal (http://127.0.0.1:5000/)
# or use localhost:<number> ie localhost:5000
# ctrl c = close web server
