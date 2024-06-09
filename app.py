# Import flask
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#Scss(app) # we added our app in our scss files 

# configuring the extension for the flask SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False # This is called as creating a flag for database, when a user goeas to your webpage after deployment it wont be using a preexisting db it will create a new one
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
    
# we are going to use a contect manager below
with app.app_context():
    db.create_all() 






# Below os the main homepage route which also plays the role of adding and reading the data
# In order to create a route we need to create a flask decorator and create a route
@app.route("/",methods = ["POST","GET"]) #since its the homepage we have just kept "/" in the bracket for now
# Index is going to be our homepage so we are create a route for the homepage below
def index():
    #add task function
    if request.method == "POST":
        current_task = request.form['content']
        new_task = MyTask(content = current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Error:{e}")
            return f"error:{e}"
    #See current added Task
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template("index.html", tasks = tasks)#as the routing file is by defaault named templates this will shouw us the index.html as our home page


# the below route plays the role of deleting the data form the added tasks
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"Error:{e}"


# and final the below route is created to update/edit the existing to-do tasks
@app.route("/update/<int:id>", methods = ["GET","POST"])
def update(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == "POST": 
        task.content = request.form["content"]
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error: {e}"
    else:
        return render_template('edit.html', task = task )






#The below code is used if you want to run the code inn local server without deploying
# # in order to give our flask app a final test: 
# # Thebelow is the runner and debugger
# if __name__ in "__main__":
#     # we are going to use a contect manager below
#     with app.app_context():
#         db.create_all() 
#     app.run(debug=True) # we have kept the debugger always on so that flask will keep updating itself

#Deploying the code
if __name__ == "__main__":
    app.run(debug=True) # we have kept the debugger always on so that flask will keep updating itself