from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

@app.route('/render_mol')
def render_mol():
    mol_path = './data/6tap.cif'
    
    # Check if the file exists
    if not os.path.exists(mol_path):
        return f'<h1>Error: File {mol_path} not found</h1>'
    
    # Read the molecular structure file
    with open(mol_path, 'r') as f:
        mol_data = f.read()
    
    # HTML template with 3Dmol.js
    html_template = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Molecule Viewer</title>
        <script src="https://3dmol.csb.pitt.edu/build/3Dmol-min.js"></script>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            #molviewer {{ width: 800px; height: 600px; border: 1px solid #ccc; }}
        </style>
    </head>
    <body>
        <h1>Molecule Viewer</h1>
        <p>Rendering: {mol_path}</p>
        <div id="molviewer"></div>
        
        <script>
            var viewer = $3Dmol.createViewer("molviewer", {{backgroundColor: "white"}});
            
            // Add the molecular data (CIF format)
            viewer.addModel(`{mol_data}`, "cif");
            
            // Set visualization style
            viewer.setStyle({{}}, {{stick: {{}}, sphere: {{scale: 0.3}}}});
            
            // Zoom to fit and render
            viewer.zoomTo();
            viewer.render();
        </script>
    </body>
    </html>
    '''
    
    return html_template

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)