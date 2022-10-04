#!/usr/bin/env python
# coding: utf-8

# # Εργασία 6. Συναρτήσεις

# 1. Ορίστε μια συνάρτηση που δέχεται σαν παράμετρο την ακτίνα και επιστρέφει το εμβαδό ενός κύκλου. Μέσω docstrings περιγράψτε πολύ συνοπτικά την λειτουργία της συνάρτησης.

# In[1]:


import math
def calcArea(r):
    '''Η τρέχουσα συνάρτηση δέχεται σαν όρισμα την ακτίνα ενός κύκλου και επιστρέφει το εμβαδόν του'''
    return(math.pi*r**2)

calcArea(2)


# 2. Ορίστε μια συνάρτηση που θα δέχεται σαν παράμετρο το ΑΦΜ σας και θα επιστρέφει True αν το τελευταίο ψηφίο είναι ζυγός αριθμός και False αν είναι μονός. Ενδεικτικά για την λύση, υπενθυμίζεται ότι πρέπει να εξάγετε το τελευταίο στοιχείο μιας συμβολοσειράς (το ΑΦΜ στην τρέχουσα περίπτωση), να το μετατρέψετε σε ακέραιο και να κάνετε χρήση του τελεστή modulo (υπόλοιπο διαίρεσης).

# In[2]:


def checkAFM(afm):
    
    if not isinstance(afm, str):
        afm=str(afm)
    
    digit= int(afm[-1])
    if (digit % 2) == 0:
        return(True)
    else:
        return(False)
    
checkAFM('109034328')
    
    


# 3. Ορίστε μια συνάρτηση με το όνομα abs_ofNumber η οποία θα δέχεται μια παράμετρο. Η συνάρτηση θα επιστρέφει την απόλυτη τιμή (μέσω της συνάρτησης abs) αν ειναι ακέραιος ή δεκαδικός ή θα επιστρέφει None σε διαφορετική περίπτωση.

# In[3]:


def abs_ofNumber(x):
    if type(x) is int or type(x) is float:
        return(abs(x))
    else:
        return(None)
    


# In[4]:


print(abs_ofNumber(-1.5) )


# In[5]:


print(abs_ofNumber(-15) )


# In[6]:


print(abs_ofNumber("Test") )


# 4. Χρησιμοποιείστε την συνάρτηση sqrt του αρθρώματος math για να υπολογίσετε την τετραγωνική ρίζα ενός αριθμού.

# In[7]:


import math
math.sqrt(144)


# 4. Χρησιμοποιείστε την συνάρτηση sqrt του αρθρώματος math για να υπολογίσετε την τετραγωνική ρίζα ενός αριθμού.

# 5. Ορίστε και καλέστε μια συνάρτηση lambda που θα επιστρέφει τον κύβο, το τετράγωνο και την τετραγωνική ρίζα ενός αριθμού. Υπενθυμίζεται η χρήση των πλειάδων (tuple packing) για τη επιστροφή πολλών τιμών από μια συνάρτηση.

# In[8]:


x = lambda x: (x**3, x**2, x**0.5) 


# In[9]:


cube, square, root = x(2)


# In[10]:


print(cube, square, root,  sep=', ')


# # Εργασία 7. Ανάγνωση & εγγραφή αρχείων, διαχείριση αρχείων και καταλόγων

# 1. Διαβάστε και εκτυπώστε το περιεχόμενο ενός αρχείου κειμένου γραμμή -γραμμή.
# 

# In[11]:


def read_file():
    with open('../docs/exercise7.txt', 'r') as file:
        for line in file:
            print(line, end="")

read_file()


# 2. Γράψτε μια συνάρτηση η οποία θα διαβάζει ένα αρχείο κειμένου και θα εκτυπώνει τις λέξεις πού έχουν μήκος περισσότερους από 4 χαρακτήρες.
# 

# In[12]:


def read_words():
    with open('../docs/exercise7.txt', 'r') as file:
        data = file.read()
        words = data.split()
        for word in words:
            if len(word) > 4:
                print(word, end="\n")

read_words()


# 3. Γράψτε το περιεχόμενο ενός αρχείου σε ένα άλλο αρχείο.

# In[13]:


r_path = '../docs/exercise7.txt'
w_path = '../docs/exercise7_bck.txt'
with open(r_path, 'r') as reader, open(w_path, 'w') as writer:
    lines = reader.readlines()
    writer.writelines(lines)


# 4. Εκτυπώστε μια λίστα με τα αρχεία ενός καταλόγου. Στην συνέχεια εκτυπώστε μια λίστα με τους καταλόγους του.

# In[14]:


import os
os.getcwd()


# In[15]:


