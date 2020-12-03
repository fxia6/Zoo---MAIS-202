<h1>Project Description</h1>
This is a project to classify zoo animals, and to guess the type of animal the user is thinking of by delivering a webapp using Flask.

<h1>How to run the app</h1>
1. Install scikit-learn, flask, numpy, pandas
2. Change into the main directory of this repository 
3. Set the environment variable using command 'export FLASK_APP=app.py'
4. Run using command 'flask run'
5. Click in the http link that pops up and you can now see the webapp

<h1>Repository Organization</h1>
1. data: all the csv files from kaggle we used as our data
2. deliverables: deliverable 1,2,3
3. static: an image of akinator
4. templates: html templates
zoo.csv and class.csv are data files relevant to the project.
zoo.py is the python script to train our model.
zoo.ipynb is the python file that contains the process of hyperparameter tuning.
app.py is the main python script to instantiate Flask server.
