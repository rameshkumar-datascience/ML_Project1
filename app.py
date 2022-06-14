from flask import Flask

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "Oh Yes! you have successfully setup CI-CD, deployed app into Heroku platform"

if __name__=="__main__":
    app.run(debug=True)