import subprocess
import speech_recognition as sr

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command recognized: {command}")
        execute_command(command)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def execute_command(command):
    if "open the youtube" in command:
        open_youtube()
    elif "turn down the volume" in command:
        adjust_volume("down")
    elif "increase the volume" in command:
        adjust_volume("up")
    elif "open the calendar" in command:
        open_application("gnome-calendar")
    elif "open the counter" in command:
        open_application("gnome-calculator")
    elif "open the terminal" in command:
        open_application("gnome-terminal")
    elif "goodbye" in command:
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("Command not recognized")

def open_youtube():
    try:
        subprocess.Popen(["firefox", "https://www.youtube.com"], stderr=subprocess.DEVNULL)
        print("Firefox opened with YouTube successfully")
    except OSError as e:
        print(f"Error opening Firefox: {e}")

def adjust_volume(direction):
    try:
        if direction == "down":
            subprocess.Popen(["amixer", "-D", "pulse", "sset", "Master", "10%-"], stderr=subprocess.DEVNULL)
            print("Volume turned down successfully")
        elif direction == "up":
            subprocess.Popen(["amixer", "-D", "pulse", "sset", "Master", "10%+"], stderr=subprocess.DEVNULL)
            print("Volume turned up successfully")
    except OSError as e:
        print(f"Error adjusting volume: {e}")

def open_application(app_name):
    try:
        subprocess.Popen([app_name], stderr=subprocess.DEVNULL)
        print(f"{app_name} opened successfully")
    except OSError as e:
        print(f"Error opening {app_name}: {e}")

if __name__ == "__main__":
    while True:
        listen_command()

