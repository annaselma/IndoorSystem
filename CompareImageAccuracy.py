#!/usr/bin/env python
# coding: utf-8

# In[41]:


from PIL import Image
import os
import cv2
import numpy as np
 #The images should be in the same sizes 
i1 = Image.open("frame90.jpg")
i2 = Image.open("frame89.jpg")
assert i1.mode == i2.mode, "Different kinds of images."
assert i1.size == i2.size, "Different sizes."
 
pairs = zip(i1.getdata(), i2.getdata())
if len(i1.getbands()) == 1 :
    # for gray-scale jpegs
    dif = sum(abs(p1-p2) for p1,p2 in pairs)
    print ("The image are the same")
else:
    print ("The image are different")
    dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
 
ncomponents = i1.size[0] * i1.size[1] * 3
print ("Difference (percentage):", (dif / 255.0 * 100) / ncomponents, "%")


# In[ ]:





# In[ ]:




