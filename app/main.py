import uvicorn
from os import getenv

if __name__ == "__main__":
    port = int(getenv("PORT", 8000))
    uvicorn.run("api.app:app", host="127.0.0.1", port=port, reload=True)