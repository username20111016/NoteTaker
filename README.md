📝 Notes App

A simple Flask web app to create, organize, and view notes.
Notes are saved into a JSON file so they don’t get deleted when you close the app.

🚀 Features

Add notes by category (e.g. School, Personal, Work)

View previous notes organized by category

Clean Bootstrap UI for better look

Persistent storage using notes.json

Easy to extend (delete notes, edit notes, etc.)

📂 Project Structure
notes-app/
│── app.py             # Flask backend
│── requirements.txt   # Dependencies
│── notes.json         # Notes data (auto-created)
│
└── templates/
    └── index.html     # Frontend template

🛠️ Installation & Running Locally

Clone the repo:

git clone https://github.com/YOUR_USERNAME/notes-app.git
cd notes-app


Install dependencies:

pip install -r requirements.txt


Run the app:

python app.py


Open your browser and go to:

http://127.0.0.1:5000

🖼️ Screenshot

(add one later by taking a screenshot and uploading it to GitHub Issues, then copy the link here)

✨ Future Improvements

Add ability to delete/edit notes

User authentication (private notes)

Deploy online with Render/Heroku
