import cv2
import numpy as np
from matplotlib import pyplot as plt

directory = 'photos2/picture.jpg'

img = cv2.imread(directory)
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

lab_img[:, :, 0] = (lab_img[:, :, 0].astype(float) * 0.7).clip(0,255).astype(np.uint8)
lab_img[:, :, 1] = (lab_img[:, :, 1].astype(float) * 1.05).clip(0,255).astype(np.uint8)
lab_img[:, :, 2] = (lab_img[:, :, 2].astype(float) * 1.1).clip(0,255).astype(np.uint8)

lab_img = cv2.cvtColor(lab_img, cv2.COLOR_LAB2RGB)

plt.figure(figsize=(15, 15))
plt.imshow(lab_img)
plt.show()

cv2.imwrite("photos2/result.jpg", cv2.cvtColor(lab_img, cv2.COLOR_BGR2RGB))
