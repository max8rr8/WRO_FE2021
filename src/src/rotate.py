from config import OBJECTS
from src.detection import detect_object
import time 
import cv2

last_seen = 0
rotat = 0

def should_start_rotate(img, direction):
    global last_seen
    global rotat
    # print(direction)
    main_line = detect_object(name="main_line", img=img, **OBJECTS.MAIN_LINE[direction])
    main_line = main_line[0] is not None

    if not main_line:
        return False

    print("LINE", time.time() - last_seen)
    if time.time() - last_seen < 1:
        return False
    cv2.imwrite(f"r{rotat}.png", img)
    rotat += 1
    last_seen = time.time()

    return True