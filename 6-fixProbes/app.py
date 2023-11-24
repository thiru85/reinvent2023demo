import sys
import boto3
import os
import json
import warnings
import random
from flask import Flask
import socket
from boto3.dynamodb.conditions import Key, Attr

app = Flask(__name__)

iterator = 0
 
@app.route("/cake")
def cake_api():
    query_list=[]
    l = []
    
    global iterator
    
    iterator += 1000
    
    for item in response['Items']:
        query_list.append(item)
    output=query_list[random.randint(0,len(response))]

    for i in range(0, len(response)):
        l.append("dummydata" * 1024 * iterator)
    
    return {
        "cakeID": output["id"],
        "cakeName": output["cakeName"],
        "cakeSize": output["cakeSize"],
        "containerID": socket.gethostname(),
    }
    

    
@app.route("/healthz")
def iAmHealthy():

    return {
        "message": "I am okay"
    }, 200
    print("Healthcheck done from: " + source_ip)


@app.route("/healthy")
def thisfunctiondoesNothing():

    return {
        "message": "there's nothing to see here"
    }, 400

def writetolog(x):
    with open('/tmp/logmeforever.txt', 'a') as f:
        f.write("THIS IS YOUR LIVENESSPROBE TEST")
        f.write("\n")
        f.write("someone was hungry for cake from: " + x)

warnings.filterwarnings('ignore', category=FutureWarning, module='botocore.client')

dynamodbobj = boto3.resource("dynamodb", )
table = dynamodbobj.Table(os.environ.get('TABLENAME'))
response = table.scan()

writetolog("test")
app.run(host='0.0.0.0', port='8080')

# this is a comment