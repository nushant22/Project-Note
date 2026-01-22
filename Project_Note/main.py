from fastapi import FastAPI
from Project_Note.database.db import engine
from Project_Note.database import models
from Project_Note.routes.note import router as note_router

app = FastAPI(title="Project Note API")

try:
    models.Base.metadata.create_all(bind=engine)
    print("✓ Database tables created/verified")
except Exception as e:
    print(f"⚠️  Could not create tables on startup: {e}")
    print("   This is OK - tables will be created when you first use the app")

app.include_router(note_router)

@app.get("/")
def root():
    return {"message": "FastAPI Note App - Visit /notes/ to manage your notes"}

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    import traceback
    traceback.print_exc()
    return {"error": str(exc)}
