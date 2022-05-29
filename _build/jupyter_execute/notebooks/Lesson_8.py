#!/usr/bin/env python
# coding: utf-8

# # 8. Ανάγνωση αρχείων csv, η βιβλιοθήκη pandas

# Στόχος του μαθήματος είναι να εξοικειωθεί ο φοιτητής με την ανάγνωση και εγγραφή αρχείων CSV. 
# Επίσης γίνεται μια σύντομη αναφορά στις δυνατότητες της βιβλιοθήκης pandas όσον αφορά την διαχείριση δεδομένων σε μορφή πινάκων.

# ## Ανάγνωση αρχείων csv

# Εισάγουμε τα απαραίτητα άρθρωματα (modules).

# In[1]:


import os # μας επιτρέπει να έχουμε αλληλεπίδραση με το λειτουργικό σύστημα
import csv # απαραίτητο για την ανάγνωση και εγγραφή αρχείων CSV
from urllib import request # απαραίτητο για την λήψη αρχείων από το διαδίκτυο
import pandas as pd # η βιβλιοθήκη pandas για την διαχείρηση πινάκων
from pathlib import Path # βιβλιοθήκη για την διαχείριση των διαδρομών (paths) στον δίσκο
import numpy as np


# Προαιρετικά ελέγχουμε ποιος είναι ο τρέχων κατάλογος:

# In[2]:


print(os.getcwd())


# Αρχικά κατεβάζουμε από το διαδίκτυο τα αναγκαία αρχεία CSV.
# 
# (Πηγή δεδομένων https://www.kaggle.com/datasets/rinichristy/covid19-coronavirus-pandemic)

# In[3]:


# Πρώτο αρχείο
remote_url = 'https://raw.githubusercontent.com/kokkytos/programming/main/docs/COVID-19%20Coronavirus.csv'
# Define the local filename to save data
local_file1 = 'COVID-19_Coronavirus.csv'
# Download remote and save locally
request.urlretrieve(remote_url, local_file1)

# Δεύτερο αρχείο
remote_url = 'https://raw.githubusercontent.com/kokkytos/programming/main/docs/COVID-19%20Coronavirus_V2.csv'
# Define the local filename to save data
local_file2 = 'COVID-19_Coronavirus_V2.csv'
# Download remote and save locally
request.urlretrieve(remote_url, local_file2)


# In[4]:


with open(local_file1, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# In[5]:


with open(local_file1, 'r') as file:
    reader = csv.reader(file)
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Ονόματα στηλών {", ".join(row)}')
            print("\n\n")
            line_count += 1
        else:
            print(row)


# To κόμμα (,) χρησιμοποιείται ως προκαθορισμένη επιλογή σαν διαχωριστικό στηλών.
# Μπορούμε ρητά να δηλώσουμε ποιο θα είναι το διαχωριστικό με την επιλογή _delimiter_.

# In[6]:


with open(local_file2, 'r') as file:
    reader = csv.reader(file, delimiter = ';',quoting=csv.QUOTE_ALL)
    for row in reader:
        print(row)


# In[7]:


with open(local_file1, 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))


# In[8]:


with open(local_file1, 'r') as file:
    reader = csv.reader(file, delimiter = ';',quoting=csv.QUOTE_ALL)
    for row in reader:
        print(row)


# ## Εγγραφή σε csv

# In[9]:


with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    employee_writer.writerow(['John Smith', 'Accounting', 'June'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


# Εγγραφή σε CSV από dictionary (λεξικό). Σε αυτή την περίπτωση πρέπει να ορίσουμε προκαταβολικά τα ονόματα των στηλών (fieldnames παράμετρος στην μέθοδο DictWriter) για να γίνει η ταυτοποίηση των κλειδιών από το λεξικό κατά την εγγραφή.

# In[10]:


with open('employee_file2.csv', mode='w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames= ['emp_name', 'dept', 'birth_month'],delimiter=';')

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})


# ## Η βιβλιοθήκη pandas

# ![alt text](pandas-data-structure.svg)

# Δημιουργία pandas Series object 

# In[11]:


s = pd.Series([2, 4, 6, 8, 10])


# Δημιουργία pandas Dataframe object. Η τελευτάι στήλη είναι από το προηγούμενο Series object.

# In[12]:


df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83], 'V':s});
df


