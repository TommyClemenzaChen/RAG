# flask

from flask import Flask, request, jsonify
from src.components.rag_functions import get_retriever, query
# from src.logger import logging
# import serverless_wsgi


app = Flask(__name__)

# Initialize the retriever once when the app starts
retriever = get_retriever()

@app.route('/')
def index():
    return {"Hello": "Worlde"}

@app.route('/query', methods=['POST'])
def query_message():
    try:
        data = request.get_json()
        message = data.get('message')
        
        # logging.info(f"Message: {message}")
        response = query(retriever, message)
        # logging.info(f"Response: {response}")
        return jsonify({"response": response}), 200
    except Exception as e:
        # logging.error(f"Error: {e}")
        return jsonify({"error": "Error processing the request"}), 500
    

# def handler(event, context):
#     return serverless_wsgi.handle_request(app, event, context)

if __name__ == '__main__':
    port = 8000
    app.run(port=port, host ='0.0.0.0')
    # app.run(port = port, debug=True)