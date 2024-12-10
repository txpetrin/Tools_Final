from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import openai
import os


app = Flask(__name__)
app.debug = True

# Set up SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///responses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# ChatGPT Setup
openai.api_key = os.getenv("OPENAI_API_KEY")

# Retreives answer from ChatGPT
def input_prompt(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant who provides an executive summary of 4-6 bullet points for all prompts."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message["content"]


class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Response {self.id}>'


def create_tables():
    with app.app_context():
        db.create_all()


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        prompt = data.get('text')

        
        response_text = input_prompt(prompt)

        new_response = Response(prompt=prompt, response=response_text)
        db.session.add(new_response)
        db.session.commit()

        return jsonify({'response': response_text})

    responses = Response.query.all()
    return render_template('index.html', responses=responses)

# New route to query all entries in the database
@app.route("/all_entries", methods=['GET'])
def all_entries():
    responses = Response.query.all()

    response_data = [{"id": response.id, "prompt": response.prompt, "response": response.response} for response in responses]
    
    return jsonify(response_data)

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)

