import cv2

# Load an image from file
image_path = 'your_image_path.jpg'  # Replace with the path to your image file
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Could not load the image from path {image_path}")
else:
    # Display the image in a window
    cv2.imshow('Loaded Image', image)

    # Wait for a key press and close the image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
