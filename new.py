from flask import Flask, render_template, redirect, request
from forms import LatLongForm
import json
import sys
import pickle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'arjun'

# this is used for routing the app to the selected server
# in this case it is localhost
# app.route will route the app to the correct web page

@app.route('/', methods = ['GET', 'POST'])
def askinfo():
    form = LatLongForm()
    if form.is_submitted():
        loc_data = request.form
        print(loc_data)
        #return render_template('location_data.html', markers=loc_data)
        # name of the file which will get created
        with open("markers.json", "r") as data_file:    
            data = json.load(data_file)
        data.append(loc_data)
        with open("markers.json", "w") as out_file:
            json.dump(data, out_file)

   return render_template('enter_locdata.html', form=form)


# templates in flask are blueprints for html code which you can use
# render_template will run the html file
# Jinja can be used to pass variables from flask statements into the html page
#   for direct use by double curly braces {{}}
#   Jinja is a markup language used in templating

if __name__ == '__main__':
    app.debug = True
    app.run()
