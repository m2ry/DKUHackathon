from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of item counts
location_options = ["Cali", "Florida"]

# Dictionary of suggestions
suggestions = {
    "Theft": ["Get a door camera", "Get a home security system", "Lock your door and windows", "Purchase blinds and/or curtains"],
    "Fire": ["Buy an new smoke alarm", "Buy a fire extinguisher", "Purchase Kitchen and Laundry Inspection"],
    "Flood": ["Build flood wall around house", "Seal doors and windows", "Install sump pump", "Install backwater valves"],
    "Wild Fire": ["Install clay or metal roof"]
}

# Color hex codes
colors = {
    "background": "#E8F6FF",
    "button": "#094D92",
    "text": "#000000"
}

@app.route('/')
def index():
    return render_template('index.html', location_options=location_options, colors=colors)

@app.route('/generate_checklist', methods=['POST'])
def generate_checklist():
    location = request.form['location']

    # Initialize suggestion list with theft and fire suggestions
    suggestion_list = suggestions["Theft"] + suggestions["Fire"]

    if location == "Cali":
        # Add wild fire suggestions for Cali
        suggestion_list += suggestions["Wild Fire"]
    elif location == "Florida":
        # Add flood suggestions for Florida
        suggestion_list += suggestions["Flood"]

    # Shuffle the suggestion list
    random.shuffle(suggestion_list)

    return render_template('checklist.html', suggestion_list=suggestion_list, colors=colors)

@app.route('/upload_certificate', methods=['POST'])
def upload_certificate():
    suggestion = request.form['suggestion']
    return render_template('success.html', suggestion=suggestion, colors=colors)

if __name__ == '__main__':
    app.run(debug=True)
