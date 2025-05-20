"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = [
    # Actividades deportivas existentes...
    {"id": 1, "name": "Fútbol", "type": "deporte", "participants": []},
    {"id": 2, "name": "Básquetbol", "type": "deporte", "participants": []},
    # Nuevas actividades deportivas
    {"id": 3, "name": "Voleibol", "type": "deporte", "participants": []},
    {"id": 4, "name": "Natación", "type": "deporte", "participants": []},
    {"id": 101, "name": "Tenis", "type": "deporte", "participants": []},
    {"id": 102, "name": "Atletismo", "type": "deporte", "participants": []},

    # Actividades artísticas existentes...
    {"id": 5, "name": "Pintura", "type": "artístico", "participants": []},
    {"id": 6, "name": "Teatro", "type": "artístico", "participants": []},
    # Nuevas actividades artísticas
    {"id": 7, "name": "Danza", "type": "artístico", "participants": []},
    {"id": 8, "name": "Música", "type": "artístico", "participants": []},
    {"id": 201, "name": "Fotografía", "type": "artístico", "participants": []},
    {"id": 202, "name": "Escultura", "type": "artístico", "participants": []},

    # Actividades intelectuales existentes...
    {"id": 9, "name": "Ajedrez", "type": "intelectual", "participants": []},
    {"id": 10, "name": "Debate", "type": "intelectual", "participants": []},
    # Nuevas actividades intelectuales
    {"id": 11, "name": "Olimpiada de Matemáticas", "type": "intelectual", "participants": []},
    {"id": 12, "name": "Club de Lectura", "type": "intelectual", "participants": []},
    {"id": 301, "name": "Robótica", "type": "intelectual", "participants": []},
    {"id": 302, "name": "Programación", "type": "intelectual", "participants": []},
]


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specificy activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
