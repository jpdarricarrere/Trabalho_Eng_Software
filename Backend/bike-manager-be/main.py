from fastapi import FastAPI 

app = FastAPI() 

@app.get("/")
def server_status_index():
    return {"Status": "It lives!"}