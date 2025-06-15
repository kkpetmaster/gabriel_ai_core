from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CommandInput(BaseModel):
    command: str

@app.get("/interface/ping")
def ping():
    return {"message": "AIIN Gabriel Interface OK", "status": 200}

@app.post("/interface/dispatch")
def dispatch_command(input_data: CommandInput):
    if input_data.command == "launch:sigma":
        return {"result": "Command dispatched: launch:sigma"}
    return {"result": f"Command received: {input_data.command}"}
