import cv2 as opencv

imageLocation = "image.bmp"
# read image from file
image = opencv.imread(imageLocation)

# resize the image
image = opencv.resize(image, (256, 256))

# display the image
opencv.imshow("image",image)

# wait for user to press a key or close the image
opencv.waitKey(0)
  
# closing all open windows
opencv.destroyAllWindows()