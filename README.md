# Deaf_Helper — Speech to Text for the Hearing Impaired

> A real-time speech-to-text app that displays spoken words on screen instantly, designed to help hearing-impaired people read what others are saying.

---

## Project Structure

```
deaf_helper_ui/
├── app.py          ← Python Flask server + Speech Recognition
├── index.html      ← UI structure
├── style.css       ← Styling
├── script.js       ← Clock, weather, speech stream
└── requirements.txt
```

---

## Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python** | Core backend language |
| **Flask** | Web server |
| **SpeechRecognition** | Convert speech to text |
| **PyAudio** | Access microphone |
| **Requests** | Fetch weather data |
| **HTML5** | UI structure |
| **CSS3** | Styling and layout |
| **JavaScript** | Clock, date, weather, live stream |
| **Open-Meteo API** | Free weather data (no API key needed) |

---

## How It Works

```
Microphone → Python (SpeechRecognition) → Flask → Browser (Live Display)
```

1. Python listens to the microphone continuously
2. Google Speech Recognition converts audio to text
3. Flask sends the text to the browser via Server-Sent Events
4. The browser displays the text instantly on screen

---

## UI Layout

```
┌─────────────────────────────────────────┐
│ 03:45 PM        ☀ 28 °C                |
│ 19/05/2026                              │
│ ┌                                     ┐ │
│                                         │
│           TEXT APPEARS HERE             │
│                                         │
│ └                                     ┘ │
└─────────────────────────────────────────┘
```

- **Top Left** — Time (hh:mm AM/PM) + Date (DD/MM/YYYY)
- **Top Right** — Weather icon + Temperature
- **Center** — Spoken text displayed in large font
- **Corners** — Bracket decorations

---

## Installation & Setup

### On PC (Windows)

**1. Install dependencies:**
```bash
pip install flask SpeechRecognition requests
pip install pipwin
pipwin install pyaudio
```

**2. Run the app:**
```bash
python app.py
```

**3. Open browser:**
```
http://localhost:5000
```

---

### On Android (Termux)

**1. Create project folder:**
```bash
mkdir -p ~/smartglass
cd ~/smartglass
```

**2. Install dependencies:**
```bash
pip install flask SpeechRecognition requests pyaudio
```

**3. Run the app:**
```bash
python app.py
```

**4. Open browser:**
```
http://localhost:5000
```

---

## Features

- ✅ Supports **Arabic & English** speech
- ✅ Real-time display with **no delay**
- ✅ Live **clock** updates every second
- ✅ **Date** displayed in DD/MM/YYYY format
- ✅ **Weather** auto-updates every 10 minutes
- ✅ No buttons — starts automatically on launch
- ✅ Works **offline** (except weather + speech recognition)
- ✅ Free — **no API key needed**

---

## Requirements

```
flask
SpeechRecognition
pyaudio
requests
```

---

## Developer

**Adham** 
