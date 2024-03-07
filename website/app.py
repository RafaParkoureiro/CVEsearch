from flask import Flask, render_template, request
import pandas as pd
import nvdlib
import basic_search
import ai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_cve', methods=['POST'])
def search():
    cve_id = request.form['cve_id']
    df = basic_search.search(cve_id)
    return render_template('result.html', df=df)

# New route to handle question input
@app.route('/ask_question', methods=['POST'])
def ask_question():
    cve_id = request.form['cve_id']
    question = request.form['question']
    prompt = f"{cve_id},{question}"
    api_key = "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"
    answer = ai.model(prompt, api_key)
    
    # Fetch CVE information again
    df = basic_search.search(cve_id)
    
    return render_template('result.html', df=df, question=question, answer=answer)

# New route to open the advanced search page
@app.route('/advanced_search', methods=['GET', 'POST'])
def advanced_search():

    return render_template('advanced_search.html')  # You would need to create this template

# Add the import statement for advanced_search.py
from advanced_search import returnresponse

# Add a route to render the advanced search page
@app.route('/advanced_search')
def show_advanced_search():
    return render_template('advanced_search.html')

# Add a route to handle the form submission from the advanced search page
@app.route('/advanced_search_results', methods=['POST'])
def advanced_search_results():
    search_query = request.form['search_query']
    results = returnresponse(search_query)
    return render_template('advanced_search_results.html', results=results)

@app.route('/search_cve', methods=['POST'])
def search_cve():
    cve_id = request.form['cve_id']
    df = basic_search.search(cve_id)
    return render_template('result.html', df=df)




if __name__ == '__main__':
    app.run(debug=True)