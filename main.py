from fastapi import FastAPI
from pydantic import BaseModel
from app.llm_handler import get_sql_from_question
from app.query_builder import run_sql_query
from app.db import create_database

app = FastAPI()

# ✅ Define a model to describe the input data
class AskRequest(BaseModel):
    question: str

# ✅ Create DB on startup
@app.on_event("startup")
def setup():
    create_database()

# ✅ Modified /ask endpoint with debug print statements
@app.post("/ask")
async def ask_question(request: AskRequest):
    question = request.question
    print(f"✅ Received question: {question}")

    sql = get_sql_from_question(question)
    print(f"🧠 Generated SQL: {sql}")

    result = run_sql_query(sql)
    print(f"📊 Query Result: {result}")

    return {
        "question": question,
        "sql_query": sql,
        "result": result
    }
