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
# iterate i from 1 to 1406
#url="http://xkcd.com/"+i+"/"

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

#otsu 
threshold_global_otsu = threshold_otsu(color.rgb2grey(img))
img = color.rgb2grey(img) >= threshold_global_otsu
# io.imshow(img)
# io.show()

# #invert img
# x=np.ones(img.shape)
# x.fill(1)
# img=x-img

# img=morph.binary_erosion(img, np.array([[1,1]]))
# img=morph.binary_dilation(img, np.array([[1,1]]))
# img=morph.binary_erosion(img, np.array([[1],[1]]))
# img=morph.binary_dilation(img, np.array([[1],[1]]))
# #invert img
# x=np.ones(img.shape)
# x.fill(1)
# img=x-img

# io.imshow(img)
# io.show()


for i in range(2):
	#closing1
	mask1=np.array([[1],[1]])
	img=morph.binary_closing(img, mask1, out=None)


	mask1=np.array([[1,1]])
	img=morph.binary_closing(img, mask1, out=None)



io.imshow(img)
io.show()


#invert img
x=np.ones(img.shape)
x.fill(1)

img=x-img

img=morph.binary_erosion(img,np.array([[1,1],[1,1]]))


#invert img
x=np.ones(img.shape)
x.fill(1)

img=x-img




io.imshow(img)
io.show()





# # #invert img
# # x=np.ones(img.shape)
# # x.fill(1)

# # img=x-img


# # #skeleton
# # img=morph.medial_axis(img, mask=np.array([[1,1],[1,1]]), return_distance=False)




# # #invert img
# # x=np.ones(img.shape)
# # x.fill(1)

# # img=x-img

# # io.imshow(img)
# # io.show()


#draw histogram

# (h,l)=img.shape

# hist=np.ones(l)
# sum=0
# for i in range(l):
# 	sum=0
# 	for j in range(h):
# 		sum+=(1-img[j,i])
	
# 	hist[i]=sum

# plt.plot(hist)
# plt.show()

# hist=np.ones(l)
# sum=0
# for i in range(l):
# 	sum=0
# 	for j in range(h):
# 		sum+=(1-img[j,i])
	

# 	if sum>1:
# 		hist[i]=sum-1
# 	else:
# 		hist[i]=0

# plt.plot(hist)
# plt.show()

# #getting a list of postions of zero pixels
# p=[]
# for i in range(l):
# 	# if abs(hist[i]-hist[i+3])>2 and hist[i]<3:
# 	# 	print i
# 	if hist[i]==0:
# 		p.append(i)

# print p

# rise=[]
# fall=[]
# for i in range(5,len(p)-6):
# 	if abs(p[i]-p[i+1])>5 and abs((p[i]+p[i-1]+p[i-2]+p[i-3]+p[i-4]+p[i-5]+p[i-6])/7 - p[i-3])<=1:
# 		rise.append(p[i])


# 	if abs(p[i]-p[i-1])>5 and abs((p[i]+p[i+1]+p[i+2]+p[i+3]+p[i+4]+p[i+5]+p[i+6])/7 - p[i+3])<=1:
# 		fall.append(p[i])


# m=len(rise)-1
# i=0
# while i<m:
# 	if rise[i+1]-rise[i] < 30:
# 		del rise[i+1]
# 		m=m-1
# 	i=i+1	

# m=len(fall)-1
# i=0
# while i<m:
# 	if fall[i+1]-fall[i] < 30:
# 		del fall[i+1]
# 		m=m-1
# 	i=i+1	

# i=0

# # m=len(rise)-1

# # m=len(fall)-1
# # while i<m and i<n:
# # 	if rise[i+1]-fall[i] < 20:
# # 		del rise[i+1]
# # 		m=m-1
# # 	i=i+1
# print rise

# print fall
# #separate each character