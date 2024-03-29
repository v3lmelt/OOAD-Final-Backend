import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from starlette.middleware.cors import CORSMiddleware

from Service import accountService, fileUploadService, dishService, dishDistributionService, cashService, \
    statisticService

app = FastAPI()
add_pagination(app)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(accountService.router)
app.include_router(fileUploadService.router)
app.include_router(dishService.router)
app.include_router(dishDistributionService.router)
app.include_router(cashService.router)
app.include_router(statisticService.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload=True)
