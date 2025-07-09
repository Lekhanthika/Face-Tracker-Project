📌 Project Overview

This project is an **Intelligent Face Tracker** that uses real-time face detection and recognition to automatically register new visitors and count unique entries. The system detects faces from a live video stream or file, compares them with previously seen faces using embeddings, and logs the appearance of new individuals.

🚀 Features

* 🔍 Real-time face detection using **YOLOv8**
* 🧠 Face recognition using **InsightFace embeddings**
* 🆕 Auto-registration of new visitors (no manual input required)
* 🧾 Cropped face images saved locally with timestamps
* 🧮 Total visitor counter
* 📋 Logs stored with frame information and recognition status
* 💾 Optionally logs events into an SQLite database (face_tracker.db)

🛠️ Tech Stack

**Programming Language**: Python
**Face Detection**: YOLOv8 via Ultralytics
**Face Recognition**: InsightFace
**Video Processing**: OpenCV
**Data Storage**: JSON + SQLite

 📂 Project Structure

├── main.py                # Main tracking script
├── config.json            # Configuration settings
├── cropped_faces/         # Saved cropped face images
├── face_tracker.db        # SQLite DB for event logs (optional)
├── README.md              # Project documentation


🧪 Installation & Setup


# Clone the repository
https://github.com/Lekhanthika/Face-Tracker-Project.git
cd Face-Tracker-Project

# (Optional) Create a virtual environment
python3 -m venv faceenv
source faceenv/bin/activate  # macOS/Linux
faceenv\Scripts\activate    # Windows

# Install requirements
pip install -r requirements.txt

# Download YOLOv8 weights if not present (optional)
# Download InsightFace models on first run (auto)

# Run the application
python main.py


📸 How It Works

1. The script captures video frames.
2. Faces are detected using YOLOv8.
3. Face embeddings are computed using InsightFace.
4. If a face is new (not in memory), it's registered:

   * Saved to cropped_faces/
   * Logged as a new visitor
   * Assigned a visitor ID
5. If recognized, it's marked as "known visitor."

 📹 Demo Video

[🔗 Watch the Demo] https://www.loom.com/share/ee76c5476f6d45c5a6aeb8c8b4561afb?sid=563c74d7-745b-4fe0-8671-bec268e4b7af

 📈 Sample Output

⬆️ Frame 0, Face 0: New visitor registered (Total: 1)
⬆️ Frame 0, Face 1: New visitor registered (Total: 2)
➰ Frame 5, Face 0: Known visitor
⚠️ Frame 60: No faces detected.


 🙌 Credits

* [InsightFace](https://github.com/deepinsight/insightface)
* [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* OpenCV

 📬 Submission

* GitHub Repo: [https://github.com/Lekhanthika/Face-Tracker-Project](https://github.com/Lekhanthika/Face-Tracker-Project)
* Demo Video: https://www.loom.com/share/ee76c5476f6d45c5a6aeb8c8b4561afb?sid=563c74d7-745b-4fe0-8671-bec268e4b7af

---
“This project is a part of a hackathon run by https://katomaran.com”
For any assistance or customization, feel free to reach out!