#!/usr/bin/python3

from flask import Blueprint, render_template, jsonify
from api.v1.views import app_views

@app_views.route("/status", methods=['GET'])
def son():
    return jsonify({"status": "OK"})
