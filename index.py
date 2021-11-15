#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/name', methods=['GET'])
# url arg name
def query_records_by_name():
    name = request.args.get('name')
    with open('data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'})

@app.route('/', methods=['GET'])
# url arg name
def query_records():
    with open('data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        if records:
            return jsonify(records)
        else:
            return jsonify({'error': 'data not found'})
            
@app.route('/', methods=['POST'])
# body payload
# name
# email
def create_record():
    record = json.loads(request.data)
    with open('data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

@app.route('/', methods=['PUT'])
# body payload
# name
# email         email address to be updated
def update_record():
    record = json.loads(request.data)
    new_records = []
    with open('data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
    
@app.route('/', methods=['DELETE'])
# body payload
# name       name to be deleted
def delte_record():
    record = json.loads(request.data)
    new_records = []
    with open('data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open('data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

app.run(host='0.0.0.0', port=81)

