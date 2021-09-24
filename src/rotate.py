from config import OBJECTS
from src.detection import detect_object
import time 

last_seen = 0

def should_start_rotate(img, direction):
    global last_seen
    # print(direction)
    main_line = detect_object(name="main_line", img=img, **OBJECTS.MAIN_LINE[direction])
    main_line = main_line[0] is not None

    if not main_line:
        return False

    print(time.time() - last_seen)
    if time.time() - last_seen < 1.5:
        return False
    
    last_seen = time.time()

    return True