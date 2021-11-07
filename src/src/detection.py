import cv2


def binarize(img, bin_min, bin_max):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv[:, :, 0][hsv[:, :, 0] > 165] = 0
    bin_image = cv2.inRange(hsv, bin_min, bin_max)
    bin_image = cv2.erode(bin_image, None, iterations=4)
    bin_image = cv2.dilate(bin_image, None, iterations=4)

    return bin_image


def get_contour_params(cnt):
    M = cv2.moments(cnt)
    area = M['m00']
    cx = int(M['m10'] / area)
    cy = int(M['m01'] / area)

    return area, cx, cy


def crop(img, area):
    y1, y2 = area[0]
    x1, x2 = area[1]
    return img[y1:y2, x1:x2]


def detect_object(name,
                  img,
                  zone,
                  bin_min,
                  bin_max,
                  area_min,
                  show=True,
                  show_unbinarized=True):
    img = crop(img, zone)
    contour = None
    area, cx, cy = (None, None, None)

    binarized = binarize(img, bin_min, bin_max)
    debug = cv2.cvtColor(binarized, cv2.COLOR_GRAY2BGR)
    
    contours = cv2.findContours(binarized, cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_NONE)[0]

    if len(contours) > 0:
        cv2.drawContours(debug, contours, -1, (0, 255, 0), 1)
        area = cv2.contourArea(contours[0])
        contours = list(
            filter(lambda c: cv2.contourArea(c) > area_min, contours))
        if len(contours) > 0:
            cv2.drawContours(debug, contours, -1, (0, 255, 0), 3)

            contour = max(contours, key=cv2.contourArea)
            area, cx, cy = get_contour_params(contour)

            cv2.drawContours(debug, [contour], -1, (0, 0, 255), 3)
            cv2.circle(debug, (cx, cy), 5, (0, 0, 255), -1)
    if show:
        if show_unbinarized:
            debug = cv2.cvtColor(binarized, cv2.COLOR_GRAY2BGR)
            cv2.imshow(name, cv2.hconcat([img, debug]))
        else:
            cv2.imshow(name, debug)
    return contour, (area, cx, cy)