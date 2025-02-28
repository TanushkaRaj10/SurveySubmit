from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from mangum import Mangum  # Required for Vercel
import os

app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, change this to specific domains if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(router)

# Handler for Vercel serverless deployment
handler = Mangum(app)