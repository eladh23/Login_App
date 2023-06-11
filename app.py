from flask import Flask, render_template, request ,redirect

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def login():
    massage = "Error ,try again"
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "elad123" and password == "12345":
        return "<p>Welcome</p>"
    else:
        return render_template("login.html" , msg = massage)

@app.route("/notfound", methods=["POST", "GET"])
def not_found():
        return render_template("404.html")
    
if __name__ == "__main__":
    app.run(debug=True, port=9000)
