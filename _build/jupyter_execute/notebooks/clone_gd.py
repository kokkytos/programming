#!/usr/bin/env python
# coding: utf-8

# # Λήψη αποθετηρίου στο Google Drive

# Μέσω του τρέχοντος notebook γίνεται η λήψη του github αποθετηρίου στο Google Drive.
# Το notebook αυτό πρέπει να εκτελεστεί μέσω του Google Colab.
# 

# In[1]:


# έλεγχος αν το notebook τρέχει στο google colab
try:
    from google.colab import drive
    drive.mount('/content/drive')
    get_ipython().run_line_magic('cd', '/content/drive/MyDrive/Colab\\ Notebooks/')
    get_ipython().system('git clone https://github.com/kokkytos/programming.git')
except:
  print("Παρακαλώ εκτελέστε το notebook στο Google Colab")


# In[ ]:




