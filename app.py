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
    if request.method == "POST":
        print("POST request received at /api")

    #return render_template("temp.html")
    
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
    

if __name__=='__main__':
    app.run()

