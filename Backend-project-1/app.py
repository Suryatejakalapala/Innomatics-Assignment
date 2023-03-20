from flask import Flask , render_template , request
import re

app = Flask(__name__)  

# Creating a route for the home page
@app.route('/' , methods = ['GET' , 'POST'])
def Home_page():
    # If the request method is POST (i.e. the user submitted the form)
    if request.method == 'POST':
        # Get the test string and regex pattern from the form data
        test_string = request.form['test_string']
        regex = request.form['regex']
        
        # Find all matches of the regex pattern in the test string
        matches = re.findall(regex, test_string)
        
        # Render the index.html template and pass in our variables
        return render_template('index.html', matches=matches, test_string=test_string, regex=regex)
    
    # If the request method is GET (i.e. the user is loading the page for the first time)
    return render_template('index.html')

if __name__ ==  '__main__':
    app.run(debug='True')