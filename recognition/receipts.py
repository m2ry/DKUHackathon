pip install opencv-contrib-python

from imutils.perspective import four_point_transform
import pytesseract
import argparse
import imutils
import cv2
import re

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
ap.add_argument("-d", "--debug", type=int, default=-1)
args = vars(ap.parse_args())

orig = cv2.imread(args["image"])
image = orig.copy()
image = imutils.resize(image, width=500)
ratio = orig.shape[1] / float(image.shape[1])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5,), 0)
edge = cv2.Canny(blur, 75, 200)

if args["debug"] > 0:
  cv2.imshow("Input", image)
  cv2.imshow("W/ Edges", edge)
  cv2.waitKey(0)

contours = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

receipt_contour = None

for c in contours:
  perimeter = cv2.arcLength(c, True)
  approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)

  if len(approx) == 4:
    receipt_contour = approx
    break

if args["debug"] > 0:
  output = image.copy()
  cv2.drawContours(output, [receipt_contours], -1, (0, 255, 0), 2)
  cv2.imshow("Receipt Outline", output)
  cv2.waitKey(0)

receipt = four_point_transform(orig, receiptContours.reshape(4, 2) * ratio)

cv2.imshow(imutils.resize(receipt, width=500))
cv2.waitKey(0)

options = "--psm 4"
text = pytesseract.image_to_string(cv2.cvtColor(receipt, cv2.COLOR_BGR2RGB), config=options)

print("[INFO} raw output:")
print(text)
print("\n")

pricePattern = r'([0-9]+\.[0-9]+)'
print("[INFO] price line items:")

for row in text.split("\n"):
  if re.search(pricePattern, row) is not None:
    print(row)
