# Keylogger Project

## Overview

This project is a basic keylogger program developed as part of my internship at SkillCraft Technology. The keylogger records and logs keystrokes, providing insights into keyboard activity for educational and ethical purposes.

## Features

- Captures and logs keystrokes.
- Saves logged keystrokes to a file for later analysis.
- Utilizes event-driven programming to respond to keyboard events.
- Implements error handling for robustness.

## Requirements

- Python 3.13 or higher
- `pyinput` library
- `pywin32` library

### Install Required Libraries

You can install the necessary libraries using pip:

```bash
pip install pyinput pywin32
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/keylogger.git
   ```

2. Navigate to the project directory:

   ```bash
   cd keylogger
   ```

3. Run the keylogger:

   ```bash
   python keylogger.py
   ```

4. The keylogger will start capturing keystrokes and save them to a file named `keylog.txt`.

## Key Learnings

- **Event-Driven Programming:** Understanding how to capture and respond to keyboard events.
- **Keystroke Logging:** Implementing a mechanism to record and log keystrokes.
- **File Input/Output:** Saving logged keystrokes to a file for later analysis.
- **Multithreading or Async Programming:** Utilizing concurrent programming techniques to run the keylogger in the background.
- **Error Handling:** Managing potential errors that may occur during keystroke logging or file operations.
- **Platform-Specific APIs:** Familiarizing myself with platform-specific APIs or libraries for keyboard event handling.

## Ethical Considerations

This keylogger is intended for educational purposes only. Please ensure you have permission to log keystrokes on any system where you deploy this software. Misuse of keyloggers can lead to legal consequences.
