from fastapi import FastAPI
from api import router



###########################################################################################
#                               Starting FastAPI APP
###########################################################################################

app = FastAPI()
app.include_router(router, prefix="/api")

