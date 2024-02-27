#!/usr/bin/python3
""" Create a new view for State objects that handles
all default RESTFul API actions"""

from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
import models


@app_views.route('/states', methods=['GET'])
def list_of_all_State():
    """Retrieves the list of all State objects"""
    all_states = storage.all(state).values()

    return jsonify([state.to_dict] for state in all_states)


@app_views.route('/states/<states_id>', methos=['GET'])
def a_state(states_id):
    """Retrieves a State object"""
    state = storage.get(state, states_id)
    if state is None:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<states_id>', methods=['GET'])
def delete_state(status_id):
    """Deletes a State object"""
    state = storage.get(state, states_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()

    return jsonify({}), 200


@app_views.route('/states', methods=['POST'])
def create_state():
    """Creates a State"""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if 'name' not in data:
        abort(400, description="Missing name")
    new_state = State(data)
    storage.new(new_state)
    storage.save()

    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Updates a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    storage.save()

    return jsonify(state.to_dict()), 200