# αλλαγή τρέχοντος καταλόγου
os.chdir('../docs')
os.getcwd()


# In[16]:


#  λίστα με τα αρχεία ενός καταλόγου

from pathlib import Path
directory = Path('./')
contents = directory.iterdir()
files = [f.name for f in contents if f.is_file()]
print(files)


# In[17]:


#  λίστα με τους καταλόγους
from pathlib import Path
directory = Path('./')
contents = directory.iterdir()
files = [f.name for f in contents if f.is_dir()]
print(files)


# 5. Γράψτε ένα πρόγραμμα στην python για να διαπιστώσετε αν ένα αρχείο υπάρχει. Αν το αρχείο υπάρχει τότε εκτυπώστε το όνομα αρχείου (filename) και τον κατάλογο στον οποίο βρίσκεται.
# 

# In[18]:


import os

data_file = Path('../docs/COVID-19 Coronavirus.csv')

if data_file.is_file():
    
    filename = os.path.basename(data_file)
    relative_dir = os.path.dirname(data_file)
    absolute_dir = os.path.abspath(relative_dir)
    absolute_file = os.path.abspath(filename)
    
    print(f"Όνομα αρχείου: {filename}", 
          f"Relative Path καταλόγου: {relative_dir}" , 
          f"Absolute Path καταλόγου: {absolute_dir}", 
          f"Absolute Path Αρχείου: {absolute_file}",
          sep="\n")
else:
    print ("Το αρχείο δεν υπάρχει ")


# # Εργασία 8. Πίνακες και διαγράμματα
# 

# 1. Γράψτε ένα πρόγραμμα στην Python που θα διαβάζει ένα αρχείο CSV και θα χρησιμοποιεί σαν διαχωριστικό στηλών τον χαρακτήρα tab.
# 
# Tip: Ο
# χαρακτήρας tab δηλώνεται με συγκεκριμένο τρόπο στην Python (βλ. μάθημα για συμβολοσειρές)

# In[19]:


import csv 

local_file = '../docs/COVID-19 Coronavirus_V3.csv'

with open(local_file, 'r') as file:
    reader = csv.reader(file, delimiter = '\t')
    for row in reader:
        print(row)


# 2. Γράψτε ένα πρόγραμμα στην Python που θα διαβάζει ένα αρχείο CSV σαν λεξικό.

# In[20]:


with open(local_file, 'r') as file:
    csv_file = csv.DictReader(file, delimiter = '\t',quoting=csv.QUOTE_ALL)
    data = [dict(row) for row in csv_file]


# In[21]:


data[0]


# In[22]:


data[1]


# 3. Φτιάξτε ένα λεξικό στην Python και αποθηκεύστε το σαν CSV.

# In[23]:


