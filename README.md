<h4> Mile Stone Project No. 4. Online Cook Book</h4>
<p> http://cook-book-4.herokuapp.com/get_recipes </p>
<p> https://github.com/Mel28/cook-book </p>
<h3>User Story</h3>
Hello!
Welcome to my 4th milestone project. For this project we were tasked with creating an online recipe database where users can add recipes,
edit recipes and delete recipes as they like. The home page displays all the recipes currently in the data base, the home screen is the place where users
can edit or delete a recipe. The user can filter by food type by using the dropdown list in the nav bar so if the data base gets large, users can
filter to their desired type of food recipe. There is an option in the nav bar where users can add a new recipe to the page.
<h3>Steps taken to build application</h3>
<li> sudo pip3 install flask command to install flask</li>
<li> sudo pip3 freeze --local > requirements.txt to create requirements file</li>
<li> used command echo web: python app.py > Procfile, to create Procfile</li>
<li> used command: heroku ps:scale web=1 to scale dynos</li>
<li> This Online cook book was built using Flask, Python, MongoDB, materialize and deployed to Heroku </li>
<li> Created MongoDB cook-book data base with two collections recipes and categories, added 6 documents to categories, and 6 to recipes, one for each category.
This then got expanded on during testing.</li>
<li> in Heroku settings add IP and Port as config variables, set IP to: 0.0.0.0 and PORT to: 5000</li>
<li> Connected flask app to mongoDB by creating a user on mongoDB and using the command 'sudo pip3 install flask_pymongo'</li>
<li> by using jinja statements, I accessed the MongoDB categories and referenced the key value pairs (documents)</li>
<h3> Style </h3>
<p> I have used materialize and bootstrap packages to give the app a more user-friendly style and to help with responsive design.
I have added my own media queries, so the app is responsive and usable no matter what device the user is using. </p>
<p> I dynamically added the background colour of the ul elements of the home page using javaScript.</p>
<h3> Testing and deployment </h3>
<li>Initial test:
@app.route('/')
def hello():
    return 'Hello world....third time lucky!'
<li> Testing done using byotest.py file in testing folder. All test's pass!
Checks were made by running this file during production of the app to test different functionalities that have been added</li>
<li> I have successfully deployed the app to heroku throughout the building of the application. The app can be viewed here:
            http://cook-book-4.herokuapp.com/get_recipes </li>
<li>The app has been tested in different browsers successfully such as firefox, internet explorer and chrome</li>

<h3>Acknowledgements</h3>
<p> Thanks to the tutors at the code institute for their help and advice during production of this project.</p>