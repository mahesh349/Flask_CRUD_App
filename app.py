# Import flask
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#Scss(app) # we added our app in our scss files 

# configuring the extension for the flask SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app) #we added our app in our SQLAlchemy

#we nned to create class model
class MyTask(db.Model):
    #creating all the columns of the table in database
    id = db.Column(db.Integer, primary_key = True) #giving sql attributes to the column like the input should be an integer and we have made the integer column a primary key
    content = db.Column(db.String(100),nullable = False) #giving the content column a string datatype input option with a input limit of 100 characters
    complete = db.Column(db.Integer, default = 0)
    created = db.Column(db.DateTime, default = datetime.utcnow) #we added the date and time sql datatype in the column to show when it was created and also imported dateandtime to add the current time stamps

    # using dunder method of a string representation
    def __repr__(self) -> str:
        return f"Task {self.id}"


# In order to create a route we need to create a flask decorator and create a route
@app.route("/") #since its the homepage we have just kept "/" in the bracket for now
# Index is going to be our homepage so we are create a route for the homepage below
def index():
    return render_template("index.html")#as the routing file is by defaault named templates this will shouw us the index.html as our home page

# in order to give our flask app a final test: 
if __name__ in "__main__":
    # we are going to use a contect manager below
    with app.app_context():
        db.create_all() 
    app.run(debug=True) # we have kept the debugger always on so that flask will keep updating itself

