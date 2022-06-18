from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    logging.info("We are testing logging")
    return "Oh Yes! you have successfully setup CI-CD, deployed app into Heroku platform"

if __name__=="__main__":
    app.run(debug=True)