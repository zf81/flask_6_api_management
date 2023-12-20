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
