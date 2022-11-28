from flask import Flask, render_template

app = Flask(__name__)

achtelfinals = [
    {"Spiel1": {"home": "Germany", "away": "Germany"}},
    {"Spiel2": {"home": "Germany", "away": "Germany"}},
    {"Spiel3": {"home": "Germany", "away": "Germany"}},
    {"Spiel4": {"home": "Germany", "away": "Germany"}},
    {"Spiel5": {"home": "Germany", "away": "Germany"}},
    {"Spiel6": {"home": "Germany", "away": "Germany"}},
    {"Spiel7": {"home": "Germany", "away": "Germany"}},
    {"Spiel8": {"home": "Germany", "away": "Germany"}},
]

viertelfinals = [
    {"Spiel1": {"home": None, "away": None}},
    {"Spiel2": {"home": None, "away": None}},
    {"Spiel3": {"home": None, "away": None}},
    {"Spiel4": {"home": None, "away": None}},
]

halbfinals = [
    {"Spiel1": {"home": None, "away": None}},
    {"Spiel2": {"home": None, "away": None}},
]

finale = {"home": None, "away": None}


@app.get("/")
def home():
    render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=4000)
