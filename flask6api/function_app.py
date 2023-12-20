import azure.functions as func
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.function_name(name="Example")
@app.route(route="welcome")
def welcome(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    lastname = request.args.get('lastname', 'no last name provided')
    weather = request.args.get('weather', 'no weather provided. Look outside your window!')
    nameCapital = name.upper()
    lastnameCapital = lastname.upper()


    return func.HttpResponse(
        json.dumps(
        {'Welcome' : f'Hello {nameCapital} {lastnameCapital}!', 
        'Weather' : f'Today it is {weather} Thanks for stopping by!'}
        ),        
        status_code=200
        )