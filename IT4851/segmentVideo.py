import numpy as np
import cv2 as cv
import os
from moviepy.editor import *

cap = cv.VideoCapture('example.mp4')
count = 0
i = 0
ratiopre = 0
rationext = 0
start_time = 0
end_time = 0

while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:
        print('Read %d frame: ' % count, ret)
        cv.imwrite("frame%d.jpg" % count, frame)  # save frame as JPEG file

        # Calculate ratio
        if count >= 1:
            if count == 1:

                img1 = cv.imread('frame%d.jpg' % (count - 1))
                img2 = cv.imread('frame%d.jpg' % count)

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

                img2 = cv.imread('frame%d.jpg' % count)

                gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

                kp2, des2 = sift.detectAndCompute(gray2, None)

            # Match descriptors.
            matches = bf.match(des1, des2)

            if len(kp1) == 0 or len(kp2) == 0:
                rationext = 0
            else:
                rationext = len(matches) / (len(des1) + len(des2))

            os.remove('frame%d.jpg' % (count - 1))

        # Cut clip if ratio > threshold = 0.7
        if rationext != 0:

            print(rationext - ratiopre)

            if (rationext - ratiopre) > 0.26:
                # end_time = count / 30
                #
                # my_clip = VideoFileClip("intro.mp4")
                #
                # clip1 = my_clip.subclip(start_time, end_time)
                #
                # processed_vid = clip1.write_videofile('video%d.mp4' % i)
                #
                # start_time = end_time

                cv.imwrite("keyFrame%d.jpg" % i, frame)  # save frame as JPEG file
                i += 1

        ratiopre = rationext
        count += 1
    else:
        os.remove('frame%d.jpg' % pre)
        os.remove('frame%d.jpg' % cur)
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
