from flask import Flask, render_template

app = Flask(__name__)

@app.route('/about')
def about():
    return ('huamani molina')

if __name__ == "__main__":
    app.run(debug=True)
