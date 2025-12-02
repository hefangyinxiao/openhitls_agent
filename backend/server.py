from typing import TypedDict

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain_core.messages import (
    convert_to_openai_messages,
    message_chunk_to_message, ToolMessage
)

from agent.graph_chat import graph

app = FastAPI(
    title="API for openwebui-pipelines",
    description="API for openwebui-pipelines",
)

@app.post("/openwebui-pipelines/api/stream")
async def stream(inputs:dict):
    async def event_stream():
        # try:
        print(f"\nReceived inputs: {inputs}\n")
        async for event in graph.astream(input=inputs, stream_mode="messages", subgraphs=True, config={"recursion_limit": 100}):
            # print(f"\nReceived event: {event}\n")
            # get first element of tuple
            message = message_chunk_to_message(event[1][0])
            if isinstance(message, ToolMessage):
                if convert_to_openai_messages(message)['content']=='Task completed. No further action required.':
                    yield '</thinking>'
                else:
                    yield '\n🛠️工具调用成功\n'
                continue
            # print(f"\nConverted event: {message}\n")

            yield convert_to_openai_messages(message)['content']
        # except Exception as e:
        #     print(f"An error occurred: {e}")

    return StreamingResponse(event_stream(), media_type="application/json")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)