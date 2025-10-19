from fastapi import FastAPI

app = FastAPI(title="EvogoatML API")

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/")
def root():
    return {"message": "EvogoatML is alive and evolving!"}
