
import flask
from flask import Flask, request, redirect, url_for, flash, jsonify, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

app.run()