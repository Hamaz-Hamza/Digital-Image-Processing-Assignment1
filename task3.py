import cv2 as opencv

imageLocation = "image.bmp"
# read image from file
image = opencv.imread(imageLocation)

# resize the image
image = opencv.resize(image, (256, 256))

# convert to grayscale
image = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)

# convert to binary
ret, bw_img = opencv.threshold(image, 127, 255, opencv.THRESH_BINARY)

# display the image
opencv.imshow("image",bw_img)

# wait for user to press a key or close the image
opencv.waitKey(0)
  
# closing all open windows
opencv.destroyAllWindows()
