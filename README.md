# Project Note - Note Management System

A modern, full-stack note management application built with **FastAPI** and **MySQL**, featuring a responsive web interface for creating, reading, updating, and deleting notes with advanced search and categorization capabilities.

## Features

✨ **Core Features:**
- 📝 **Create Notes** - Add new notes with title, content, and category
- 📖 **View All Notes** - Display all notes in a clean card-based layout
- ✏️ **Edit Notes** - Update note content, title, and category
- 🗑️ **Delete Notes** - Remove notes permanently
- 🔍 **Search Functionality** - Search notes by title or content
- 🏷️ **Categorization** - Organize notes by categories
- ⏰ **Timestamps** - Automatic creation and modification timestamps
- 🌐 **REST API** - Full-featured API endpoints for programmatic access
- 📱 **Responsive UI** - Modern, gradient-styled web interface

## Tech Stack

### Backend
- **Framework:** FastAPI (Python web framework)
- **Database:** MySQL 8.0.44
- **ORM:** SQLAlchemy 2.0.46
- **Database Driver:** PyMySQL
- **Template Engine:** Jinja2
- **Environment Management:** python-dotenv

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients
- **JavaScript** - Interactive functionality

### Python Version
- Python 3.14+

## Project Structure

```
Project-Note/
├── Project_Note/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── config/
│   │   ├── __init__.py
│   │   └── db.py              # Database configuration (legacy)
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db.py              # Database connection and session setup
│   │   └── models.py          # SQLAlchemy ORM models
│   ├── models/
│   │   ├── __init__.py
│   │   └── note.py            # Note data models
│   ├── routes/
│   │   ├── __init__.py
│   │   └── note.py            # API and web routes
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── note.py            # Pydantic schemas for validation
│   └── templates/
│       ├── index.html         # Main notes display page
│       └── edit.html          # Edit note page
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (not in repo)
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## Installation

### Prerequisites
- Python 3.14+
- MySQL 8.0+ (running and accessible)
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/nushant22/Project-Note.git
cd Project-Note
```

### Step 2: Create Virtual Environment
```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file in the project root with the following variables:

```env
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password_here
DB_NAME=project_note
```

**Note:** Make sure MySQL is running and the database `project_note` exists.

### Step 5: Run the Application
```bash
python -m uvicorn Project_Note.main:app --reload
```

The application will be available at: **http://127.0.0.1:8000**

## Usage

### Web Interface

#### Create a Note
1. Navigate to http://127.0.0.1:8000/notes/
2. Fill in the form with:
   - **Title:** Note title
   - **Content:** Note content
   - **Category:** Select or type a category
3. Click **"Add Note"**

#### View Notes
- All notes are displayed as cards on the main page
- Each card shows: Title, Content Preview, Category, Creation Date, and Actions

#### Search Notes
- Use the search bar at the top to find notes by title or content
- Results update in real-time

#### Filter by Category
- Select a category from the dropdown to filter notes
- Select "All Categories" to view all notes

#### Edit a Note
1. Click the **"Edit"** button on any note card
2. Update the note details
3. Click **"Update Note"**

#### Delete a Note
- Click the **"Delete"** button on any note card
- The note will be permanently removed

### REST API Endpoints

#### Base URL
```
http://127.0.0.1:8000/notes
```

#### GET Endpoints

**Get All Notes**
```
GET /api/all
```
Response:
```json
[
  {
    "id": 1,
    "title": "My First Note",
    "content": "Note content here...",
    "category": "Personal",
    "created_at": "2026-01-22T10:30:00",
    "updated_at": "2026-01-22T10:30:00"
  }
]
```

**Get Note by ID**
```
GET /api/{id}
```
Example: `GET /api/1`

**Search Notes**
```
GET /api/search?query=search_term
```
Example: `GET /api/search?query=python`

#### POST Endpoints

**Create Note**
```
POST /api/create
Content-Type: application/json

{
  "title": "New Note",
  "content": "Note content",
  "category": "Work"
}
```

#### PUT Endpoints

**Update Note**
```
PUT /api/update/{id}
Content-Type: application/json

{
  "title": "Updated Title",
  "content": "Updated content",
  "category": "Updated Category"
}
```

#### DELETE Endpoints

**Delete Note**
```
DELETE /api/delete/{id}
```
Example: `DELETE /api/delete/1`

## Database Schema

### Notes Table
```sql
CREATE TABLE note (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  content LONGTEXT NOT NULL,
  category VARCHAR(100),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

## Configuration Details

### Database Connection
- **Host:** 127.0.0.1 (localhost)
- **Port:** 3306 (default MySQL port)
- **Driver:** PyMySQL
- **Connection String:** `mysql+pymysql://user:password@host:port/database`

### Important Notes
- The password is URL-encoded in the connection string (special characters like `@` are encoded as `%40`)
- Connection pooling is enabled with `pool_pre_ping=True` to maintain connection health
- Tables are automatically created on application startup if they don't exist

## Error Handling

The application includes comprehensive error handling:
- Database connection errors are caught and logged
- Invalid input data is validated using Pydantic schemas
- HTTP exceptions are properly formatted with status codes
- Missing resources return 404 responses
- Internal errors return 500 responses with error details

## Development

### Running in Development Mode
```bash
python -m uvicorn Project_Note.main:app --reload
```
The `--reload` flag enables auto-restart on file changes.

### Running in Production Mode
```bash
python -m uvicorn Project_Note.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Testing the API
Use tools like:
- **Postman** - GUI API client
- **curl** - Command-line HTTP client
- **Python requests** - Programmatic testing

Example with curl:
```bash
curl -X GET http://127.0.0.1:8000/notes/api/all
curl -X POST http://127.0.0.1:8000/notes/api/create \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","content":"Test content","category":"Test"}'
```

## Future Enhancements

- 🔐 User authentication and authorization
- 📧 Email notifications
- 🏷️ Tags in addition to categories
- 📎 File attachments
- 🎨 Note color coding
- 📱 Mobile app
- 🔄 Real-time collaboration
- 📊 Notes statistics and analytics
- 🌙 Dark mode UI
- 🔔 Reminders and notifications

## Troubleshooting

### Database Connection Issues
**Problem:** `Can't connect to MySQL server`
- **Solution:** Ensure MySQL is running and credentials in `.env` are correct

### Port Already in Use
**Problem:** `Address already in use`
- **Solution:** Change the port: `python -m uvicorn Project_Note.main:app --port 8001`

### Import Errors
**Problem:** `ModuleNotFoundError`
- **Solution:** Ensure virtual environment is activated and dependencies are installed

### CORS Issues
**Problem:** Cross-origin requests fail
- **Solution:** Configure CORS in `main.py` if needed

## License

This project is open source and available for personal and educational use.

## Author

Created by **nushant22** (Nushant Ghimire)

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository:
https://github.com/nushant22/Project-Note/issues

## Contributors

Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

**Last Updated:** January 22, 2026  
**Version:** 1.0.0
