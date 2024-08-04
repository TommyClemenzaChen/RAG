# flask

from flask import Flask, request, jsonify, render_template
from src.components.rag_functions import get_retriever, query
# from src.logger import logging
# import serverless_wsgi


app = Flask(__name__)

# Initialize the retriever once when the app starts
retriever = get_retriever()

# @app.route('/')
# def index():
#     return {"Hello": "Worlde"}

@app.route('/', methods=['GET', 'POST'])
def query_message():
    if request.method == 'GET':
        return render_template('index.html')
    
    #PUT
    try:
        data = request.get_json()
        message = data.get('msg')
        
        response = query(retriever, message)
        # logging.info(f"Got response")
        return jsonify({"response": response}), 200
    except Exception as e:
        # logging.info(f"Error: {e}")
        return jsonify({"error": "Error processing the request"})
    
    
    

# def handler(event, context):
#     return serverless_wsgi.handle_request(app, event, context)

if __name__ == '__main__':
    port = 8000
    app.run(port=port, host ='0.0.0.0', debug = True)
    # app.run(port = port, debug=True)