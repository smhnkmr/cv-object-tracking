import cv2

#tracker = cv2.TrackerKCF_create()
tracker = cv2.TrackerCSRT_create()

video = cv2.VideoCapture('street.mp4')
ok, frame = video.read()

bbox = cv2.selectROI(frame)

ok = tracker.init(frame, bbox)

while True:

    # Capture frame-by-frame
    ok, frame = video.read()

    if not ok:
        break

    ok, bbox = tracker.update(frame)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)

    # Display the resulting frame
    cv2.imshow('Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video.release()
cv2.destroyAllWindows()