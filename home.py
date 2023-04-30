from flask import Flask, render_template, request
import requests
import wikipedia

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("search_page.html", content=name)

@app.route("/")
def admin():
    return render_template("search_page.html")

@app.route("/carinfo")
def info():
    brand = request.args.get('brand')
    model = request.args.get('model')
    param = str(brand + model)
    wikipedia.set_lang('en')
    result = wikipedia.search(param)
    print(result)
    return render_template("car_info.html", brand=brand,model = model, info = result)

if __name__ == "__main__":
    app.run(debug=True)