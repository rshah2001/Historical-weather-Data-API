from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    # Created a directory called templates and the function below will automatically look for the name
    # mentioned in the () inside the templates folder
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    # Created a directory called templates and the function below will automatically look for the name
    # mentioned in the () inside the templates folder
    return {"Station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
