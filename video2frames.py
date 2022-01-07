import cv2
import sys

try:
    video_path = r'{}'.format(sys.argv[1])
except IndexError:
    print("Usage: video2frames.py <video_file>")
    sys.exit(0)

video  = cv2.VideoCapture(video_path)

if not video.isOpened():
    print('Error : Cannot open video file')

i = 0
while(video.isOpened()):
    ret, frame = video.read()
    if ret:
        cv2.imwrite('./data/validation/frame-{}.jpg'.format(i), frame)
        i += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()