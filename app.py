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
    '''
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
    '''
    user_message = request.json.get("message")
    
    try:
        # Use the updated completion method and parameters
        response = openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            max_tokens=50,
            temperature=0.7,
        )
        # Extracting the chatbot response from the async response object
        chatbot_message = response["choices"][0]["message"]["content"]
        return jsonify({"response": chatbot_message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    

if __name__=='__main__':
    app.run()

