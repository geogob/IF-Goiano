"""
===============================
Dense DAISY feature description
===============================

The DAISY local image descriptor is based on gradient orientation histograms
similar to the SIFT descriptor. It is formulated in a way that allows for fast
dense extraction which is useful for e.g. bag-of-features image
representations.

In this example a limited number of DAISY descriptors are extracted at a large
scale for illustrative purposes.
"""
from skimage.feature import daisy
from skimage import data
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.color import rgb2hed
from skimage import exposure

img=plt.imread('dataset/Sem ferrugem/sem-18.jpg')

ihc_rgb = img
ihc_hed = rgb2hed(ihc_rgb)

#lena = img_as_float(np.array(Image.open('dataset/Com ferrugem/com-01.jpg')))
image = ihc_hed[:, :, 0] #img[:,:,0]
img_eq = exposure.equalize_hist(image)

img = rgb2gray(img)
descs, descs_img = daisy(img_eq, step=180, radius=58, rings=2, histograms=6,
                         orientations=8, visualize=True)

fig, ax = plt.subplots()
ax.axis('off')
ax.imshow(descs_img)
descs_num = descs.shape[0] * descs.shape[1]
ax.set_title('%i DAISY descriptors extracted:' % descs_num)
plt.show()
