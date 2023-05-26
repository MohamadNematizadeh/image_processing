
import cv2
import numpy as np

# Initialize webcam
cap = cv2.VideoCapture(0)

# Define color ranges
red_lower = np.array([0, 0, 100])
red_upper = np.array([50, 50, 255])

green_lower = np.array([0, 100, 0])
green_upper = np.array([50, 255, 50])

blue_lower = np.array([100, 0, 0])
blue_upper = np.array([255, 50, 50])

yellow_lower = np.array([0, 100, 100])
yellow_upper = np.array([50, 255, 255])

orange_lower = np.array([0, 70, 140])
orange_upper = np.array([50, 170, 255])

purple_lower = np.array([100, 0, 100])
purple_upper = np.array([255, 50, 255])

# Loop through frames
while True:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert RGB to BGR
    bgr_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # Apply color ranges
    red_mask = cv2.inRange(bgr_frame, red_lower, red_upper)
    green_mask = cv2.inRange(bgr_frame, green_lower, green_upper)
    blue_mask = cv2.inRange(bgr_frame, blue_lower, blue_upper)
    yellow_mask = cv2.inRange(bgr_frame, yellow_lower, yellow_upper)
    orange_mask = cv2.inRange(bgr_frame, orange_lower, orange_upper)
    purple_mask = cv2.inRange(bgr_frame, purple_lower, purple_upper)
    
    # Find contours
    red_contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    green_contours, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    yellow_contours, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    orange_contours, _ = cv2.findContours(orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    purple_contours, _ = cv2.findContours(purple_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw bounding boxes around contours
    for contour in red_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    for contour in green_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    for contour in blue_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    for contour in yellow_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
    
    for contour in orange_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 140, 255), 2)
    
    for contour in purple_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
    
    # Display image
    cv2.imshow('Color Recognition', frame)
    
    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release webcam and destroy windows
cap.release()
cv2.destroyAllWindows()