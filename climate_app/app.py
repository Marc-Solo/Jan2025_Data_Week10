import pandas as pd
from flask import Flask, jsonify
from sql_helper import SQLHelper


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sqlHelper = SQLHelper()


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        # f"/api/v1.0/precipitation2"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Execute queries
    df = sqlHelper.queryPrecipitationORM()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/stations")
def stations():
    # Execute queries
    df = sqlHelper.queryStationsORM()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/tobs")
def tobs():
    # Execute queries
    df = sqlHelper.queryTobsORM()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
