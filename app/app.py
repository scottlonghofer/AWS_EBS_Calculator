from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        error = False
        error = not request.form["volume size"]
        if not error:
            size = request.form["volume size"]
            size = int(size) * 3 if int(size) > 33 else 100

        return render_template("index.html", size=size)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
