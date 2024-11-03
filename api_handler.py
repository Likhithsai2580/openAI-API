import requests

API_URL = "https://gpt.dzkj.top/api/openai/v1/chat/completions"

def send_non_streaming_request(payload):
    """
    Sends a non-streaming request to the target API and returns the JSON response.
    """
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    return response.json()

def send_streaming_request(payload):
    """
    Sends a streaming request to the target API and yields streaming data.
    """
    with requests.post(API_URL, json=payload, stream=True) as response:
        response.raise_for_status()
        for line in response.iter_lines(chunk_size=1):
            if line:
                # Yield each line as a decoded string
                yield line.decode('utf-8')

if __name__ == "__main__":
    # Example usage of the API handler functions
    # Non-Streaming Example
    print("Non-Streaming Request Example:")
    payload_non_stream = {
        "messages": [{"role": "user", "content": "How many 'r's are there in Strawberry?"}],
        "model": "gpt-4o-mini-2024-07-18",
        "temperature": 0.5,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "top_p": 1,
        "stream": False
    }
    response_non_stream = send_non_streaming_request(payload_non_stream)
    print(response_non_stream)

    # Streaming Example
    print("\nStreaming Request Example:")
    payload_stream = {
        "messages": [{"role": "user", "content": "Write 10 lines on India"}],
        "model": "gpt-4o-mini-2024-07-18",
        "temperature": 0.5,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "top_p": 1,
        "stream": True
    }
    for chunk in send_streaming_request(payload_stream):
        print(chunk)