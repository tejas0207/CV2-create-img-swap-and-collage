# 🔅 Task 4.2
# 📌 Take 2 image crop some part of both image and swap it.
import cv2
import numpy
photo=cv2.imread('download.jpg')
cv2.imshow("myphoto",photo)
cv2.waitKey(5000)
cv2.destroyAllWindows()
photo_1=cv2.imread('images.jpg')
cv2.imshow("myphoto",photo_1)
cv2.waitKey()
cv2.destroyAllWindows()
photo_2=photo_1[60:140,30:193]
cv2.imshow("myphoto",photo_2)
cv2.waitKey(5000)
cv2.destroyAllWindows()
photo[60:140,30:193]=photo_2
cv2.imshow("myphoto",photo)
cv2.waitKey()
cv2.destroyAllWindows()
photo_3=cv2.imread('download.jpg')
photo_4=photo_3[60:140,30:193]
cv2.imshow("myphoto",photo_4)
cv2.waitKey(5000)
cv2.destroyAllWindows()

photo_1[60:140,30:193]=photo_4
cv2.imshow("myphoto",photo_1)
cv2.waitKey()
cv2.destroyAllWindows()
