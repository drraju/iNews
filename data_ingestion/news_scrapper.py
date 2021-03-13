# import all packages. later convert these into requirements.txt
#from flask import Flask, render_template, request, jsonify, app
from bs4 import BeautifulSoup as bs
#from flask_cors import CORS, cross_origin
import requests
from urllib.request import urlopen as uReq

# Initialize the flask app and assing to newsapp
#newsapp = Flask(__name__)

"""
Author : Raju Datla
App: To scrap news websites we will use
find(element_tag, attribute) which returns first matching item
find_all(element_tag, attrbute) which returns  a list of matching items
"""

# Accessing raw article
url = 'https://www.bbc.co.uk/news/world-europe-49345912'
article = requests.get(url)
soup = bs(article.content, 'html.parser')
# Create the routes/ # route with allowed methods as POST and GET
#@app.route('/', methods=['POST', 'GET'])
def get_bbc_text(url: str) -> list:
    """Parse bbc article and return text in list of strings"""

    article = requests.get(url)
    soup = bs(article.content, "html.parser")
    body = soup.find(property="articleBody")
    text = [p.text for p in body.find_all("p")]
    return text

print(get_bbc_text(url))


# let us pass the article content to BeautifulSoup and specify the HTML parser
#soup = bs(article.content, 'html.parser')

# Locate the elements on browser and find which dev.
