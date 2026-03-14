from fastapi import APIRouter
from pydantic import BaseModel
from agent.Security_agent import handle_query
from utils.logger import logger
from database.db import cursor
router = APIRouter()


# ------------------------
# Request model
# ------------------------
class ChatRequest(BaseModel):
    message: str


# ------------------------
# Chat endpoint
# ------------------------
@router.post("/chat")
def chat(req: ChatRequest):
    try:
        logger.info(f"User query: {req.message}")

        result = handle_query(req.message)

        if isinstance(result, dict) and "message" in result:
            return {"message": result["message"]}

        return {"message": str(result)}

    except Exception as e:
        logger.exception("Agent error")
        return {"message": f"Internal error: {str(e)}"}
        
@router.get("/investigations")
def get_investigations():

    cursor.execute("""
    SELECT id,timestamp,target,intent,severity,score
    FROM investigations
    ORDER BY id DESC
    LIMIT 20
    """)

    rows = cursor.fetchall()

    results = []

    for r in rows:
        results.append({
            "id": r[0],
            "timestamp": r[1],
            "target": r[2],
            "intent": r[3],
            "severity": r[4],
            "score": r[5]
        })

    return results