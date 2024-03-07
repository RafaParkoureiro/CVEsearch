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
    api_key = '56d9404c-f27a-453b-9065-d340bed0562f'
    df = basic_search.search(cve_id)
    
    return render_template('result.html', df=df, question=question, answer=answer)


if __name__ == '__main__':
    app.run(debug=True)