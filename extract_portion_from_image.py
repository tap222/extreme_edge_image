import numpy as np
import cv2

img = cv2.imread("pepsi.jpg")
pts = np.array([[542, 107], [562, 102], [582, 110], [598, 142], [600, 192], [601, 225], [592, 261], [572, 263], [551, 245], [526, 220], [520, 188], [518, 152], [525, 127], [524, 107]], dtype=np.int32)

mask = np.zeros((img.shape[0], img.shape[1]))
cv2.fillConvexPoly(mask, pts, 1)
mask = mask.astype(np.bool)

out = np.zeros_like(img)
out[mask] = img[mask]
cv2.imshow('Extracted Image', out)
cv2.waitKey(0)
cv2.destroyAllWindows()
