import keyboard

def send_to_ev(key_pressed):
    #send the pressed key to ev
    return

def read_key(key):
    if key.event_type == keyboard.KEY_DOWN:
        print(f"Key pressed: {key.name}")
        send_to_ev(key.name)

keyboard.hook(read_key)

keyboard.wait("esc")