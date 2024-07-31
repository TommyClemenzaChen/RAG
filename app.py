# flask

from flask import Flask, render_template, request, jsonify
from src.components.rag_functions import get_retriever, query
from src.logger import logging

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
        
        logging.info("Message: ", message)
        response = query(retriever, message)
        logging.info("Response: ", response)
        return jsonify({"response": response})
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"error": "Error processing the request"})
    



if __name__ == '__main__':
    port = 8000
    app.run(port=port, debug=True)