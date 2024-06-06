# Import flask
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# In order to create a route we need to create a flask decorator and create a route
@app.route("/") #since its the homepage we have just kept "/" in the bracket for now
# Index is going to be our homepage so we are create a route for the homepage below
def index():
    return render_template("index.html")#as the routing file is by defaault named templates this will shouw us the index.html as our home page

# in order to give our flask app a final test: 
if __name__ in "__main__":
    app.run(debug=True) # we have kept the debugger always on so that flask will keep updating itself
