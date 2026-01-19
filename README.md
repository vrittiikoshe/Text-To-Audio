# 🎧 Text to Audiobook

Text to Audiobook is a dynamic web application that converts written text into natural-sounding audio using text-to-speech technology.  
The project features a clean landing page, an intuitive text-to-audio converter, and real-time audio playback controls.

---

## 🚀 Features

- Convert text into audio instantly
- Dedicated start (landing) page
- Audio playback controls:
  - Play
  - Pause
  - Resume
  - Stop
- Adjustable playback speed using a slider
- Clean and modern user interface
- Dynamic audio generation on the server side

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Text-to-Speech:** gTTS (Google Text-to-Speech)  
- **Server:** Gunicorn (for deployment)

---

## 📂 Project Structure

PythonProject/
│── app.py
│── Procfile
│── requirements.txt
│── project.json
│
│── templates/
│ ├── start.html
│ └── index.html
│
│── static/
│ ├── css/
│ │ ├── start.css
│ │ └── style.css
│ └── audio/

---

## ▶️ How to Run Locally

1. Clone the repository or download the files
2. Navigate to the project directory
3. Create and activate a virtual environment (optional but recommended)
4. Install dependencies:

```bash
pip install -r requirements.txt
Run the application:
python app.py
Open your browser and visit:
http://127.0.0.1:5001

🌐 Deployment
- This project is deployment-ready and can be hosted on platforms like Render using Gunicorn.
- Deployment files included:
- Procfile
- requirements.txt

💡 Use Cases
- Listening to study notes
- Multitasking while consuming text content
- Accessibility support
- Converting scripts or written content into audio
audio

📌 Future Enhancements
- Support for multiple languages
- Audio download option
- User authentication
- Audio history management

👩‍💻 Author
Developed by Vritti Koshe

📄 License
This project is licensed under the MIT License.
