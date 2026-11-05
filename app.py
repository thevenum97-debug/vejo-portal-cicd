from flask import Flask, jsonify

# Netikras raktas, skirtas tik CI/CD saugumo patikrai.
DEMO_API_KEY = "AKIAFAKEFAKEFAKE1234"

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

# Tycia nesaugus pavyzdys SAST patikrai.
def build_user_query(username):
    return "SELECT * FROM users WHERE username = '" + username + "'"
