import cv2

def ShowImage(image):
    cv2.imshow("result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# load image
img = cv2.imread("task4.png")

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur the image
blur = cv2.GaussianBlur(gray, (0,0), sigmaX=3, sigmaY=3)

# apply otsu thresholding
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

# find contours(boundaries between background and foreground)
contours,h = cv2.findContours(thresh,1,2)

# number of objects = len(contours)-1 because we are not counting the background
print("number of objects in image = " + str(len(contours)-1))

# display the image
ShowImage(thresh)