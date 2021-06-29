from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template ("index.html", num = 5)

@app.route('/<num>')
def boxes(num):
    return render_template ("four.html", num = int(num))

if __name__ == "__main__":

    app.run(debug=True)
