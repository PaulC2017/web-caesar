from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color:#eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;   
            }
       
        </style>
    
    </head>

    
    <body>  

    <form action="/" method="post">
        <label for="new-rotate">
            Rotate by
            <input type="text" value = "0" id="new-rotate" name="rot"/>
         </label>
        <input type="submit" value="Submit"/>
        <br>
    </form>
    <form action= "/" method="post" >
    <textarea rows="4" cols="50" name="text">   </textarea>

    
       



    </body>
</html>

"""


@app.route("/" , methods=["post"])
def encrypt():
    the_text = request.form.get("text")
    the_text=str(the_text)
    the_rot = request.form.get("rot")
    the_rot = int(the_rot)
    encrypt = rotate_string(the_text,the_rot)
    result = "<h1>" + encrypt + "</h1>"
    return result



@app.route("/" )
def index():
    return form 



app.run()