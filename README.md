<h3>User Story</h3>
Hello!
welcolme to my 4th milestone project. For this project we were tasked with creating an online recipe database where users can add recipies,
edit recipes and delete recipes as they like. The home page displays all the recipes currently in the data base, you can filter by food type by using the
dropdown list in the nav bar so if the data base gets large, users can filter to thier desired type of food recipe. 
<h3>Steps taken to build application</h3>
<li> sudo pip3 install flask comand to install flask</li>
<li> sudo pip3 freeze --local > requirements.txt to create requirements file</li>
<li> used command echo web: python app.py > Procfile</li>
<li> used command: heroku ps:scale web=1 to scale dynos</li>
<li> This Online cook book was built using Flask, Python, MongoDB, materialize </li>
<li> Created MongoDB cook-book data base with two collections recipes and categories, added 6 documents to categories, and 6 to recipes, one for each category</li>
<li> in Heroku settings add IP and Port as config variables, set IP to: 0.0.0.0 and PORT to: 5000</li>
<li> Conected flask appto mongoDB by creating a user on mongoDB and using the comand 'sudo pip3 install flask_pymongo'</li>
<li> by using jinja statements, I accesssed the MongoDB categories and refrenced the key value pairs (documents)</li>
<h3>Functionality</h3>
<h3> Style </h3>
<h3> Testingand deployment </h3>
<li>Initial test:
@app.route('/')
def hello():
    return 'Hello world....third time lucky!'
<li> Testing done using byotest.py file in testing folder. All test's pass!</li>

<h3>Acknowledgements</h3>
<p> Thanks to the tutors at the code institute for thier help and advice</p>