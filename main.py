from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routers.__init__

app = FastAPI()

app.include_router(
    routers.__init__.router_imap,
    prefix="/api",                
    tags=["IMap API"],
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
