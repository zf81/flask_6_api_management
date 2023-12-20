# flask_6_api_management

The goal of this week's assignment is to develop and document APIs using Flask, and manage them with Azure API Management.

# Flask-based RESTful API
- In Google Cloud Shell editor, created a new python file with code taken from Professor Hants' [app_flasgger.py](https://github.com/hantswilliams/HHA_504_2023/blob/main/WK6/code/flask/app_flasgger.py) file.
- You can find the final main.py file with edits here: [main.py](https://github.com/zf81/flask_6_api_management/blob/main/main.py)
- CD into the directory in which the .py file is located
- In the terminal, enter <code>pip install flasgger</code>
- Then enter, <code>python [your-file-name].py</code>

- Click on the generated link which will open up a new tab 
- In the URL of the new tab, replace the part after ".cloudshell.dev/" with the app route name specified in the python file followed by a "?"
- The app route name I used was "hello"
- Therefore, I typed this in the URL: <code>hello?name=fizzah&lastname=zaidi&weather=snowing</code>
- Here is the output after entering in the URl:
- <img width="500" alt="image" src="https://github.com/zf81/flask_6_api_management/blob/main/screenshots/flaskapp2.png?raw=true">

# OpenAPI Specification and Documentation

- To view Swagger documentation, type in "apidocs" after ".cloudshell.dev/"
- The URL will then return a page called "A swagger API." On this page, there will be a list of the possible requests a user can make of the endpoint

![swagger](https://github.com/zf81/flask_6_api_management/blob/main/screenshots/swagger.png)

# Azure API deployment
- To start deploying Flask app, First, go bakc to ther terminal and type <code>curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash</code>
- Type in <code>az</code> to ensure Azure has downloaded 
- To log into Azure, type <code>az login --use-device-code</code>
- Copy the code that is provided and click on the URL which will open a new tab 
- Paste the code when prompted 
- Click on the correcr account
- Click yes when prompted "Are you trying to sign in to Microsoft Azure CLI?"
- To install the Core Tools package, enter <code>sudo apt-get install azure-functions-core-tools-4</code> in ther terminal 

</br>

## Creating Function Project
- You will need to create a new function project by entering <code>func init [name-of-your-project] --python -m V2</code>
- To cd into the project folder, enter: <code>cd [name-of-your-project]</code> 
- In the Google Shell Editor, you will see a new folder that contains the files <code>local.settings.json</code>,  <code>function_app.py</code>, and <code>.gitignore</code>
- The code for the Azure app can be found in the <code>function_app.py</code> file
- Navigate to the <code>function_app.py</code> file and enter the following code:

```python
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
```

- Navigate to <code>local.settings.json</code> and for <code>AzureWebJobsFeatureFlags</code> check that it is set to <code>EnableWorkerIndexing</code>
- Navigate to <code>local.settings.json</code> and for <code>AzureWebJobsStorage</code> set it to <code>"UseDevelopmentStorage=true"</code>
- Go back to the terminal and enter the following <code>func start</code> to check if the function has been set up. It should return the following:

![funcstart](https://github.com/zf81/flask_6_api_management/blob/main/screenshots/funcstart.png)

- Clicking on the localhost link will open a new browser page and you should see this confirmation:

![azureapprunning](https://github.com/zf81/flask_6_api_management/blob/main/screenshots/azureapprunning.png)

</br>

## Create Azure Resources

- Enter the following to create an Azure resource group

```python
az group create --name [YOUR_RESOURCE_GROUP_NAME] --location [REGION]
```
Resource group name: fizzah507-rg
Location: eastus

</br>

- Enter the following to create storage account which will be located within the resource group:

```python
az storage account create --name [STORAGE_NAME] --location [REGION] --resource-group [YOUR_RESOURCE_GROUP_NAME] --sku Standard_LRS
```
Storage name: fizzahstorage
Location: eastus
Resource group name: fizzah507-rg

</br>

- Enter the following to create the function app:

```python
az functionapp create --resource-group [YOUR_RESOURCE_GROUP_NAME] --consumption-plan-location [REGION] --runtime python --runtime-version 3.9 --functions-version 4 --name [APP_NAME] --os-type linux --storage-account [STORAGE_NAME]
```
My app name was flask6api

</br>

## Azure Deployement 
- Enter <code>func azure functionapp publish [APP_NAME]</code> which wil deploy the app to Azure 
- If successful, you wil be provided with an "Azurewebsites" link 

My azure app link: https://flask6api.azurewebsites.net/api/hello

![azureapp2](https://github.com/zf81/flask_6_api_management/blob/main/screenshots/azureapp2.png)

- After entering in first and last name along with the weather in the URL, the page returned:
  
![azureapp1](https://github.com/zf81/flask_6_api_management/blob/main/screenshots/azureapp1.png)

</br>

# Errors
- After launching the Azure app using <code>func azure functionapp publish [APP_NAME]</code>, the URL link loaded a 401 error page. To fix this error, I went back to <code>function_app.py</code>. First, I saw this in the code
  
```python
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
```

I changed it to:

```python
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
```
By changing it to anonymous, now anyone could be able to view the app and they would not require permission

