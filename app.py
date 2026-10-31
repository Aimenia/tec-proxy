from flask import Flask, jsonify
import urllib.request
import json
import random

app = Flask(__name__)

STOPS = {
    "falmagne_chu": "N514",
    "gare_sport2000": "N896",
    "gare_bowling": "N891"
}

@app.route('/bus/<trajet>')
def get_bus(trajet):
    if trajet not in STOPS:
        return jsonify({"error": "Trajet inconnu"}), 400
    
    stop_id = STOPS[trajet]
    tec_url = f"https://www.letec.be/api/v1/stops/{stop_id}/passages?t={random.randint(1,100000)}"
    
    req = urllib.request.Request(tec_url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
