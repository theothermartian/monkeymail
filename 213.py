from bs4 import BeautifulSoup
import urllib2
import numpy as np
from skimage import filter
from scipy import ndimage
from skimage.transform import resize
from skimage.filter import threshold_otsu
import urllib
import matplotlib.pyplot as plt

import skimage.io as io
import skimage.color as color
import skimage.morphology as morph


proxy = urllib2.ProxyHandler({'http': 'http://s.sayak:kx8qnSBY@202.141.80.19:3128'})
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
urllib2.install_opener(opener)


# #image acquisition
# img=open("1.png","wb")
# img.write((urllib2.urlopen("https://webmail.iitg.ernet.in/plugins/captcha/backends/watercap/image_generator.php")).read())
# img.close()



#original
img = io.imread('1.png')
# io.imshow(img)
# io.show()

img=color.rgb2grey(img)



img=ndimage.gaussian_filter(img, sigma=2)
io.imshow(img)
io.show()
#otsu 
threshold_global_otsu = threshold_otsu(img)
img = color.rgb2grey(img) >= threshold_global_otsu


#dilation
x=np.ones(img.shape)
x.fill(1)
img=x-img

for i in range(2):
	img=morph.binary_dilation(img, np.array([[1,1],[1,1]]), out=None)



x=np.ones(img.shape)
x.fill(1)
img=x-img

io.imshow(img)
io.show()


x=np.ones(img.shape)
x.fill(1)
img=x-img

for i in range(2):
	img=morph.binary_erosion(img, np.array([[1,1],[1,1]]), out=None)
	

x=np.ones(img.shape)
x.fill(1)
img=x-img
io.imshow(img)
io.show()
#draw histogram

(h,l)=img.shape

hist=np.ones(l)
sum=0
for i in range(l):
	sum=0
	for j in range(h):
		sum+=(1-img[j,i])
	
	hist[i]=sum

plt.plot(hist)
plt.show()


