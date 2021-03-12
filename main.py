import os
import threading
import subprocess
from flask import Flask, request, jsonify
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route('/postreceiveservice', methods=['POST'])
def postReceiveService():
        return handleRequest(request)

@app.route('/postreceiveapp', methods=['POST'])
def postReceiveApp():
        return handleRequest(request)

def handleRequest(request):
        url = request.json['repository']['url'] + ".git"
        repoName = request.json['repository']['name']
        
        t = threading.Thread(target=thread_function, args=(repoName, url))
        t.start()

        resp = jsonify(success=True)
        resp.status_code = 200
        return resp

def thread_function(repoName, url):
        try:
                os.system('echo ' + repoName + " " + url + ' | netcat localhost 7777')
                print("finished deployment!")
        except Exception as e:
                print('issues while running deployemnet ' + str(e))

if __name__ == "__main__":
        print("hello mentimeter!")
        app.run(host='0.0.0.0', port=9001, debug=True)