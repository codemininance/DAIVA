import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

# Load Vosk model
model_path = "model/vosk-model-small-en-us-0.15"
print("Loading model...")
model = Model(model_path)
rec = KaldiRecognizer(model, 16000)

# Queue to hold audio data
q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

# Start listening
print("🎤 Speak something... (Press Ctrl+C to stop)")
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            if result.get("text"):
                print("You said:", result["text"])
