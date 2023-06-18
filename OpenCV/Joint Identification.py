import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find the edges in the image using the Canny algorithm
edges = cv2.Canny(thresh, 100, 200)

# Find contours in the edges image
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop through the contours and find the one that is most likely to be a leg
max_area = 0
max_contour = None
for contour in contours:
    area = cv2.contourArea(contour)
    if area > max_area:
        max_area = area
        max_contour = contour

# Draw the contour on the original image
cv2.drawContours(img, [max_contour], -1, (0, 255, 0), 2)

# Display the original image with the leg contour drawn on it
cv2.imshow('Leg Detection', img)
cv2.waitKey(0)