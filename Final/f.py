from flask import Flask, render_template_string, request, jsonify ,render_template
import json

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <style>
      /* Import Google font - Poppins */
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap");
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}
body {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  background-image: url("/static/back.png");
}
.container {
  position: relative;
  max-width: 700px;
  width: 100%;
  background: #fff;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}
.container header {
  font-size: 1.5rem;
  color: #333;
  font-weight: 500;
  text-align: center;
}
.container .form {
  margin-top: 30px;
}
.form .input-box {
  width: 100%;
  margin-top: 20px;
}
.input-box label {
  color: #333;
}
.form :where(.input-box input, .select-box) {
  position: relative;
  height: 50px;
  width: 100%;
  outline: none;
  font-size: 1rem;
  color: #707070;
  margin-top: 8px;
  border: 1px solid #ddd;
  border-radius: 6px;
  padding: 0 15px;
}
.input-box input:focus {
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.1);
}
.form .column {
  display: flex;
  column-gap: 15px;
}
.form .gender-box {
  margin-top: 20px;
}
.gender-box h3 {
  color: #333;
  font-size: 1rem;
  font-weight: 400;
  margin-bottom: 8px;
}
.form :where(.gender-option, .gender) {
  display: flex;
  align-items: center;
  column-gap: 50px;
  flex-wrap: wrap;
}
.form .gender {
  column-gap: 5px;
}
.gender input {
  accent-color: rgb(130, 106, 251);
}
.form :where(.gender input, .gender label) {
  cursor: pointer;
}
.gender label {
  color: #707070;
}
.address :where(input, .select-box) {
  margin-top: 15px;
}
.select-box select {
  height: 100%;
  width: 100%;
  outline: none;
  border: none;
  color: #707070;
  font-size: 1rem;
}
.form button {
  height: 55px;
  width: 100%;
  color: #fff;
  font-size: 1rem;
  font-weight: 400;
  margin-top: 30px;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  background: rgb(130, 106, 251);
}
.form button:hover {
  background: rgb(86, 85, 92);
}
/*Responsive*/
@media screen and (max-width: 500px) {
  .form .column {
    flex-wrap: wrap;
  }
  .form :where(.gender-option, .gender) {
    row-gap: 15px;
  }
}

textarea {
    width: 100%; 
    padding: 10px; 
    border: 1px solid #ccc; 
    border-radius: 5px; 
    box-sizing: border-box; 
  	resize : none;
}

    </style>
    <!--<link rel="stylesheet" href="style.css" />-->
</head>
<body>
    <section class="container">
      <header>ADD YOUR NEW LOCATIONS</header>
      <form action="#" class="form" method = "post">
        <div class="input-box">
          <label>Full Name</label>
          <input type="text" name="full_name" placeholder="Enter full name" required />
        </div>

        <div class="input-box">
          <label>Email Address</label>
          <input type="email" name="email" placeholder="Enter email address" required /> <!-- Updated type to 'email' for better validation -->
        </div>
        <div class="input-box">
            <label>Place Name(to be displayed)</label>
            <input type="text" placeholder="Enter place" required />
          </div>
        <div class="column">
          <div class="input-box">
            <label>Latitude</label>
            <input type="text" name="latitude" placeholder="Enter the latitude" required />
          </div>
          <div class="input-box">
            <label>Longitude</label>
            <input type="text" name="longitude" placeholder="Enter the longitude" required />
          </div>
        </div>
        
        <div class="input-box address">
          <label>Description(text here will be converted to voicenote)</label>
          <textarea name="description" placeholder="Enter more about the place" required style="height: 150px;"></textarea>
        </div>
        <button>Submit</button>
      </form>
    </section>
</body>
</html>

"""
@app.route("/")
def home():
  return render_template('home.html')
  
@app.route("/map")
def map():
  return render_template('version1.html')

@app.route("/about")
def about():
  return render_template('about_us.html')






@app.route('/add', methods=['GET', 'POST'])
def form_submit():
    if request.method == 'POST':
        # Convert form data to dictionary
        form_data = request.form.to_dict()
        # Convert dictionary to JSON string
        
        with open("E:\Project\static\markers.json", 'r') as json_file:
          jdata = json.load(json_file)
        
        try:
            # Load existing JSON data
            with open("E:\Project\static\markers.json", 'r') as json_file:
                jdata = json.load(json_file)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            # If the file is empty or not valid JSON, initialize jdata as an empty dictionary
            jdata = {}



        # Check if the 'users' key exists
        if 'users' in jdata and isinstance(jdata['users'], list):
            # Append new form data to the existing list
            jdata['users'].append(form_data)
        else:
            # Create a new list and store the form data
            jdata['users'] = [form_data]


        with open("E:\Project\static\markers.json", 'w') as marker_file:
            json.dump(jdata, marker_file,indent=2)
        return 'Form submitted and data saved!'
    return render_template_string(HTML_FORM)


if __name__ == '__main__':
    app.run(debug=True)
