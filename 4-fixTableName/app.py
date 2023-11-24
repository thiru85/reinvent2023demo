import sys
import boto3
import os
import json
import warnings
import random
from flask import Flask
import socket
from boto3.dynamodb.conditions import Key, Attr
from multiprocessing import Value
from flask import request

iterator = 0

app = Flask(__name__)
 
@app.route("/cake")
def cake_api():
    global iterator
    query_list=[]
    source_ip=request.remote_addr
    for item in response['Items']:
        query_list.append(item)
    output=query_list[random.randint(0,len(response))]
    iterator += 1

    if iterator > 8:
        sys.exit()

    return {
        "cakeID": output["id"],
        "cakeName": output["cakeName"],
        "cakeSize": output["cakeSize"],
        "containerID": socket.gethostname(),
        "iterator": iterator
    }
    print("someone was hungry for cake from: " + source_ip)
    writetolog(source_ip)
    
@app.route("/healthz")
def iAmHealthy():
    
    global iterator
    iterator += 1
    if iterator > 8:
        print("i have ceased to operate")
        sys.exit()
    
    return {
        "message": "I am okay"
    }, 200

@app.route("/healthy")
def thisfunctiondoesNothing():
    
    global iterator
    iterator += 1
    if iterator > 8:
        print("i have ceased to operate")
        sys.exit()
    
    return {
        "message": "there's nothing to see here"
    }, 400


warnings.filterwarnings('ignore', category=FutureWarning, module='botocore.client')
def writetolog(x):
    with open('/tmp/logmeforever.txt', 'a') as f:
        f.write("THIS IS YOUR LIVENESSPROBE TEST")
        f.write("\n")
        f.write("someone was hungry for cake from: " + x)

dynamodbobj = boto3.resource("dynamodb", )
table = dynamodbobj.Table(os.environ.get('TABLENAME'))
response = table.scan()
writetolog("test")
app.run(host='0.0.0.0', port='8080')

# this is a comment