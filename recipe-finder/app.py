from flask import Flask, render_template, request
import helpers

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    # Collect all 10 ingredient input from the post request that was sent from index.html
    # If the input is empty, it will not be added to the list
    ingredients = []
    for i in range(1, 11):
        val = request.form.get(f"ingredient{i}")
        if val and val.strip():
            ingredients.append(val.strip())
    
    # If no ingredients were provided
    if not ingredients:
        return render_template("index.html", ingredients=[], recipes=[])

    recipes = helpers.search_spoonacular(ingredients)

    # Going to the results page
    return render_template("base.html", ingredients=ingredients, recipes=recipes)

if __name__ == "__main__":
    app.run(debug=True)

