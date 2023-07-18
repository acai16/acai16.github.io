from flask import Flask, render_template, request

app =Flask(__name__)



@app.route('/', methods = ["POST", "GET"])
def home():
    if request.method == 'POST':
        input = request.form.get('text')
        processed_text = input.upper()
        return render_template("index.html", processed_text = processed_text)
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)