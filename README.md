# Overview
This is the backend code for a restaurant ordering application. Checkout https://github.com/mandar-01/Sweetgreen-Frontend/tree/main for the frontend code. 

# Installation instructions
This article assumes you have Python3 installed. If not, install Python 3, preferable Python 3.11.2

It is highly recommended to run this code in a python virtual environment. Setup a python virtual environment using `python -m venv your_environment_name`

## Activate the virtual environment and start the Flask server: 

Go to the root folder where you created the virtual environment.

For Windows:Execute `your_environment_name/Scripts/activate`

For Linux:
Execute `source your_environment_name/bin/activate`

Install all the requirements from requirements.txt:
`pip install -r requirements.txt`

Go to the root folder of this repository. Start the Flask server using:
`flask --app .\api\index.py run`
