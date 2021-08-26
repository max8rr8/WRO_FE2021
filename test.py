import hardware

while not hardware.read_button():
    hardware.get_frame()