from fastapi import FastAPI
from app.routes.user_service_route import router as user_request_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os


app=FastAPI(title="Customer Support Agent API")

app.include_router(user_request_router,prefix="/csa-api/v1/services", tags=["user_request_service"])

app.mount("/static",StaticFiles(directory="front-end/static"),name="static")

@app.get("/")
async def serve_index():
    return FileResponse(os.path.join("front-end","index.html"))

app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"],)


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
