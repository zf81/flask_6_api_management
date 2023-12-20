from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/')
def home():
    return f"Welcome to Flask API Endpoint Server"

@app.route('/hello', methods=['GET'])
def hello_get():
    """
    This endpoint returns a message based on the information provided in the JSON body.
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: World
      - name: lastname
        in: query
        type: string
        required: false
        default: Lastname Not Provided
      - name: weather
        in: query
        type: string
        required: false
        default: nothing
    responses:
      200:
        description: A greeting message
    """
    name = request.args.get('name', 'World')
    lastname = request.args.get('lastname', 'no last name provided')
    weather = request.args.get('weather', 'no weather provided. Look outside your window!')
    nameCapital = name.upper()
    lastnameCapital = lastname.upper()

    return jsonify({'message': f'Hello {nameCapital} {lastnameCapital}! Today it is {weather}.'})



if __name__ == '__main__':
    app.run(debug=True)