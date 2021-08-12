from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "alo alo 123"

