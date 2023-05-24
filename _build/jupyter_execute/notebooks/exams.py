#!/usr/bin/env python
# coding: utf-8

# # Εξετάσεις στον Προγραμματισμό Η/Υ

# Το τρέχον notebook μπορείτε να το χρησιμοποιήσετε ως πρόχειρο για την δοκιμαστική εκτέλεση κώδικα.

# In[3]:





# In[1]:


import numpy as np
np.random.seed(seed=123)
myarray= np.random.randint(1,1000, size=(100,100))
myarray


# In[2]:


import numpy.ma as ma #εισαγωγή της απαραίτητης βιβλιοθήκης


# In[3]:


x=np.arange(6)


# In[4]:


x_masked = ma.masked_array(x, mask=[1,0,0,0,0,0])
np.nanmean(x_masked)
type(x_masked)

