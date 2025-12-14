from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="GuardianX Backend",
    description="Fact verification backend service",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Allow all origins (OK for dev)
    allow_credentials=True,
    allow_methods=["*"],        # Allow all HTTP methods
    allow_headers=["*"],        # Allow all headers
)

# Import routers AFTER app creation
from app.api.ingest import router as ingest_router
from app.api.verify import router as verify_router

# Register routers
app.include_router(ingest_router)
app.include_router(verify_router)

# Health check
@app.get("/", tags=["Health"])
def root():
    return {"message": "GuardianX backend is running"}
