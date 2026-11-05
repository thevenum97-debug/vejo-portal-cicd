from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def portal():
    return jsonify(
        imone="VejoEnergija",
        paskirtis="Mokomasis saugumo ivykiu portalas",
        ivykiai=[
            "Nesekmingas prisijungimas",
            "Aptiktas itartinas failas",
            "Reikalinga serverio saugumo perziura"
        ]
    )

@app.get("/healthz")
def health():
    return jsonify(status="ok")

# SQL tekstas ir parametro reiksme perduodami atskirai.
def build_user_query(username):
    query = "SELECT * FROM users WHERE username = ?"
    return query, (username,)
