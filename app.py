from flask import Flask, render_template, request
import openai


app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'


# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    
    '''
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    '''
    return "I am GOOD!!!!! "
    

if __name__=='__main__':
    app.run()