# Δημιουργία Index object

# In[13]:


index = pd.Index(list('abcde'))
print(index)


# Αλλαγή Index σε ένα dataframe

# In[14]:


df = df.set_index(index)
df


# Επιλογή στηλών από το dataframe df σε ένα νέο dataframe με το όνομα df_subset

# In[15]:


df_subset = df[['X','V']]
df_subset


# Ορισμός τιμών μια στήλης σε κενό (nan), με βάση κριτήρια

# In[16]:



df.loc[df['Z'] >= 96,'Z'] = np.nan
df


# Φιλτράρισμα δεδομένων

# In[17]:


df_2 =  df[df['V'] >= 6] 
df_2


# ή αλλιώς:

# In[18]:


df_2 =  df.loc[df['V'] >= 8] 
df_2


# με βάση συνθήκη όπου περιέχονται στην στήλη V τα στοιχεία της λίστας options

# In[19]:



options=[4,10]
rslt_df = df[df['V'].isin(options)] 
rslt_df


# Τροποποίηση κελιού

# In[20]:


df.at['a', 'V'] = 1000
df


# In[21]:


df.to_csv("leonidas.csv", sep=';', index=False)


# Προσθήκη γραμμής

# In[22]:


# Νεα γραμμή σαν dataframe

row_df = pd.DataFrame([ pd.Series([1,2,8,99])], index = ["f"])
row_df.columns =['X', 'Y', 'Z', 'V']
row_df


# Εναλλακτικά φτιάχνουμε αν θελουμε την ιδια γραμμή με άλλη μέθοδο (μέσω ενός dictionary):

# In[23]:


my_dictionary = {'X': [1], 'Y': [2],'Z': [8], 'V': [99]}
row_df = pd.DataFrame.from_dict(my_dictionary)
row_df = row_df.set_index(pd.Index(['f']))
row_df


# In[24]:


# Συννένωση
df1 = pd.concat([df,row_df],ignore_index=False)
df1


# Αντιμετάθεση στηλών και γραμμών (transpose)

# In[25]:


df2 = df1.T # transpose
df2


# In[26]:


list(df2.columns)


# In[27]:


list(df1.index)


# Μπορούμε να διαβάσουμε ένα αρχείο CSV σαν pandas dataframe.
# 
# Ακολουθεί το παρακάτω παράδειγμα με δεδομένα Airbnb.
# 
# Λήψη αρχείου csv από το διαδίκτυο:

# In[28]:


remote_url = 'http://data.insideairbnb.com/greece/attica/athens/2021-12-23/visualisations/listings.csv'
# Define the local filename to save data
local_file3 = 'listings.csv'
# Download remote and save locally
request.urlretrieve(remote_url, local_file3)


# Ανάγνωση του αρχείου σαν panda DataFrame

# In[29]:


# read the airbnb NYC listings csv file
airbnb = pd.read_csv(local_file3)


# Εκτύπωση των πρώτων 10 γραμμών

# In[30]:


airbnb.head()


# Εκτύπωση των 5 τελευταίων γραμμών

# In[31]:


airbnb.tail(10)


# Μπορούμε να πάρουμε για όλες τις αριθμητικές στήλες περιγραφικά στατιστικά (mean, std, min, τεταρτημόρια κτλ) με την μέθοδο describe()

# In[32]:


airbnb.describe()


# Ανάγνωση των δεδομένων μιας στήλης σαν pandas Series

# In[33]:


# Results for a single column
airbnb['name']


# Επιλογή συγκεκριμένων στηλών από το dataframe

# In[34]:


# results for multiple columns
airbnb[['host_id', 'host_name']]


# Επιστροφή του τύπου δεδομένων για όλες τις στήλες

# In[35]:


airbnb.dtypes


# Μετατροπή της στήλης last_review σε datetime64 object

# In[36]:


