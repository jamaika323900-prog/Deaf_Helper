import speech_recognition as sr
import threading
import queue
import json
import requests
from flask import Flask, Response, jsonify

app = Flask(__name__)

text_queue = queue.Queue()
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.5


def listen_loop():
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        text_queue.put({"type": "status", "text": "listening"})
        while True:
            try:
                audio = recognizer.listen(source, timeout=1, phrase_time_limit=10)
                text_queue.put({"type": "status", "text": "processing"})
                try:
                    result = recognizer.recognize_google(audio, language="ar-EG,en-US")
                    text_queue.put({"type": "transcript", "text": result})
                    text_queue.put({"type": "status", "text": "listening"})
                except sr.UnknownValueError:
                    text_queue.put({"type": "status", "text": "listening"})
                except sr.RequestError:
                    text_queue.put({"type": "error"})
            except sr.WaitTimeoutError:
                pass
            except Exception:
                pass


@app.route("/")
def index():
    with open("index.html", encoding="utf-8") as f:
        return f.read(), 200, {"Content-Type": "text/html"}


@app.route("/style.css")
def css():
    with open("style.css", encoding="utf-8") as f:
        return f.read(), 200, {"Content-Type": "text/css"}


@app.route("/script.js")
def js():
    with open("script.js", encoding="utf-8") as f:
        return f.read(), 200, {"Content-Type": "application/javascript"}


@app.route("/weather")
def weather():
    try:
        loc = requests.get("https://ipapi.co/json/", timeout=5).json()
        lat = loc.get("latitude", 30.0)
        lon = loc.get("longitude", 31.0)
        res = requests.get(
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current_weather=true",
            timeout=5
        ).json()
        temp = res["current_weather"]["temperature"]
        return jsonify({"temp": temp})
    except Exception:
        return jsonify({"temp": "--"})


@app.route("/stream")
def stream():
    def event_gen():
        while True:
            try:
                data = text_queue.get(timeout=30)
                yield f"data: {json.dumps(data)}\n\n"
            except queue.Empty:
                yield 'data: {"type":"ping"}\n\n'
    return Response(event_gen(), mimetype="text/event-stream",
                    headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})


if __name__ == "__main__":
    threading.Thread(target=listen_loop, daemon=True).start()
    print("SmartGlass running → http://localhost:5000")
    app.run(debug=False, threaded=True)
