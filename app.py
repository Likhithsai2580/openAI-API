from flask import Flask, request, Response, jsonify, stream_with_context
import api_handler
from models import AVAILABLE_MODELS, ABOUT_INFO

app = Flask(__name__)

@app.route("/models", methods=['GET'])
def list_models():
    """
    Get the list of available models.
    """
    return jsonify(AVAILABLE_MODELS)

@app.route("/about", methods=['GET'])
def about():
    """
    Get information about the API service.
    """
    return jsonify(ABOUT_INFO)

@app.route("/v1/chat/completions", methods=['POST'])
def chat_completions():
    # Parse the incoming JSON payload
    payload = request.get_json()
    
    if payload.get('stream'):
        # Streaming response
        def event_generator():
            for chunk in api_handler.send_streaming_request(payload):
                yield f"{chunk}\n"
        return Response(
            stream_with_context(event_generator()),
            mimetype="text/event-stream"
        )
    else:
        # Non-streaming response
        response = api_handler.send_non_streaming_request(payload)
        return jsonify(response)

@app.route("/")
def home():
    """
    API Documentation
    """
    return {
        "title": "OpenAI API Service",
        "description": "API service for GPT model interactions",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)