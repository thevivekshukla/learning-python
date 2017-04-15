import glob2
import cv2

images = glob2.glob('*.jpg')

for image in images:
  img = cv2.imread(image, 1)
  new_img = cv2.resize(img, (100, 100))
  cv2.imwrite('100x100_'+image, new_img)