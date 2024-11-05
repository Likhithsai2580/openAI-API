# OpenAI API Service

## Description
This project provides an API service for interacting with GPT models. It uses FastAPI for handling API requests and includes both non-streaming and streaming endpoints.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SreejanPersonal/openAI-API.git
    cd openAI-API
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### List Models
- **URL:** `/models`
- **Method:** `GET`
- **Description:** Get the list of available models.

### About
- **URL:** `/about`
- **Method:** `GET`
- **Description:** Get information about the API service.

### Chat Completions
- **URL:** `/v1/chat/completions`
- **Method:** `POST`
- **Description:** Send a request to the API for chat completions.
- **Request Body:**
    ```json
    {
        "messages": [{"role": "user", "content": "Your message here"}],
        "model": "model-id",
        "temperature": 0.5,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "top_p": 1,
        "stream": false
    }
    ```
- **Response:** JSON object with the chat completion result.
