from __future__ import print_function
import sys
from flask import Flask, render_template, request, jsonify
import openai
from openai import OpenAI
from config import Config
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Set up Azure OpenAI credentials


search_endpoint = "https://searchservice0610.search.windows.net"
search_index = "testing0610"
openai.api_key = app.config['AZURE_OPENAI_API_KEY']
openai.azure_endpoint=app.config['AZURE_OPENAI_ENDPOINT']
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
search_client = SearchClient(endpoint=search_endpoint, index_name=search_index, credential=AzureKeyCredential("M4wJRAcuGlA1TUCDH0f4S2Pb33Owm6R7Ons1TrcrEPAzSeD0IhKQ"))


user_input = input("Enter your username: ")
query = "SELECT * FROM users WHERE username = '" + user_input + "';"
execute_query(query) 

user_input = input("Enter expression: ")
result = eval(user_input)

user_input = input("Enter filename: ")
with open(user_input, 'r') as file:  # Vulnerable to directory traversal
    content = file.read()

    import os

directory = input("Enter the directory to list: ")
command = f"ls {directory}"  # Vulnerable to Command Injection
os.system(command)


if __name__ == '__main__':
    app.run(debug=True)
