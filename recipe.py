#importing all the liabraries
import google.generativeai as genai
import os
from dotenv import load_dotenv
import re
import markdown

load_dotenv()

api_key = os.getenv("api_key")

genai.configure(api_key = os.environ["api_key"])


#get user input

'''
def get_user_input():
    ingredients = input("Enter the ingredients you have (comma-separated): ")
    dietary_preference = input("Enter your Dietary preferences : ")
    return ingredients, dietary_preference
'''

def generate_prompt(ingredients, dietary_preference):
    if dietary_preference.lower() == "none":
        dietary_preference = "no specific dietary preference"
    prompt = (
        f"Suggest a DETAILED recipe always with ONLY the following ingredients: {ingredients}."
        f"Consider the following dietary preferences: {dietary_preference}."
    )
    return prompt

def get_recipe_reccomendation(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    recipe = response.text
    recipe_html = markdown.markdown(recipe)
    return recipe_html


#main function to run everything

'''
def main():
    ingredients, dietary_preference = get_user_input()
    prompt = generate_prompt(ingredients, dietary_preference)
    recipe = get_recipe_reccomendation(prompt)
    print("\nRecommended Recipe:\n")
    print(recipe)

if __name__ == "__main__":
    main()
'''
