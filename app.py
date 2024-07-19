from flask import Flask, render_template
from flask import request
from recipe import generate_prompt, get_recipe_reccomendation
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ingredients = request.form['ingredients']
    dietary_preference = "none"  # Add a way to collect dietary preference from the form if needed
    prompt = generate_prompt(ingredients, dietary_preference)
    recipe_html = get_recipe_reccomendation(prompt)
    return render_template('result.html', result = recipe_html , user_input = ingredients)

if __name__ == '__main__':
   app.run()