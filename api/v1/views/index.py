#!/usr/bin/python3
"""create  an endpoint (route) will be to return the status of your API"""

import models
from models import storage
from flask import Blueprint, render_template, jsonify
from api.v1.views import app_views


@app_views.route("/status", methods=['GET'])
def son():
    """create a route"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def count():
    """returns number of objects per type"""
    todolist = {'states': State, 'users': User,
                'amenities': Amenity, 'cities': City,
                'places': Place, 'reviews': Review}
    cdict = {}
    for cls in todolist:
        cdict[cls] = storage.count(todolist[cls])
    return jsonify(cdict)
