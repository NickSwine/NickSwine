import requests, os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def search_spoonacular(ingredients_list):
    ingredients = [i.strip() for i in ingredients_list if i and i.strip()]
    
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "ingredients": ",".join(ingredients),
        "number": 10,
        "ranking": "1",  # Optional: can be used to rank results
        "apiKey": os.getenv("API_KEY")
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        return r.json()  # list of recipe dictionaries
    except Exception as e:
        print("Error calling Spoonacular API:", e)
        return []
