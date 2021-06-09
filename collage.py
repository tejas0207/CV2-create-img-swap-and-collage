# 🔅 Task 4.3
# 📌 Take 2 image and combine it to form single image. For example collage
final = numpy.hstack((photo , photo_1))
cv2.imshow("myphoto",final)
cv2.waitKey()
cv2.destroyAllWindows()
