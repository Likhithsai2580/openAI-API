from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
import api_handler
from models import AVAILABLE_MODELS, ABOUT_INFO

app = FastAPI(
    title="OpenAI API Service",
    description="API service for GPT model interactions",
    version="1.0.0"
)

@app.get("/models")
async def list_models():
    """
    Get the list of available models.
    """
    return JSONResponse(content=AVAILABLE_MODELS)

@app.get("/about")
async def about():
    """
    Get information about the API service.
    """
    return JSONResponse(content=ABOUT_INFO)

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    # Parse the incoming JSON payload
    payload = await request.json()
    
    if payload.get('stream'):
        # Streaming response
        def event_generator():
            for chunk in api_handler.send_streaming_request(payload):
                yield f"{chunk}\n"
        return StreamingResponse(event_generator(), media_type="text/event-stream")
    else:
        # Non-streaming response
        response = api_handler.send_non_streaming_request(payload)
        return JSONResponse(content=response)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)