# Recipe Generator

This Streamlit app allows users to generate diverse cooking recipes based on their preferences for country, vegetarian or non-vegetarian dishes, and optional specific ingredients. The recipe generation is powered by OpenAI's GPT-3.5 Turbo model.

## Getting Started

To run this recipe generator locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone [https://github.com/Nabeel-ashrif/Gen-AI-cooking_app.git]
   ```

2. Install the required dependencies:

   ```bash
   pip install openai python-dotenv streamlit
   ```

3. Create a `.env` file in the project directory and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

   Obtain your API key by signing up at [OpenAI](https://beta.openai.com/signup/).

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

   Replace `app.py` with the actual filename if it's different.

## Usage

1. Select a country from the dropdown menu.
2. Choose between "Vegetarian," "Non-Vegetarian," or "No Preference" for the type of dish.
3. Optionally, enter other rquirements in the text input.
4. Click the "Generate Recipe" button to generate a cooking recipe based on the provided inputs.

## Code Structure

- `app.py`: Contains the Streamlit app code, including user interface and interaction.
- `openai.py`: Wraps OpenAI's API calls for generating recipes using the GPT-3.5 Turbo model.

## Environment Variables

Ensure you have a `.env` file in the project directory with the following content:

```env
OPENAI_API_KEY=your_api_key_here
```

## Dependencies

- [OpenAI Python](https://github.com/openai/openai-python): Python client for OpenAI API.
- [python-dotenv](https://github.com/theskumar/python-dotenv): Loads environment variables from a .env file.
- [Streamlit](https://github.com/streamlit/streamlit): Creates web applications with minimal effort.

## License



Feel free to contribute or report issues. Happy cooking! 🍲
