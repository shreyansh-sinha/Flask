from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def hello_shreya():
	var_name = "Shreya"
	return render_template('about.html', html_name = var_name)

app.run(debug=True)