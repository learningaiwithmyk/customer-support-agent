from fastapi import FastAPI
from app.routes.user_service_route import router as user_request_router

app=FastAPI(title="Customer Support Agent API")

app.include_router(user_request_router,prefix="/csa-api/v1/services", tags=["user_request_service"])

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
