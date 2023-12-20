# flask_6_api_management

The goal of this week's assignment is to develop and document APIs using Flask, and manage them with Azure API Management.

## Flask-based RESTful API
- In Google Cloud Shell editor, created a new python file with code taken from Professor Hants' [app_flasgger.py](https://github.com/hantswilliams/HHA_504_2023/blob/main/WK6/code/flask/app_flasgger.py) file.
- You can find the final main.py file with edits here: [main.py](https://github.com/zf81/flask_6_api_management/blob/main/main.py)
- CD into the directory in which the .py file is located
- In the terminal, enter <code>pip install flasgger</code>
- Then enter, <code>python [you-file-name].py</code>

- Click on the generated link which will open up a new tab 
- In the URL of the new tab, replace the part after ".cloudshell.dev/" with the app route name specified in the python file followed by a "?"
- The app route name I used was "hello"
- Therefore, I typed this in the URL: <code>hello?name=fizzah&lastname=zaidi&weather=snowing</code>
- Here is the output after entering in the URl:
- <img width="500" alt="image" src="https://github.com/zf81/flask_6_api_management/blob/main/screenshots/flaskapp2.png?raw=true">
