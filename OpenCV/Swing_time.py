import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('1.mp4')

# Set up the background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

# Initialize variables
foot_in_air = False
swing_start = 0
swing_end = 0

# Loop through each frame in the video
while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break
    
    # Apply background subtraction to isolate the moving object (the person)
    fgmask = fgbg.apply(frame)
    
    # Apply a threshold to convert the image to binary
    thresh = cv2.threshold(fgmask, 127, 255, cv2.THRESH_BINARY)[1]
    
    # Find contours in the thresholded image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Loop through each contour
    for contour in contours:
        # Find the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        
        # Check if the contour is in the lower half of the frame (where the feet are)
        if y + h > frame.shape[0] / 2:
            # Check if the foot is in the air
            if not foot_in_air:
                # If the foot was on the ground and is now in the air, mark the start of the swing phase
                foot_in_air = True
                swing_start = cap.get(cv2.CAP_PROP_POS_MSEC)
        else:
            # If the foot is on the ground, mark the end of the swing phase and reset the foot_in_air variable
            if foot_in_air:
                foot_in_air = False
                swing_end = cap.get(cv2.CAP_PROP_POS_MSEC)
                
                # Calculate the swing time
                swing_time = swing_end - swing_start
                print(f"Swing time: {swing_time:.2f} ms")
    
    # Display the frame
    cv2.imshow('frame', frame)
    
    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
