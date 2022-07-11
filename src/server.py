import io
import json
import os
import threading
from flask import Flask, request, jsonify, abort
from ImageProcessing import process_image
from flask_cors import CORS 
from PIL import Image
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
def runImageProcessing(imgDir):
    os.chdir('ImageProcessing')
    out = []
    try:
        out = process_image(imgDir)
    except Exception as e:
        print(e)
    os.chdir('./..')
    #dump initial schema to file
    with open('common/outImageProcessing.json','w') as file:    
        jsonObj = json.dumps(out)
        file.write(jsonObj) 
@app.route('/imageprocessing', methods=['POST'])
def get_image():
    rm_file = "rm -rf common/outImageProcessing.json"
    os.system(rm_file)
    imgFile = request.files.get('image')
    imgFile.save('assets/'+imgFile.filename)
    imgDir = '../assets/'+imgFile.filename
    thread = threading.Thread(target=runImageProcessing, args=(imgDir,))
    thread.start()
    return jsonify({"image":imgFile.filename}) , 200    
@app.get('/ipoutput')
def get_ipoutput():
    if os.path.exists('common/outImageProcessing.json'):
        with open('common/outImageProcessing.json','r') as file:
            jsonObj = json.load(file)
            return jsonify(jsonObj)
    else:
        return jsonify({"error":"No output available"}) , 404
    
#options method
@app.route('/', methods=['OPTIONS'])
def options():
    return jsonify({'message': 'options'})



if __name__ == '__main__':
    app.run(debug=True,port = 5000)

