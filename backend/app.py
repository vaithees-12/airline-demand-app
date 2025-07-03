from flask import Flask, jsonify
import requests
import pandas as pd
from flask_cors import CORS
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

BASE_URL = "https://opensky-network.org/api/states/all"

# Fetch flight data from OpenSky
def get_flight_data():
    try:
        res = requests.get(BASE_URL)
        if res.status_code != 200:
            return pd.DataFrame()
        raw = res.json()['states']
        columns = [
            'icao24', 'callsign', 'origin_country', 'time_position',
            'last_contact', 'longitude', 'latitude', 'baro_altitude',
            'on_ground', 'velocity', 'true_track', 'vertical_rate',
            'sensors', 'geo_altitude', 'squawk', 'spi', 'position_source'
        ]
        df = pd.DataFrame(raw, columns=columns)
        df['time_position'] = pd.to_datetime(df['time_position'], unit='s', errors='coerce')
        return df
    except Exception as e:
        print("Error fetching flight data:", e)
        return pd.DataFrame()

# API: All flights with position
@app.route("/api/flights")
def flights():
    df = get_flight_data()
    result = df[['callsign', 'origin_country', 'latitude', 'longitude', 'velocity']].dropna().to_dict(orient='records')
    return jsonify(result)

# API: Popular routes (simulated from callsign prefix)
@app.route("/api/popular-routes")
def popular_routes():
    df = get_flight_data()
    df = df.dropna(subset=['callsign', 'origin_country'])
    df['route'] = df['origin_country'] + " ➝ " + df['callsign'].str[:3].fillna("UNK")
    route_counts = df['route'].value_counts().head(10).reset_index()
    route_counts.columns = ['route', 'count']
    return jsonify(route_counts.to_dict(orient='records'))

# API: Speed distribution (binning velocities)
@app.route("/api/speed-distribution")
def speed_distribution():
    df = get_flight_data()
    df = df[['velocity']].dropna()
    if df.empty:
        return jsonify([])
    bins = pd.cut(df['velocity'], bins=10).value_counts().sort_index()
    result = [{"range": str(i), "count": int(bins[i])} for i in bins.index]
    return jsonify(result)

# API: High-demand times by hour
@app.route("/api/high-demand-times")
def high_demand():
    df = get_flight_data()
    df = df.dropna(subset=['time_position'])
    if df.empty:
        return jsonify([])
    df['hour'] = df['time_position'].dt.hour
    demand = df['hour'].value_counts().reindex(range(24), fill_value=0).sort_index()
    result = [{"hour": h, "count": int(demand[h])} for h in demand.index]
    return jsonify(result)

# API: Simulated price trends
@app.route("/api/price-trends")
def price_trends():
    routes = ["DEL ➝ BOM", "SYD ➝ MEL", "NYC ➝ LAX", "DXB ➝ LHR", "SIN ➝ BKK",
              "CDG ➝ AMS", "LAX ➝ SFO", "FRA ➝ DUB", "MAD ➝ BCN", "JFK ➝ ATL"]
    prices = [{"route": r, "price": round(random.uniform(80, 400), 2)} for r in routes]
    return jsonify(prices)

# Run the server
if __name__ == "__main__":
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=True)

