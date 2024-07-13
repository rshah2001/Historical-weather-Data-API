from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

station = pd.read_csv("data_small/stations.txt", skiprows=17)
station = station[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    # Created a directory called templates and the function below will automatically look for the name
    # mentioned in the () inside the templates folder
    return render_template("home.html", data=station.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # this line will concatenate and add str(station) using zfill to add extra 0's in front
    # to get the station id directly
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    # Created a directory called templates and the function below will automatically look for the name
    # mentioned in the () inside the templates folder
    return {'Station': station,
            'date': date,
            'temperature': temperature}


@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")

    return result

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result

if __name__ == "__main__":
    app.run(debug=True, port=5001)
