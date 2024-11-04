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

