from flask import Flask,render_template,jsonify

from src.pipeline.prediction_pipeline import PredictPipeline,CustomData

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")