airbnb['last_review'] = pd.to_datetime(airbnb['last_review'])
airbnb.dtypes


# Μπορούμε να εξάγουμε το έτος από ένα datetime object σε μια νέα στήλη. Μετατροπή της στήλης year σε ακέραιο

# In[37]:


# extract the year from a datetime series
airbnb['year'] = airbnb['last_review'].dt.year

# to integer
airbnb['year'] = airbnb['year'].astype('UInt16')

airbnb['year'].head()


# Το ίδιο μπορούμε να κάνουμε και με τον μήνα.

# In[38]:


airbnb['month'] = airbnb['last_review'].dt.month
airbnb['month']=airbnb['month'].astype('UInt16')
airbnb.head()


# Αν κάποια στήλη περιέχει κενά στην αρχή ή το τέλος της μπορούμε να τα αφαιρέσουμε ως εξής:

# In[39]:


airbnb['name'] = airbnb['name'].str.strip()
airbnb['name'].head()


# Μετατροπή όλων των χαρακτήρων μιας στήλης σε πεζά:

# In[40]:


airbnb['name_lower'] = airbnb['name'].str.lower()
airbnb['name_lower'].head()


# Δημιουργία μιας στήλης που στηρίζεται σε υπολογισμό μεταξύ άλλων στηλών (calculated column)

# In[41]:


airbnb['min_revenue'] = airbnb['minimum_nights'] * airbnb['price']
airbnb[['minimum_nights', 'price', 'min_revenue']]


# Υπολογισμός του μέσου όρου μιας στήλης

# In[42]:


airbnb['price'].mean()


# Υπολογισμός του διαμέσου μιας στήλης

# In[43]:


airbnb['price'].median()


# Υπολογισμό μέσου όρου τιμής ανά τύπο δωματίου

# In[44]:


airbnb[['room_type', 'price']].groupby('room_type', as_index=False).mean()


# Υπολογισμό διαμέσου τιμής ανά τύπο δωματίου. Χρησιμοποιούμε την στήλη room_type σαν index

# In[45]:


airbnb[['room_type', 'price']].groupby('room_type', as_index=True).median()


# Υπολογισμό διαμέσου τιμής ανά τύπο δωματίου και έτος

# In[46]:


airbnb[['room_type', 'year', 'price']].groupby(['room_type', 'year'], as_index=False).mean()


# Φιλτράρισμα γραμμών με βάση ένα κριτήριο (τιμή <1000) και προσάρτηση σε ένα νέο dataframe

# In[47]:


# get all rows with price < 1000
airbnb_under_1000 = airbnb[airbnb['price'] < 1000]
airbnb_under_1000.head()


# Φιλτράρισμα με πολλαπλά κριτήρια (τιμή <1000 και έτος 2020)

# In[48]:


# get all rows with price < 1000 and year equal to 2020
airbnb_2019_under_1000 = airbnb[(airbnb['price'] < 1000) & (airbnb['year'] == 2020)]
airbnb_2019_under_1000.head()


# Ιστόγραμμα για την στήλη price στον πίνακα airbnb_under_1000

# In[49]:


ax = airbnb_under_1000['price'].plot.hist(bins=40)


# # Βιβλιογραφία
# 
# pandas Tutorial for Beginners, https://www.datacamp.com/tutorial/pandas, Πρόσβαση: 18/05/2022
# 
# Reading and Writing CSV Files in Python, https://realpython.com/python-csv/#reading-csv-files-with-csv, Πρόσβαση: 18/05/2022
# 
# Reading CSV files in Python, https://www.programiz.com/python-programming/reading-csv-files, Πρόσβαση: 18/05/2022
# 
# COVID-19 Coronavirus Pandemic, https://www.kaggle.com/datasets/rinichristy/covid19-coronavirus-pandemic, Πρόσβαση: 18/05/2022
# Pandas User Guide, https://pandas.pydata.org/docs/user_guide/index.html#user-guide, Πρόσβαση: 23/05/2022
# 
# McKinney, W., 2013. Python for data analysis. O’Reilly, Beijing.
# 
# 
