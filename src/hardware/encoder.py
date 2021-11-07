import Encoder

Tuner = Encoder.Encoder(17, 27)
start_ticks = 0

def reset_encoder():
    global start_ticks
    start_ticks = int(Tuner.read())

def read_encoder():
    return int(Tuner.read()) - start_ticks