import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] ='cook-book'
app.config["MONGO_URI"] ='mongodb://Mel28:AlexGauci333@ds131601.mlab.com:31601/cook-book'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html', 
        recipes=mongo.db.recipes.find())
        
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
        categories=mongo.db.categories.find())
    
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editrecipe.html', recipes=the_recipe, categories=all_categories)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'category_name':request.form.get('category_name'),
        'recipe_ingredients': request.form.get('recipe_ingredients'),
        'recipe_method': request.form.get('recipe_method'),
        'contains_meat':request.form.get('contains_meat'),
        'country_origin':request.form.get('country_origin')
        
    })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


@app.route('/get_categories/<food_type>')
def get_categories(food_type):
    recipes=mongo.db.recipes.find({'food_type': food_type})
    return render_template('categories.html',
        recipes=recipes)

    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)