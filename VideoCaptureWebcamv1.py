# import the necessary packages
# This code is based on the opencv functions

# works perfect and saves camera paramter logfile

import numpy as np
import argparse
import imutils
import time
import cv2
import pickle
import csv

webcam = cv2.VideoCapture(0)
writer = None
zeros = None
#data = [] 
# initialize the video stream and allow the camera
# sensor to warmup
print("[INFO] warming up camera...")


fps =  int(webcam.get(cv2.CAP_PROP_FPS)) # Frame rate
frame_h =  int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT )) #Height of the frames in the video stream
frame_w =  int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH)) #Width of the frames in the video stream
frame_f = int(webcam.get(cv2.CAP_PROP_FORMAT)) #Format of the Mat objects returned by retrieve() .
frame_m = int(webcam.get(cv2.CAP_PROP_MODE)) #Backend-specific value indicating the current capture mode.
frame_b = int(webcam.get(cv2.CAP_PROP_BRIGHTNESS)) #Brightness of the image (only for cameras).
frame_c = int(webcam.get(cv2.CAP_PROP_CONTRAST)) #Contrast of the image (only for cameras).
frame_s = int(webcam.get(cv2.CAP_PROP_SATURATION)) #Saturation of the image (only for cameras).
frame_hu = int(webcam.get(cv2.CAP_PROP_HUE)) #Hue of the image (only for cameras).
frame_g = int(webcam.get(cv2.CAP_PROP_GAIN)) #Gain of the image (only for cameras).
frame_e = int(webcam.get(cv2.CAP_PROP_EXPOSURE)) #Exposure (only for cameras).
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')



time.sleep(1.0)

# loop over frames from the video stream
while True:
	# grab the frame from the video stream and resize it to have a

	retval,frame = webcam.read()
	cv2.imshow("Capturing", frame)
	#frame = imutils.resize(frame, width=300)
 
	# check if the writer is None
	if writer is None:
		writer = cv2.VideoWriter("example.avi", fourcc,fps,(frame_w , frame_h ), True)
	
	# output = np.zeros((frame_h , frame_w , 3), dtype="uint8")
	# output[0:frame_h, 0:frame_w,0:3] = frame

	# write the output frame to file
	writer.write(frame)

	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
 
# do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
#webcam.stop()
writer.release()




# save camera parametric data
with open('camera_parameters', 'wb') as f:
    pickle.dump([fps,frame_b,frame_c,frame_f,frame_g,frame_h,frame_hu,frame_m,frame_s,frame_w], f)


with open('camera_parameters.csv', 'w') as file:
	writer = csv.writer(file, delimiter = '\t')
	writer.writerow(["Parameter", "Value"])
	writer.writerow(["Frame rate",fps])
	writer.writerow(["Height of the frames in the video stream",frame_h])
	writer.writerow(["Width of the frames in the video stream",frame_w])
	writer.writerow(["Format of the Mat objects returned by retrieve()",frame_f])
	writer.writerow(["Backend-specific value indicating the current capture mode",frame_m])
	writer.writerow(["Brightness of the image (only for cameras)",frame_b])
	writer.writerow(["Contrast of the image",frame_c])
	writer.writerow(["Saturation of the image ",frame_s])
	writer.writerow(["Hue of the image",frame_hu])
	writer.writerow(["Gain of the image ",frame_g])
	writer.writerow(["Exposure",frame_e])




        

