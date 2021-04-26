import cv2

video_path = '../your-video'

# read video file
cap = cv2.VideoCapture(video_path)

fgbg = cv2.createBackgroundSubtractorMOG2()

while (1):

    # if ret is true than no error with cap.isOpened
    ret, frame = cap.read()

    # additional bluring to handle real life noise
    blur_frame = cv2.GaussianBlur(frame, (15, 15), 0)

    if ret == True:

        # apply background subtraction
        fgmask = fgbg.apply(blur_frame)

        (contours, hierarchy) = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # looping for contours
        for c in contours:
            if cv2.contourArea(c) < 150:
                continue

            # get bounding box from countour
            (x, y, w, h) = cv2.boundingRect(c)

            # draw bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('foreground and background', fgmask)
        cv2.imshow('rgb', frame)

        k = cv2.waitKey(20) & 0xff
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()
