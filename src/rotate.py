from config import OBJECTS
from src.detection import detect_object


def should_start_rotate(img):
    main_line = detect_object(name="main_line", img=img, **OBJECTS.MAIN_LINE)
    return main_line[0] is not None
