from fastapi import Depends, FastAPI
import uvicorn
from routers import index


app = FastAPI()


app.include_router(index.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
