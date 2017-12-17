from flask import Flask,request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

form = """ 
<!doctype html>
<html>
    <head>
        <style>
            form (
                 background-color:#eee;
                 padding:20px;
                 margin: 0 auto;
                 width:540px;
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


     <form action="/"method="post">
     <div>
        <label for="rotate"> Rotate by: </label>
            
            <input type="text" id="rotate" name="rot" value="0"/>
           
        
    </div>
    <br>
    
        <textarea   type="text" name="text">

        </textarea>
        <br>
        <input type="submit" value="Submit Query"/>
    
    </body
    
</html>

"""
    
    
        


@app.route("/")
def index():
    return form



@app.route("/" methods=[POST}])
def encrypt(numRot,textToRot):
    num_rot = numRot
    text_to_rot = textToRot
    return "<h1>" + rotate_string(text_to_rot,num_rot) + "</h1>"

app.run()