from flask import Flask, render_template, request, redirect

app = Flask(__name__)
usuarios = {
    "admin@email.com": "1234"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        if email in usuarios and usuarios[email] == senha:
            return redirect("/home")
        else:
            return "<h1>Email ou senha inválidos</h1>"

    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")


app.run(debug=True)