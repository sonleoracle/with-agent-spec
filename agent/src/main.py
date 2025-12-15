from ag_ui_agentspec.endpoint import add_agentspec_fastapi_endpoint
from fastapi import FastAPI
import uvicorn

from agent import build_agentspec_agent


def build_server() -> FastAPI:
    app = FastAPI(title="Agent Spec Agent")
    agent = build_agentspec_agent(runtime="langgraph")
    add_agentspec_fastapi_endpoint(app, agent, path="/")
    return app


app = build_server()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
