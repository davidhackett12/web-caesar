from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method = 'POST'>
            <label for= "rotation"> Rotate by:</label>
            <input id= "rotation" type = "text" name = "rot" value = "0"/>
            <textarea type= "text" name= "text">{0}</textarea>
            <input type= "submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")
    

@app.route("/", methods = ['POST'])
def encrypt():
    rotation = request.form['rot']
    string = request.form['text']
    rotation_int = int(rotation)
    string_str = str(string)
    message = rotate_string(string_str,rotation_int)
    return form.format(message)
    
    

app.run()
