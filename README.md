# Smart-CLI-File-Organiser
📁 Smart File Organizer (CLI)

A Python-powered command-line file organizer that helps you keep your directories clean by automatically sorting files into categorized folders such as Documents, Images, Videos, Music, Archives, and more.


---

🚀 Features

📂 Organizes files by extension

🧠 Smart category detection (Images, Docs, Media, etc.)

⚡ Fast and lightweight CLI tool

🛠 Customizable folder rules

🔁 Handles duplicate files safely

🧪 Dry-run mode (preview changes before applying)

🖥 Works on Windows, macOS, and Linux



---

🛠 Tech Stack

Language: Python 3

Libraries: os, shutil, argparse, pathlib



---

📦 Installation

git clone

cd smart-file-organizer
python organizer.py --help


---

▶ Usage

python organizer.py /path/to/directory

With options:

python organizer.py /path/to/directory --dry-run


---

🧠 How It Works

The tool scans the given directory, detects file extensions, maps them to predefined categories, and moves them into corresponding folders automatically.

Example:

photo.jpg   → Images/
resume.pdf  → Documents/
song.mp3    → Music/
video.mp4   → Videos/


---

📁 Folder Structure

smart-file-organizer/
│
├── organizer.py
├── rules.py
├── README.md
└── requirements.txt


---

🔧 Custom Rules

You can easily add your own file categories inside rules.py:

FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
}


---

📌 Future Improvements

🔍 AI-based file classification

🗂 Date-based organization

🧾 Logging & undo feature

📦 PyPI package release



---

🤝 Contributing

Pull requests are welcome! Feel free to open an issue or suggest improvements.
