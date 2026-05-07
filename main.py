from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Redirect server is running!"}

@app.get("/redirect")
def redirect(url: str):
    # agar URL missing hai
    if not url:
        return {"error": "No URL provided."}
    
    # redirect
    return RedirectResponse(url)
