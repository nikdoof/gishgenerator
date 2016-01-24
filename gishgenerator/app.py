from flask import Flask, render_template
from gishgenerator import generate_name

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    name, img1, img2 = generate_name()
    return render_template('index.html', name=name, img1=img1, img2=img2)

if __name__ == '__main__':
    app.run()
