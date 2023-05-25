from flask import Flask, request,  render_template
import wikipedia

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Question.html')

@app.route('/answer', methods=['POST'])
def get_answer():
    # Get the user's question from the HTML form
    question = request.form['question']
    
    # Use the Wikipedia API to search for the answer
    try:
        answer = wikipedia.summary(question)
    except wikipedia.exceptions.PageError:
        # If no page is found, return an error message
        answer = "Sorry, I couldn't find an answer to that question."
    
    # Return the answer to the HTML template
    return render_template('answer.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)