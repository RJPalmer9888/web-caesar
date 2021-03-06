from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

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
        <form method="post">
            <label>
                Rotate by: <input type="text" name="rot" value="0"/>
            </label>
            <textarea name="text" class="mainarea"/>{0}</textarea>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypto():
    rot = request.form['rot']
    rot = int(rot)
    text = request.form['text']
    new = encrypt(text,rot)
    
    return form.format(new)

@app.route("/")
def index():
    return form.format("")

app.run()