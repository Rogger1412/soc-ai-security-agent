from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import webbrowser
import threading
import logging

from api.routes import router


# ---------------------------
# Logging
# ---------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("SOC-Agent")


# ---------------------------
# FastAPI App
# ---------------------------
app = FastAPI(
    title="SOC AI Security Agent",
    description="AI-driven Security Operations Center assistant",
    version="1.0"
)


# ---------------------------
# CORS
# ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # tighten this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------
# Paths
# ---------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))              # backend/
PROJECT_ROOT = os.path.dirname(BASE_DIR)                          # ai_project/
FRONTEND_PATH = os.path.join(PROJECT_ROOT, "frontend", "index.html")


# ---------------------------
# Serve Frontend
# ---------------------------
@app.get("/")
def home():
    if not os.path.exists(FRONTEND_PATH):
        logger.error(f"Frontend not found at: {FRONTEND_PATH}")
        return JSONResponse(
            status_code=404,
            content={"message": f"Frontend not found at: {FRONTEND_PATH}"}
        )

    return FileResponse(
        FRONTEND_PATH,
        headers={
            "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
            "Pragma": "no-cache",
            "Expires": "0"
        }
    )


# ---------------------------
# Health Check
# ---------------------------
@app.get("/health")
def health():
    return {"status": "ok", "service": "SOC AI Security Agent"}


# ---------------------------
# Include API routes
# ---------------------------
app.include_router(router)


# ---------------------------
# Auto open browser (dev only)
# ---------------------------
def open_browser():
    webbrowser.open("http://127.0.0.1:8000")


# ---------------------------
# Run server
# ---------------------------
if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()

    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )