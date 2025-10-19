import sounddevice as sd
import vosk
import queue
import json

MODEL_PATH = r"C:/Users/LENOVO/Desktop/DAIVA/vosk-model-small-en-us-0.15"
model = vosk.Model(MODEL_PATH)

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

with sd.RawInputStream(samplerate=16000, blocksize = 8000, dtype='int16',
                       channels=1, callback=callback):
    rec = vosk.KaldiRecognizer(model, 16000)
    print("🎧 DAIVA is listening... Say 'DAIVA' to wake her up.")
    
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "")
            if "daiva" in text.lower():
                print("DAIVA woke up!")
                break
