from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import streamlit as st

# Load environment variables from .env file
_ = load_dotenv(find_dotenv())  # read local .env file

# Create an OpenAI client
client = OpenAI()

# Function to generate recipe based on user input
def generate_recipe(country, vegetarian, ingredients):
    prompt = f"Generate a recipe for a dish from {country} that is {'vegetarian' if vegetarian else 'non-vegetarian'}"
    if ingredients:
        prompt += f" and includes {ingredients}"
    
    # Generate the recipe using OpenAI's GPT model
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a recipe assistant, skilled in generating diverse cooking recipes."},
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content

# Streamlit interface
st.title("Recipe Generator")

# User inputs
country = st.selectbox("Select Country", ["Pakistan", "Iran", "Afghanistan", "Italy", "India", "Oman", "Egypt", "Saudi Arabia", "China"])  # Replace with list of all countries
vegetarian = st.radio("Vegetarian or Non-Vegetarian", ["Vegetarian", "Non-Vegetarian", "No Preference"])
ingredients = st.text_input("Ingredients (optional)")

# Generate recipe on button click
if st.button("Generate Recipe"):
    recipe = generate_recipe(country, vegetarian == "Vegetarian", ingredients)
    
    # Display generated recipe
    st.header("Generated Recipe")
    st.write(recipe)