with open('../docs/cities.csv', mode='w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames= ['ID', 'City', 'Population'],delimiter=',',quoting=csv.QUOTE_ALL)

    writer.writeheader()
    writer.writerow({'ID': 1, 'City': 'Athens', 'Population': '4M'})
    writer.writerow({'ID': 2, 'City': 'Thessaloniki', 'Population': '1M'})
    writer.writerow({'ID': 2, 'City': 'Trikala, Korinthias', 'Population': '500'})


# 4. Διαβάστε με την βιβλιοθήκη Pandas το επισυναπτόμενο αρχείο COVID-19 Coronavirus.csv και
# 

# Εκτυπώστε τα ονόματα των στηλών.

# In[24]:


import pandas as pd

airbnb = pd.read_csv("../docs/COVID-19 Coronavirus.csv")

list(airbnb.columns)


# Υπολογίστε τον μέσο όρο, τον διάμεσο* και την τυπική απόκλιση** για το πεδίο Total Deaths.

# In[25]:


airbnb['Total Deaths'].mean()


# In[26]:


airbnb['Total Deaths'].median()


# In[27]:


airbnb['Total Deaths'].std()


# Φιλτράρετε τα δεδομένα μόνο για την Ελλάδα με βάση το πεδίο Country και αποθηκεύστε το αποτέλεσμα σε έναν νέο dataframe.

# In[28]:


# φιλτράρισμα και προσάρτηση σε μια μεταβλητή με το όνομα greece
greece = airbnb[airbnb['Country'] == 'Greece'] 

# pandas dataframe: εκτύπωση
greece


# # 9. Γεωεπεξεργασία διανυσματικών δεδομένων
# 

# 1. Φτιάξτε μια συνάρτηση με το όνομα createPointGeom() η οποία θα έχει δύο παραμέτρους (x_coord, y_coord).
# 
# Η συνάρτηση θα πρέπει να δημιουργεί και να επιστρέφει ένα shapely Point geometry object.
# 
# Καλέστε την συνάρτηση 3 φορές με διαφορετικά ορίσματα π.χ. createPointGeom(35,45).

# In[29]:


from shapely.geometry import Point

def createPointGeom(x_coord, y_coord):
    pnt = Point((x_coord,y_coord ))
    return(pnt)
    


# In[30]:


createPointGeom(35,45)


# In[31]:


createPointGeom(30,44)


# 2. Φτιάξτε ένα shapely MultiPolygon geometry object. Στην συνέχεια να υπολογίσετε το εμβαδό (Area) για κάθε πολυγωνό του.

# In[32]:


import shapely
coords = [(0, 0), (0, -1), (7.5, -1), [7.5, 0], (0, 0)]
pol1 = shapely.geometry.Polygon(coords)

coords = [(10, 1), (10, -0.5), (8.5, -0.5), [8.5, 0], (10, 1)]
pol2 = shapely.geometry.Polygon(coords)


multipolygon = shapely.geometry.MultiPolygon([pol1, pol2])
multipolygon


# Εμβαδό για όλο multipolygon

# In[33]:


multipolygon.area


# Εμβαδό για κάθε πολύγωνο του multipolygon ξεχωριστα

# In[34]:


multipolygon.geoms[0].area


# In[35]:


multipolygon.geoms[1].area


# Μέσω loop στα polygons του multipolygon

# In[36]:


for i in range(0,len(multipolygon.geoms)):
    print(f"Area for polygon with index {i}: {multipolygon.geoms[i].area}")


# 3. Δημιουργήστε μια συνάρτηση με το ονομα getLength() η οποία θα έχει σαν παράμετρο ένα  LineString ή Polygon -object. Στην συνέχεια θα υπολογίζει το  μήκος της γραμμής αν είναι LineString ή το μήκος του εξωτερικού περιγράμματος (exterior) αν είναι Polygon object. Σε διαφορετική περίπτωση (αν δεν είναι κάτι από τα δύο) τότε εκτυπώστε το μήνυμα: "Απαιτείται αντικείμενο γεωμετρίας τύπου LineString ή  Polygon". Δείξτε την λειτουργία της συνάρτησης με 3 παραδείγματα που αφορούν τις τρείς δυνατές περιπτώσεις.

# In[37]:


multipolygon.geoms[0].geom_type


# In[38]:


pol1.exterior.length


# In[39]:


def getLength(x):
    length=None
    if type(x) is shapely.geometry.polygon.Polygon:
        length = x.exterior.length
        
    elif type(x) is shapely.geometry.polygon.LineString:
        length = x.length
    else:
        print("Απαιτείται αντικείμενο γεωμετρίας τύπου LineString ή Polygon")
        
    return(length)


# In[40]:


getLength(4)


# In[41]:


getLength("Test")


# In[42]:


coords = [(2, 0.5), (1, 1), (-1, 0), (1, 0)]
line1 = shapely.geometry.LineString(coords)
getLength(line1)


# In[43]:


getLength(pol1)


# In[44]:


pnt = Point((10,25 ))
getLength(pnt)


# 4. Κατεβάστε το αρχείο Υπολεκανών των ελληνικών ποταμών (βλ. επισυναπτόμενο)  (Πηγή: geodata.gov.gr). 
# 

# Λήψη αρχείου zip

# In[45]:


from urllib import request # απαραίτητο για την λήψη αρχείων από το διαδίκτυο


remote_url = "https://geodata.gov.gr/dataset/53e01aba-2547-4397-a0c0-cb786524be22/resource/f9bbd81f-92e1-4796-a215-eafd5f84bdb6/download/ypolekanes.zip"

# Define the local filename to save data
local_file = '../docs/ypolekanes.zip'
# Download remote and save locally
request.urlretrieve(remote_url, local_file)


# Αποσυμπίεση zip αρχείου

# In[46]:


from zipfile import ZipFile

with ZipFile(local_file, 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()


# 4.1 Διαβάστε το αρχείο με την βιβλιοθήκη geopandas
# 

# In[47]:


import geopandas as gpd

basins = gpd.read_file("../docs/ypolekanes/ypolekanes.shp")


# 4.2 Σε ένα νέο πεδίο με το όνομα AREA υπολογίστε σε km2 την έκταση του κάθε πολυγώνου
# 

# In[48]:


basins['AREA'] = basins.area*10e-6


# 4.3 Κάντε συγχώνευση των πολυγώνων με βάση το πεδίο DIST_CD και εφαρμόστε την συνάρτηση sum κατά την συγχώνευση.

# In[49]:


basins_dis = basins.dissolve(by='DIST_CD', aggfunc='sum')


# In[50]:


basins_dis.plot()

