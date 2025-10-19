# DAIVA — Driver’s Artificial Intelligence Voice Assistant

DAIVA (Driver’s Artificial Intelligence Voice Assistant) is a next-generation in-car AI assistant designed to make driving safer, smarter, and more interactive.
It integrates **voice control**, **smart navigation**, **emotion detection**, **driver monitoring**, and **vehicle assistance** into a single, intuitive platform.

---

## Core Features

### 1. OTP-Based Authentication

* Secure onboarding for new users using OTP verification.
* Personalized setup for drivers, ensuring data privacy and security.

###  2. Persistent Memory

* DAIVA remembers user preferences, contacts, home address, phone number, and commonly used commands.
* Stores data locally and securely for offline use.

### 3. Intelligent Map & Navigation

* Displays **real-time nearby petrol pumps, hospitals, restaurants, and emergency services**.
* Uses smart filtering based on urgency and location context.
* Supports **voice-based navigation** and **Google Maps integration**.

### 4. Emotion Recognition

* Analyzes driver’s tone to detect **anger, stress, or sadness**.
* Responds empathetically — calming the driver when angry or engaging positively when happy.

### 5. Wi-Fi & Connectivity

* Auto-detects Wi-Fi or in-car hotspot connectivity.
* Switches between offline and cloud-based mode depending on signal strength.

### 6. Smart Notifications

* Option to **show, hide, or minimize** notifications.
* Provides a discreet driving mode that only shows icons while muting unnecessary alerts.

### 7. App Integrations

* **YouTube** for music and podcasts
* **Google Maps** for live route assistance
* **Phone & Mail** for hands-free communication

---

##  Tech Stack

| Component                | Technology Used                             |
| ------------------------ | ------------------------------------------- |
| **Frontend (App/UI)**    | React.js + TailwindCSS                      |
| **Backend (Core Logic)** | Python (Vosk, Pyttsx3, Dlib, Flask/FastAPI) |
| **Database**             | PostgreSQL (via Vercel Postgres)            |
| **Deployment**           | Vercel                                      |
| **Voice Model**          | Vosk Speech Recognition                     |
| **Authentication**       | OTP + JWT Tokens                            |
| **Emotion Detection**    | Dlib + Audio Emotion Model                  |

---

##  Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/codemininance/DAIVA.git
cd DAIVA
```

### 2️. Create a Virtual Environment

```bash
python -m venv daiva_env
.\daiva_env\Scripts\activate
pip install -r requirements.txt
```

### 3️. Configure Model Path

Download the [Vosk model](https://alphacephei.com/vosk/models) and place it in:

```
/DAIVA/model/vosk-model-small-en-us-0.15
```

### 4️. Run the App

```bash
python daiva_main.py
```

---

##  Deployment (Vercel + Postgres)

1. Push code to GitHub.
2. Connect the repo to [Vercel](https://vercel.com/).
3. Create a **Vercel Postgres** database.
4. Set environment variables (`DATABASE_URL`, `MODEL_PATH`, etc.).
5. Deploy and test live!

---

## Future Enhancements

* Real-time **driver fatigue detection** via camera.
* **Vehicle health monitoring** and predictive maintenance alerts.
* Integration with **IoT devices** and smart car systems.
* Cloud sync across multiple vehicles for a unified profile.

---

## Author

**Mohammed Yousuf Pangal**
Student | Developer | Founder of [CODEMINANCE YouTube Channel](https://www.youtube.com/@CODEMINANCE)

---

## License

MIT License © 2025 Mohammed Yousuf Pangal
