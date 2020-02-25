from flask import Blueprint, jsonify, request
from bson.json_util import dumps
from bson.json_util import loads
import json
from bson import json_util, SON

from .extensions import mongo 

main = Blueprint('main', __name__)

@main.route('/sons/all', methods=['GET'])
def get_sons():
    output = []
    collection = mongo.db.saudi_descriptions
    cursor = collection.find({})
    for val in cursor:
        # print("### move to next ###")
        try:
            output.append({i:val[i] for i in val if i!='_id'})
        except:
            continue
    
    return jsonify({'result':output})

# do sorting on the front end
# @main.route('sons/age/oldestfirst', methods=['GET'])
# def old_to_young():
# if needed: x = collection.find().sort("born", ASCENDING)
# from pymongo import ASCENDING, DESCENDING

@main.route('/sons/full_brothers', methods=['GET'])
def full_brothers():
    collection = mongo.db.saudi_descriptions
    pipeline= [
        {"$group": {"_id": "$mother", "records": {"$push": "$$ROOT.name"},"count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("_id", -1)])}
    ]
    return jsonify({'result':list(collection.aggregate(pipeline))})

@main.route('/sons/kings', methods=['GET'])
def kings():
    output = []
    collection = mongo.db.saudi_descriptions
    cursor = collection.find( { 'king':True } )
    for val in cursor:
        try:
            output.append({val['name']: {i:val[i] for i in val if i!='_id'}})
        except:
            continue
    
    return jsonify({'result':output})


@main.route('/sons/<string:name>', methods = ['GET'])
def get_son(name):
    output = []
    print("name is:",name)
    name = name.replace("+"," ")
    collection = mongo.db.saudi_descriptions
    cursor = collection.find( { 'name':name } )
    for val in cursor:
        output.append( {i:val[i] for i in val if i!='_id'} )
    return jsonify({'result':output})
