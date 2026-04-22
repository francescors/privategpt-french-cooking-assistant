#pip install openai==0.28, tiktoken

from flask import Flask, render_template, request, flash, redirect, url_for
from openai import OpenAI
import json
import markdown
import re

OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

client = OpenAI(api_key=OPENAI_API_KEY)

assistant = "asst_ZEVFqoZ8UFxMabZYTkFzJBLY"
current_chat = 0


###################################################################################################################################################

app = Flask(__name__)

@app.route("/")
def hello():
    #return "<p>Hello, World!</p>"
    return render_template('index.html')

@app.route("/", methods=['POST'])
def hello_post():
    return "<p>Hello, World!</p>"


@app.route("/newchat", methods=['POST'])
def newchat():
    global current_chat
    thread = client.beta.threads.create()
    current_chat = thread.id 
    return ""
    

@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json()
    print(data)
    global current_chat
    
    if(current_chat == 0):
        thread = client.beta.threads.create()
        current_chat = thread.id   
    
    
    text = data['prompt']
    
    message = client.beta.threads.messages.create(
    thread_id = current_chat,
    role="user",
    content=text,
    )

    run = client.beta.threads.runs.create_and_poll(
    thread_id = current_chat,
    assistant_id = assistant,
    )
    result =""
    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(thread_id = current_chat, order= 'desc',limit = 1)
        str_messages = str(messages)
        print(str_messages)
        result = re.search(r"value=\'(.*?)\'\)\, type", str_messages)
        if result is None:
            result = re.search(r"value=\"(.*?)\"\)\, type", str_messages)
        result = result.group(1)
        result = result.replace("\\n", "\n")
        result = result.replace("\\t", "\t")
        print(message)
    
    return {'answer': markdown.markdown(result)}

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'source_documents'
    app.run(port=4000, host='0.0.0.0', debug=True)
