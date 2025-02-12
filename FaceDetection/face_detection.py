import cv2
import numpy as np

# Load the cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('test1.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.05, 7)

#to draw circle, oval,polygon
# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cx= x + w // 2
    cy= y + h // 2  # Center of the face of x,y
    #to draw circle
    #radius = max(w, h) // 2  # Approximate radius
    #cv2.circle(img, (cx, cy), radius, (0, 255, 0), 2)
    cv2.ellipse(img, (cx, cy), (w // 2, h // 2), 0, 0, 360, (0, 0, 255), 2)

#to draw diamond 
    #pts = np.array([
        #[cx, y],      # Top-center
        #[x + w, cy],  # Right-center
        #[cx, y + h],  # Bottom-center
        #[x, cy]       # Left-center
    #], np.int32)

    #pts = pts.reshape((-1, 1, 2))
    #cv2.polylines(img, [pts], isClosed=True, color=(255, 255, 0), thickness=2)

# Draw rectangles around detected faces
    #cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)

# Display the output image
cv2.imshow('img', img)

# Save the image with the detected faces
cv2.imwrite("face_detected4.jpeg", img)

# Wait for a key press and close the window
cv2.waitKey()
cv2.destroyAllWindows()
