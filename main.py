from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import streamlit as st

# Load environment variables from .env file
_ = load_dotenv(find_dotenv())  # read local .env file

# Create an OpenAI client
client = OpenAI()

# Function to generate recipe based on user input
def generate_recipe(country, vegetarian, ingredients, age_group=None, serving_size=2, spice="Default", translate=False):
    prompt = f"Generate a recipe for {serving_size} persons with {spice} spice level"
    
    if age_group:
        prompt += f" suitable for {age_group} from"
    else:
        prompt += " from"
    
    prompt += f" {country} that is {'vegetarian' if vegetarian else 'non-vegetarian'}"
    
    if ingredients:
        prompt += f" and includes {ingredients}"
    
    if translate:
        # Include a request for translation in the prompt
        prompt += f", also translate the generated recipe to the national language of {country}"
    
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
translate_option = st.radio("Also show recipie in National Language", ["No", "Yes"])
vegetarian = st.radio("Vegetarian or Non-Vegetarian", ["Vegetarian", "Non-Vegetarian", "No Preference"])
ingredients = st.text_input("Ingredients (optional)")
age_group = st.selectbox("Select Age Group", ["All Ages", "Infants (6-12 months)", "Toddlers (1-3 years)", "Preschoolers (4-6 years)", "Children (7-12 years)", "Teens (13-18 years)", "Young Adults (19-30 years)", "Adults (31-50 years)", "Mature Adults (51-65 years)", "Seniors (66+ years)"])  # Replace with list of all ages
serving_size = st.slider("Select Serving Size (Persons) ", min_value=1, max_value=20, value=2, step=1)  # Replace with number of persons
spice = st.selectbox("Select Spice level", ["Default", "Mild", "Medium", "Spicy", "Extra Spicy"])  # Replace with required spice levels


# Generate recipe on button click
if st.button("Generate Recipe"):
    recipe = generate_recipe(country, vegetarian == "Vegetarian", ingredients, age_group, serving_size, spice, translate_option == "Yes")
    
    # Display generated recipe
    st.header("Generated Recipe")
    st.write(recipe)
