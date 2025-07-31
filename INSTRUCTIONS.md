# 📘 How to Use Jarvis AI Assistant

Follow this guide to interact with and control your personal Jarvis Assistant using voice commands.

---

## 🚀 Step-by-Step Instructions

### 🔹 1. Start the Assistant

Open your terminal and run:

```bash
python ui.py
```

This will launch the **Jarvis GUI**.

---

### 🔹 2. Wait for Greeting

You’ll hear:
```
Hey <your name>, Jarvis here. What can I do for you?
```

Jarvis will now start listening in the background.

---

### 🔹 3. Say the Wake Word

To trigger Jarvis, say:
```
Jarvis
```

When Jarvis hears this, it will activate and respond to your command.

---

## 🎤 Example Voice Commands

| Category        | Example Command                      | What Happens                                       |
|----------------|--------------------------------------|---------------------------------------------------|
| Music          | "Jarvis play Believer"               | Opens Spotify and searches for *Believer*         |
| Time           | "What time is it?"                   | Tells current time                                |
| Joke           | "Tell me a joke"                     | Says a random joke                                |
| YouTube        | "Open YouTube"                       | Launches YouTube in your browser                  |
| Calculator     | "Open calculator"                    | Opens system calculator                           |
| Wikipedia      | "Search Alan Turing on Wikipedia"    | Reads a short Wikipedia summary                   |
| Google Search  | "Search AI tools on Google"          | Opens Google with your query                      |
| System         | "Shutdown computer"                  | Initiates system shutdown                         |
| Personalization| "Change my name"                     | Saves new user name                               |
| Exit           | "Jarvis stop" or "Exit"              | Gracefully shuts down the assistant               |

---

## 🧠 Assistant Behavior

- 🔄 Jarvis **always listens** after startup unless you stop it.
- 🤖 Jarvis responds using speech and displays logs in the GUI.
- 🧠 Jarvis remembers your name between sessions (saved in `data/user.txt`).
- 🎧 Each listening session is preceded by a *beep sound* (`resources/beep.mp3`).

---

## 🛠️ Troubleshooting

| Problem                          | Fix                                                                 |
|----------------------------------|----------------------------------------------------------------------|
| Assistant doesn’t hear me       | Check microphone permission and speak clearly after the beep        |
| "beep.mp3 not found" error      | Make sure `resources/beep.mp3` exists or comment out that line      |
| GUI closes unexpectedly         | Check for Python errors in terminal (often due to internet or audio)|
| Assistant keeps saying "didn’t catch that" | Try increasing volume or reducing background noise         |

---

## 🛑 To Stop the Assistant

Say:
```
Jarvis stop
```
Or click the `X` on the GUI window to exit manually.

---

## ❤️ Tips

- Use a **headset mic** for better accuracy
- Pause **briefly after the wake word** ("Jarvis ... play music")
- Keep background noise low
- Don’t say full sentences like "Can you please..." — just say: `"Play music"` or `"Tell me the time"`
