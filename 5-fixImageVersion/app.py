import sys
import boto3
import os
import json
import warnings
import random
from flask import Flask
import socket
from boto3.dynamodb.conditions import Key, Attr
from flask import request

app = Flask(__name__)
 
@app.route("/cake")
def cake_api():
    query_list=[]
    source_ip=request.remote_addr
    for item in response['Items']:
        query_list.append(item)
    output=query_list[random.randint(0,len(response))]

    return {
        "cakeID": output["id"],
        "cakeName": output["cakeName"],
        "cakeSize": output["cakeSize"],
        "containerID": socket.gethostname(),
    }
    writetolog(source_ip)

    
@app.route("/healthz")
def iAmHealthy():

    return {
        "message": "I am okay"
    }, 200

@app.route("/healthy")
def thisfunctiondoesNothing():

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