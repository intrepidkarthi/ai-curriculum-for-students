from fastapi import FastAPI, HTTPException

app = FastAPI(title="Session 03 API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/sum")
def sum_endpoint(a: int | None = None, b: int | None = None):
    if a is None or b is None:
        raise HTTPException(status_code=422, detail="Missing query params 'a' and 'b'")
    return {"sum": a + b}


@app.get("/")
def root():
    return {"message": "Welcome to Session 03 API. Try /health or /sum?a=1&b=2"}
