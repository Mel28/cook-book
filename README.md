<h3>User Story</h3>
<h3>Steps taken to build application</h3>
<li> sudo pip3 install flask comand to install flask</li>
<li> sudo pip3 freeze --local > requirements.txt to create requirements file</li>
<li> used command echo web: python app.py > Procfile</li>
<li> used command: heroku ps:scale web=1 to scale dynos</li>
<li> This Online cook book was built using Flask, Python, MongoDB, materialize </li>
<li> Created MongoDB cook-book data base with tow collections recipes and categories, added 6 documents to categories, and 6 to recipes, one for each category</li>
<li> in Heroku settings add IP and Port as config variables, set IP to: 0.0.0.0 and PORT to: 5000</li>
<li> Conected flask appto mongoDB by creating a user on mongoDB and using the comand 'sudo pip3 install flask_pymongo'</li>
<li> by using jinja statements, I accesssed the MongoDB categories and refrenced the key value pairs (documents)</li>
<h3> Testingand deployment </h3>
<li>@app.route('/')
def hello():
    return 'Hello world....third time lucky!'