# import the necessary packages
from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
webcam = cv2.VideoCapture(0)
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="example.avi",
	help="path to output video file")
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
ap.add_argument("-f", "--fps", type=int, default=20,
	help="FPS of output video")
ap.add_argument("-c", "--codec", type=str, default="MJPG",
	help="codec of output video")
args = vars(ap.parse_args())

# initialize the video stream and allow the camera
# sensor to warmup
print("[INFO] warming up camera...")
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)


def calculate_fps(self):
        

    
    fps = self.get(cv2.CAP_PROP_FPS)
    print("Framerate = %0.2f FPS" % (fps))


# initialize the FourCC, video writer, dimensions of the frame, and
# zeros array
fps = calculate_fps(webcam)
fourcc = cv2.VideoWriter_fourcc(*args["codec"])
writer = None
(h, w) = (1280, 720)
zeros = None

# loop over frames from the video stream
while True:
	# grab the frame from the video stream and resize it to have a
	# maximum width of 300 pixels
	frame = vs.read()
    
	#frame = imutils.resize(frame, width=300)
 
	# check if the writer is None
	if writer is None:
		# store the image dimensions, initialize the video writer,
		# and construct the zeros array
		#(h, w) = frame.shape[:2]
      
		writer = cv2.VideoWriter(args["output"], fourcc, 30,(w , h ), True)
		


 
	# construct the final output frame, storing the original frame
	# at the top-left, the red channel in the top-right, the green
	# channel in the bottom-right, and the blue channel in the
	# bottom-left
	output = np.zeros((h , w , 3), dtype="uint8")
	output[0:h, 0:w] = frame

 
	# write the output frame to file
	writer.write(output)

    # show the frames
	cv2.imshow("Frame", frame)
	cv2.imshow("Output", output)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
 
# do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop()
writer.release()