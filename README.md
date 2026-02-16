# 📝 QuickNote-App - Task Management Application

A clean, responsive web-based note-taking and task management application built with vanilla HTML, CSS, JavaScript in the frontend, FastAPI used as backend framework and MySQL as database.

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## 🎯 About

A modern, full-stack note management application built with **FastAPI** and **MySQL**, featuring a responsive web interface for creating, reading, updating, and deleting notes with advanced search and categorization capabilities.


## ✨ Features

✨ **Core Features:**
- 📝 **Create Notes** - Add new notes with title, content, and category
- 📖 **View All Notes** - Display all notes in a clean card-based layout
- ✏️ **Edit Notes** - Update note content, title, and category
- 🗑️ **Delete Notes** - Remove notes permanently
- 🌐 **REST API** - Full-featured API endpoints for programmatic access


## 🛠️ Technologies Used

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

## 🚀 Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Basic understanding of HTML/CSS/JS (for modifications)

## Installation

### Prerequisites
- Python 3.14+
- MySQL 8.0+ (running and accessible)
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/nushant22/QuickNote-App.git
cd QuickNote-App
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
DB_NAME=QuickNote_App
```

**Note:** Make sure MySQL is running and the database `QuickNote_App` exists.

### Step 5: Run the Application
```bash
python -m uvicorn QuickNote_App.main:app --reload
```

The application will be available at: **http://127.0.0.1:8000**

## 📂 Project Structure

```
QuickNote-App/
Project_Note/
├── database/
│   ├── __init__.py
│   ├── db.py
│   └── models.py
├── routes/
│   ├── __init__.py
│   └── note.py
├── schemas/
│   ├── __init__.py
│   └── note.py
├── templates/
│   ├── edit.html
│   └── index.html
├── __init__.py
├── main.py
├── README.md
└── requirements.txt

```

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

#### Edit a Note
1. Click the **"Edit"** button on any note card
2. Update the note details
3. Click **"Update Note"**

#### Delete a Note
- Click the **"Delete"** button on any note card
- The note will be permanently removed

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
python -m uvicorn QuickNote_App.main:app --reload
```
The `--reload` flag enables auto-restart on file changes.

### Running in Production Mode
```bash
python -m uvicorn QuickNote_App.main:app --host 0.0.0.0 --port 8000 --workers 4
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
- **Solution:** Change the port: `python -m uvicorn QuickNote_App.main:app --port 8001`

### Import Errors
**Problem:** `ModuleNotFoundError`
- **Solution:** Ensure virtual environment is activated and dependencies are installed

### CORS Issues
**Problem:** Cross-origin requests fail
- **Solution:** Configure CORS in `main.py` if needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Design inspiration from [Google Keep](https://keep.google.com/)
- Icons from [FontAwesome](https://fontawesome.com/)
- Color palette from [Coolors](https://coolors.co/)

## 📧 Contact

**Nushant Ghimire**

- LinkedIn: [nushant-ghimire-861b87325](https://www.linkedin.com/in/nushant-ghimire-861b87325/)
- GitHub: [@nushant22](https://github.com/nushant22)
- Email: [nushantghimire22@gmail.com]

---

⭐ **If you find this project useful, please give it a star!**

💡 **Have suggestions?** [Open an issue](https://github.com/nushant22/QuickNote-App/issues)

*Last Updated: February 2026*
