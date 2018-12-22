# IT4851
                                                Multimedia Database System
 - IDE : PyCharm Community Edition , Python 3.7.0
 - Library : OpenCV
 - Author : Student at Ha Noi University of Science and Technology
 
                                   **********************************************
 - pip3 install opencv-python==3.4.1 opencv-contrib-python==3.4.1
 
                                    **********************************************
Simple video segmentation (detection of shots) using local characteristics Use OpenCV to install a video segmentation application.
 
Basic requirements: Input: 1 Video
 
Output: the video and the corresponding keyframe
 
Method: Find similarity copper of the next two frames use local characteristics (sift or surf). The similarity is measured by the   number of specific points that are matched on the average plus the number of points detected.

Use threshold to locate there is a big difference to determine the margin of the shot. Students are free to propose solutions to use the appropriate threshold (1 threshold or 2 thresholds). What is the threshold value? ...).

Keyframe for every shot can choose as the frame has the greatest number of features. However, students can propose their solutions  to identify keyframes in this case

Request: Need a demo and perform tests to evaluate the pros / cons of method. In the report, it is necessary to specify what the implemented method is, especially emphasizing the proposed group points. Clarify advantages and disadvantages of the method and give examples. Note, the impact of the parameters on the final results of the system needs to be assessed.

A number of methods of detecting footage were introduced in the lecture with links to the article of each method. SV is not required to install correctly 1 of the methods But that method can be consulted to provide an effective installation solution.
