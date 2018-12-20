import numpy as np
import cv2 as cv
import os
from moviepy.editor import *
from PIL import Image
import matplotlib.pyplot as plt

cap = cv.VideoCapture('d.mp4')
count = 0
i = 0
j = 1
arr_frame = []
arr_ratio = []
ratiopre = 0
rationext = 0

# create dir save frame and keyframe
try:
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('keyframe'):
        os.makedirs('keyframe')
except OSError:
    print ('Error: Creating directory')

while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:
        print('Read %d frame: ' % count, ret)
        cv.imwrite("./data/frame%d.jpg" % count, frame)  # save frame as JPEG file

        # Calculate ratio
        if count >= 1:
            if count == 1:

                img1 = cv.imread("./data/frame%d.jpg" % (count - 1))
                img2 = cv.imread("./data/frame%d.jpg" % count)

                gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
                gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

                sift = cv.xfeatures2d.SIFT_create()

                kp1, des1 = sift.detectAndCompute(gray1, None)
                kp2, des2 = sift.detectAndCompute(gray2, None)

                # Create BFMatcher object
                bf = cv.BFMatcher()

            else:
                img1 = img2
                gray1 = gray2
                kp1 = kp2
                des1 = des2

                img2 = cv.imread("./data/frame%d.jpg" % count)

                gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

                kp2, des2 = sift.detectAndCompute(gray2, None)

            if len(kp1) == 0 or len(kp2) == 0:
                rationext = 0
            else:
                # Match descriptors.
                matches = bf.match(des1, des2)
                rationext = len(matches) / (len(des1) + len(des2))

            # os.remove('frame%d.jpg' % (count - 1))

        # Cut clip if ratio > threshold = 0.069
        if rationext != 0:

            print(abs(rationext - ratiopre))

            # add arr_frame and arr_ratio
            arr_frame.append(count)
            arr_ratio.append(abs(rationext - ratiopre))

            if abs(rationext - ratiopre) > 0.069:

                if j == 0:
                    # create image red
                    img = Image.new('RGB', (60, 30), color='red')
                    img.save('./data/frame%d.png' % (count - 1))

                    cv.imwrite("./keyframe/keyFrame%d.jpg" % i, frame)  # save frame as JPEG file
                    i += 1
                    j += 1
                else:
                    j -= 1

        ratiopre = rationext
        count += 1
    else:
        # os.remove('frame%d.jpg' % (count-1))
        # os.remove('frame%d.jpg' % cur)
        break

#add x and y labels
plt.xlabel('Frame')
plt.ylabel('Ratio')

#show plot
plt.plot(arr_frame, arr_ratio)
plt.show()

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
