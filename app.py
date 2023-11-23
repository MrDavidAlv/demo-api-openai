# app.py

from flask import Flask, render_template, request
from openai import OpenAI

client = OpenAI(api_key='YOUR-API-KEY-OPENAI')

app = Flask(__name__) 



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    prompt = request.form['prompt']
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}])
    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    app.run(debug=True)
