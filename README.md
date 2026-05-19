# hw-tracker-web

A full stack homework tracking web app built with Python, Flask, and vanilla JavaScript.

## Features
- Add assignments with course name, assignment name, and due date
- Mark assignments as complete or incomplete
- Delete assignments
- Data persists between sessions via a JSON file

## Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Storage:** JSON file

## Getting Started

### Prerequisites
- Python 3
- Flask

### Installation
git clone https://github.com/yourusername/hw-tracker-web
cd hw-tracker-web
pip install flask
python app.py

Project Structure
hw-tracker-web/
├── app.py              # Flask backend and API routes
├── assignments.json    # Persistent data storage
└── templates/
    └── index.html      # Frontend UI

Background
This project started as a C++ CLI app — check out the original at
home-work-tracker.
The web version was built to learn Python and full stack development.