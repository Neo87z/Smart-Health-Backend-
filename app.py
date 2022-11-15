import json
from flask import Flask, Response, request
from flask_cors import CORS
from inference import *

app = Flask(__name__)
CORS(app)

doctor = DoctorRecommendation()
doctor.run()

###############################################################################

host = 'localhost'
port = 5000

###############################################################################

@app.route('/scoliosis', methods=['GET', 'POST'])
def scoliosis():
    try:
        message = request.get_json(force=True)
        response = doctor.make_response(message)
        return Response(
                        json.dumps(response), 
                        mimetype='application/json'
                        )
    except:
        return Response(
                        json.dumps({'error': 'Response Failed. Please make a valid Request !!!'}), 
                        mimetype='application/json'
                        )


if __name__ == "__main__": 
    app.run(
        debug=True, 
        host=host, 
        port=port, 
        threaded=False, 
        use_reloader=True
        )

    # {"ScoliosisType": "kyphosis", "SpineAngle": "10"}