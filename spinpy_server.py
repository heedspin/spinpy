from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

@app.route('/render_mol')
def render_mol():
    mol_path = './data/6tap.cif'
    return '<h1>Render Molecule</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)