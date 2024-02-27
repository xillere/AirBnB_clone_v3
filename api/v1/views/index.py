#!/usr/bin/python3
"""create  an endpoint (route) will be to return the status of your API"""

from flask import Blueprint, render_template, jsonify
from api.v1.views import app_views


@app_views.route("/status", methods=['GET'])
def son():
    """create a route"""
    return jsonify({"status": "OK"})
