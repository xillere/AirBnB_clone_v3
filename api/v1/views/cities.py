#!/usr/bin/python3
"""cities api"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.city import City
from models.state import State
from datetime import datetime
import uuid


@app_views.route('/states/<state_id>/cities', methods=['GET'])
@app_views.route('/states/<state_id>/cities/', methods=['GET'])
def cities_in_state(state_id):
    """retuens a list of all City objects within the state"""
    list_states = storage.all("State").values()
    state_list = [obj.to_dict() for obj in list_states if obj.id == state_id]
    if state_list == []:
        abort(404)
    list_cities = [obj.to_dict() for obj in storage.all("City").values()
                   if state_id == obj.state_id]
    return jsonify(list_cities)


@app_views.route('/states/<state_id>/cities', methods=['POST'])
@app_views.route('/states/<state_id>/cities/', methods=['POST'])
def create_city(state_id):
    """makes a City"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    list_states = storage.all("State").values()
    state_list = [obj.to_dict() for obj in list_states if obj.id == state_id]
    if state_list == []:
        abort(404)
    cities = []
    new = City(name=request.json['name'], state_id=state_id)
    storage.new(new)
    storage.save()
    cities.append(new.to_dict())
    return jsonify(cities[0]), 201


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """gets a city"""
    e_cities = storage.all("City").values()
    city_list = [obj.to_dict() for obj in e_cities if obj.id == city_id]
    if city_list == []:
        abort(404)
    return jsonify(city_obj[0])


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """deletes a city"""
    e_cities = storage.all("City").values()
    city_list = [obj.to_dict() for obj in e_cities if obj.id == city_id]
    if city_list == []:
        abort(404)
    city_list.remove(city_list[0])
    for obj in e_cities:
        if obj.id == city_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """updates city object"""
    all_cities = storage.all("City").values()
    city_obj = [obj.to_dict() for obj in all_cities if obj.id == city_id]
    if city_obj == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    city_obj[0]['name'] = request.json['name']
    for obj in all_cities:
        if obj.id == city_id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(city_obj[0]), 200
