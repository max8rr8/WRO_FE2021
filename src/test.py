# import hardware

# import time


# # for i in range(50):
# #     hardware.steer(-40)
# #     time.sleep(0.3)
# # hardware.steer(40)
# #     time.sleep(0.3)
# # 
# kk = 3.6
# hardware.forward()
# for i in range(3):
#     hardware.steer(50)
#     time.sleep(kk)
#     hardware.steer(-50)
#     time.sleep(kk)


# hardware.stop_center()

import cv2

# Open Pi Camera
cap = cv2.VideoCapture(0)
# Set auto exposure to false
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
cap.set(cv2.CAP_PROP_WHITE_BALANCE_RED_V, 0)
cap.set(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U, 0)
    
exposure = 0
while cap.isOpened():
    # Grab frame
    ret, frame = cap.read()
    # Display if there is a frame
    if ret:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Set exposure manually
    # Increase exposure for every frame that is displayed
    exposure += 0.5

# Close everything
cap.release()
cv2.destroyAllWindows()