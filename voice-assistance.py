
import speech_recognition as sr
import pyttsx3
import sounddevice as sd
import wave
import tempfile
import os

recognizer = sr.Recognizer()
speaker = pyttsx3.init()

speaker.setProperty("rate", 170)
speaker.setProperty("volume", 1.0)


def speak(text):
    print("AI:", text)
    speaker.say(text)
    speaker.runAndWait()


def get_answer(question):
    question = question.lower().strip()

    if "variable" in question:
        return "A variable stores data, for example x equals 10."
    elif "loop" in question:
        return "A loop repeats code. Python has for and while loops."
    elif "function" in question:
        return "A function is reusable code defined using def."
    elif "list" in question:
        return "A list stores multiple items, such as one, two, and three."
    elif "dictionary" in question:
        return "A dictionary stores key-value pairs."
    elif "hello" in question or "hi" in question:
        return "Hello! How can I help you learn Python?"
    elif "your name" in question:
        return "I am your Python voice assistant."
    elif any(word in question.split() for word in ["stop", "exit", "goodbye"]):
        return "Goodbye! Keep learning Python."
    else:
        return "Sorry, I only answer basic Python questions for now."


def listen():
    print("\nListening... Speak now.")

    # Record 5 seconds from your default microphone
    sample_rate = 16000
    recording = sd.rec(
        int(5 * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )
    sd.wait()

    # Save audio temporarily as a WAV file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        filename = f.name

    try:
        with wave.open(filename, "wb") as audio_file:
            audio_file.setnchannels(1)
            audio_file.setsampwidth(2)
            audio_file.setframerate(sample_rate)
            audio_file.writeframes(recording.tobytes())

        with sr.AudioFile(filename) as source:
            audio = recognizer.record(source)

        return recognizer.recognize_google(audio)

    finally:
        if os.path.exists(filename):
            os.remove(filename)


def ai_assistant():
    speak("Hello! I am your Python voice assistant.")

    while True:
        try:
            question = listen()
            print("You:", question)

            answer = get_answer(question)
            speak(answer)

            if any(word in question.lower().split()
                   for word in ["stop", "exit", "goodbye"]):
                break

        except sr.UnknownValueError:
            speak("Sorry, I could not understand you. Please try again.")
        except sr.RequestError:
            speak("Speech recognition failed. Check your internet connection.")
        except KeyboardInterrupt:
            speak("Goodbye!")
            break
        except Exception as error:
            print("Error:", error)
            speak("Something went wrong. Please check the terminal.")


if __name__ == "__main__":
    ai_assistant()