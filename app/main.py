from fastapi import FastAPI

app = FastAPI(title="DevFlow API")

@app.get("/health")
def health():
    return {"status": "ok"}
