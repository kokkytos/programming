#!/usr/bin/env python
# coding: utf-8

# # 7. Ανάγνωση & εγγραφή αρχείων, μετονομασία, αναζήτηση, αντιγραφή μετακίνηση αρχείων και καταλογών

# Πριν ξεκινήσουμε την επίδειξη των εντολών για το σημερινό μάθημα, θα πρέπει να εισάγουμε μερικές απαραίτητες βιβλιοθήκες και να ορίσουμε τον τρέχων κατάλογο στη Python:

# In[1]:


import os
import pickle
from pathlib import Path
from datetime import datetime, timezone
import fnmatch
import tempfile
from tempfile import TemporaryFile, TemporaryDirectory
import shutil


# In[2]:


print(os.getcwd()) # εκτύπωση τρέχοντος καταλόγου στην Python



path="./some_directory/"
os.chdir(path) # ορισμός τρέχοντος καταλόγου

print(os.getcwd()) # επιβεβαίωση του τρέχοντος καταλόγου στην Python 


# ## Ανάγνωση & εγγραφή αρχείων

# Μπορούμε να ανοίξουμε ένα αρχείο με την μέθοδο open, να δούμε μερικές ιδιότητες του και να το κλείσουμε

# In[3]:


myfile=open("foo.txt", "r")
print ("Name of the file: ", myfile.name)
print ("Closed or not : ", myfile.closed)
print ("Opening mode : ", myfile.mode)
myfile.close()
print(myfile.closed)


# Με την μέθοδο _write()_ σε ένα object ανοικτού αρχείου (TextIOWrapper object πιο συγκεκριμένα)  μπορούμε να γράψουμε σε αυτό περιεχόμενο. Κατά το _open_ δίνουμε σαν παράμετρους το όνομα του αρχείου και την επιλογή προσπέλασης "_w_" (όπου w= εγγραφή, r= ανάγνωση, a=προσθήκη). Το _w_ μας επιτρέπει την δυνατότητα εγγραφής.
# Πάντα πρέπει να κλείνουμε το ανοικτό αρχείο με την μέθοδο _close()_.

# In[4]:


# Open a file
fo = open("foo.txt", "w") # Σημαντική παράμετρος το "w"
fo.write( "Ένα ταξίδι χιλίων χιλιομέτρων αρχίζει με ένα βήμα.\nΛάο Τσε, 6ος αιώνας π.Χ., Κινέζος φιλόσοφος")
# Close opend file
fo.close()


# Επιβεβαιώνουμε ότι όντως έγινε η εγγραφή ξαναδιαβάζοντας το αρχείο με την μέθοδο _read()_ η οποία διαβάζει το συνολικό περιεχόμενο από το αρχείο.

# In[5]:


# Open a file
fo = open("foo.txt", "r") # Σημαντική παράμετρος το "w"

text = fo.read()
print (text)

# Close opened file
fo.close()


# Επειδή υπάρχει ο κίνδυνος να καλέσουμε την μέθοδο close() σε ένα ανοικτό αρχείο, μπορούμε εναλλακτικά να ανοίξουμε ένα αρχείο με το *with*. Σε αυτήν την περίπτωση το αρχείο κλείνει αυτόματα όταν ολοκληρωθεί το μπλοκ εντολών εντός του with.

# In[6]:


with open('foo.txt', 'r') as reader:
    print(reader.read())


# Η μέθοδος read() δέχεται σαν όρισμα τον αριθμό των bytes που θα επιστρέψει.

# In[7]:


with open('foo.txt', 'r') as fo:
    text = fo.read(5)
    print (text)

    text = fo.read(10)
    print (text)


# Με την χρήση της μεθόδου _readlines()_ προσαρτούμε κάθε γραμμή που υπάρχει στο αρχείο σε μια λίστα. Όμως ο χαρακτήρας που ορίζει την νέα σειρά (\n) δεν αγνοείται από την ανάγνωση.

# In[8]:


with open('dog_breeds.txt', 'r') as reader:
    # Note: readlines doesn't trim the line endings
    dog_breeds = reader.readlines()
    dog_breeds = [line.rstrip() for line in dog_breeds] # μπορούμε να αφαιρέσουμ τα new line characters με αυτόν τον τρόπο
    print(dog_breeds)


# Με την χρήση του _with_ μπορούμε να εγγράψουμε δεδομένα κιόλας. Σημαντική παράμετρος το '_w_' κατά το _open()_ και η μέθοδος _write()_.

# In[9]:


with open('dog_breeds_reversed.txt', 'w') as writer:
    # Alternatively you could use
    # writer.writelines(reversed(dog_breeds))

    # Write the dog breeds to the file in reversed order
    for breed in reversed(dog_breeds):
        writer.write(breed)


# Με το όρισμα 'a' (append) κατά το άνοιγμα ενός αρχείου μπορούμε να εγγράψουμε σε ένα αρχείο χωρίς να διαγραφεί το προηγούμενο περιεχόμενο.

# In[10]:


with open('dog_breeds.txt', 'a') as a_writer:
    a_writer.write('Beagle\n')


# In[11]:


with open('dog_breeds.txt', 'r') as reader:
    print(reader.read())


# Μπορούμε να χρησιμοποιήσουμε παράλληλα δύο αρχείa με τις αντίστοιχες παραμέτρους ανάγνωσης, ή εγγραφής ή προσθήκης μέσω του with ως εξής:

# In[12]:


d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))


# Ανάγνωση αρχείου ανά γραμμή μέσω βρόγχου _while_ και της μεθόδου _readline()_:

# In[13]:


with open('dog_breeds.txt', 'r') as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(line, end='')
        line = reader.readline()


# Μπορούμε να διαβάσουμε γραμμή - γραμμή το περιεχόμενο ενός αρχείου μέσω ενός loop στην λίστα γραμμών που μας προσφέρει η μέθοδος readlines()

# In[14]:


with open('dog_breeds.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')


# Και για περισσότερο ευανάγνωστο κώδικα η Python μας δίνει την δυνατότητα να κάνουμε loop μέσω του reader object

# In[15]:


with open('dog_breeds.txt', 'r') as reader:
    # Read and print the entire file line by line
    for line in reader:
        print(line, end='') # use end='' το avoid new line after each print statement


# ## Σειριοποίηση (pickle)

# Στα προηγούμενα παραδείγματα διαβάσαμε ή γράψαμε συμβολοσειρές σε ένα αρχειο. Όμως, μέσω της σειριοποίησης μπορούμε να αποθηκεύσουμε σε ένα binary αρχείο τα αντικείμενα της python με τις ιδιότητές τους. Όχι μόνον σαν απλές συμβολοσειρές. Στο παρακάτω κομμάτι κώδικα θα αποθηκεύσουμε μία λίστα και μια μεταβλήτή σε ένα αρχείο με την βοήθεια της βιβλιοθήκης _pickle_.

# In[16]:


mylist=['one', 2 , 'tree']
pi=3.14
with open('pickle.txt',  'ab') as pickle_writer:
    pickle.dump(mylist, pickle_writer)  
    pickle.dump(pi, pickle_writer)      


# Αφού έχουμε αποθηκεύσει τα σχετικά object σε ένα αρχείο, μπορούμε σε μεταγενέστερα στάδια του κώδικα να τα ανακαλέσουμε αυτούσια μέσω της ανάγνωσης αυτού του αρχείου.

# In[17]:


with open('pickle.txt',  'rb') as pickle_read:
    pickle.load(pickle_read)
    print(pi)
    print(mylist)


# ## Ανάκτηση περιεχομένων φακέλου

# Μέσω της μεθόδου _os.scandir()_ μπορούμε να λάβουμε μια λίστα με τα αρχεία και τους φακέλους σε ένα κατάλογο.

# In[18]:


entries = os.scandir('./')
for entry in entries:
    print(entry.name)


# In[19]:


# εναλλακτικά
os.listdir('./')


# In[20]:


# Εναλλακτικά μέσω πρόταση with
with os.scandir('./') as entries:
    for entry in entries:
        print(entry.name)


# To ίδιο μπορούμε να κάνουμε με την μέθοδο _iterdir()_ σε ένα Path object από την βιβλιοθήκη _pathlib_

# In[21]:


entries = Path('./')
for entry in entries.iterdir():
    print(entry.name)


# Η μέθοδος is_file() μας επιτρέπει να τεστάρουμε αν ένα αντικείμενο τύπου Path είναι αρχείο. 

# In[22]:


basepath = Path('./')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(item.name)


# Επιπλέον για ένα path μπορούμε να λάβουμε την απόλυτη μορφή του (absolute path) μέσω της συνάρτησης _os.path.abspath()_  
# τον κατάλογο στον οποίο βρίσκεται (μέσω της συνάρτησης _dirname()_) και το όνομα του αρχείου (με _os.path.basename()_)

# In[23]:


path="./foo.txt" # relative path
abspath = os.path.abspath(path) # absolute path
print(abspath)
print(os.path.dirname(abspath)) # όνομα καταλόγου που βρίσκεται το αρχείο
print(os.path.basename(abspath)) # όνομα αρχείου (filename)


# Η μέθοδος is_dir() μας επιτρέπει να τεστάρουμε αν ένα αντικείμενο τύπου Path είναι φάκελος (directory). 

# In[24]:


# List all subdirectory using pathlib
basepath = Path('.')
for entry in basepath.iterdir():
    if entry.is_dir():
        print(entry.name)


# Με την μέθοδο _stat()_ μπορούμε να δούμε χρήσιμες λεπτομέρειες για ένα αρχείο και να ανακτήσουμε δεδομένα όπως το μέγεθος του, το όνομά του και η τελευταία ημερομηνία/ώρα τροποποίησης (δίνεται σε seconds απο την 1/1/1970)

# In[25]:



current_dir = Path('./') #ορίστε έναν φάκελο. Στην συγκεκριμένη περίπτωση ορίζεται ο τρέχον κατάλογος.
for path in current_dir.iterdir():
    info = path.stat()
    
    size=info.st_size
    modification_time=datetime.fromtimestamp(info.st_mtime, tz=timezone.utc) # st_time=  the number of seconds passed since 1st January 1970 (epoch)
    name=path.name
    
    print("\nΌνομα αρχείου:", name)
    print("\tΜέγεθος: ",size) # το μέγεθος του αρχείου σε bytes
    print("\tΗμερομηνία τελευταίας τροποποίησης", modification_time)


# Μέσω του Path μπορούμε να φτιάξουμε και διαδρομές προς ένα κατάλογο του δίσκου μας όπως περιγράφεται παρακάτω:

# In[26]:


# δημιουργία paths 

in_file_1 = Path.cwd() / "in" / "input.xlsx"
out_file_1 = Path.cwd() / "out" / "output.xlsx"

print(in_file_1)
print(out_file_1)

# ή

in_file_2 = Path.cwd().joinpath("in").joinpath("input.xlsx")
out_file_2 = Path.cwd().joinpath("out").joinpath("output.xlsx")


# ## Δημιουργία καταλόγων

# Στόχος είναι η δημιουργία νέων καταλόγων (directories) στο σύστημα αρχείων του υπολογιστή μας.
# 
# Πριν ξεκινήσουμε, επιβεβαιώνουμε για μια ακόμη φορά τον τρέχοντα κατάλογο

# In[27]:


path = Path.cwd() # pathlib object, εναλλακτικό του os.getcwd()

print(str(path)) # print σαν συμβολοσειρά


# Μπορούμε να δημιουργήσουμε καταλόγους με την μέθοδο _mkdir()_

# In[28]:


# create directory
try:
    p = Path('example_directory/') # ορισμός absolute ή relative Path
    p.mkdir() # δημιουργία καταλόγου
except FileExistsError:
    print(f"Ο κατάλογος {str(p)} υπάρχει ήδη")


# In[29]:


p.mkdir(exist_ok=True) # δημιουργία καταλόγου, αγνοεί την δημιουργία φακέλου αν αυτός υπάρχει ήδη


# In[30]:


p = Path('2018/10/05') # δημιουργία καταλόγου 05 και όλων των γονικών (parent) καταλόγων
p.mkdir(parents=True,exist_ok=True) 


# Είτε να αναζητήσουμε αρχεία και καταλόγους που περιλαμβάνουν συγκεκριμένους χαρακτήρες στο ονομά τους

# In[31]:


content = os.listdir('./')
print(content)

print("Εύρεση αρχείων με καταληξη txt\n")

for file_name in content:
    if fnmatch.fnmatch(file_name, '*.txt'):
        print(file_name)


# Εύρεση όλων των αρχείων στον τρέχοντα κατάλογο που το όνομά τους έχει την παρακάτω μορφή:
# 
#     data_*_backup.txt
#     
# το αστεράκι (*) αντιπροσωπεύει οποιοδήποτε αριθμό χαρακτήρων μέσα στο όνομα.
#     
# 

# In[32]:


for filename in os.listdir('./'):
    if fnmatch.fnmatch(filename, 'data_*_backup.txt'):
        print(filename)


# Εναλλακτικά με την χρήση της μεθόδου glob()

# In[33]:


p = Path('.')
for name in p.glob('data_*_backup.txt'):
    print(name)


# In[34]:


p = Path('.')
for name in p.glob('*[0-9]*backup.txt'):
    print(name)


# Οι παραπάνω αναζητήσεις αφορούσαν το περιεχόμενο μόνο στον τρέχοντα κατάλογο και όχι ταυτόχρονα και στους υποκαταλόγους (child) που υπάρχουν μέσα σε αυτόν. Για να αναζητήσουμε διαδοχικά και σε αυτούς τους καταλόγους χρησιμοποιούμε το παρακάτω πρόθεμα πριν από το κριτήριο αναζήτησης **/

# In[35]:


# Append "**/" before the search term in pattern to recursively search this directory 
p = Path('.')
for name in p.glob('**/*.py'):
    print(name)


# In[36]:


# αναζήτηση για ότι περιέχει f και 1 στο filename

p = Path('.')
for name in p.glob('**/f*1*'):
    print(name)


# Για να ανατρέξουμε διαδοχικά σε όλους του φακέλους ενός καταλόγου χρησιμοποιούμε την μέθοδo os.walk

# In[37]:


# walk
# Walking a directory tree and printing the names of the directories and files
for dirpath, dirnames, files in os.walk('.', topdown=False):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)


# ## Προσωρινά αρχεία και κατάλογοι

# Με την python μπορούμε να δημιουργήσουμε προσωρινά αρχεία και καταλόγους οι οποιού παύουν να υπάρχουν μετά την εκτέλεση του κώδικα. Αυτό γίνεται με την βοήθεια του αρθρώματος (module) tempfile και της συνάρτησης  TemporaryFile() και TemporaryDirectory()

# In[38]:


from tempfile import TemporaryFile

# temporary files
with TemporaryFile('w+t') as fp: # άνοιγμα προσωρινού αρχείου για εγγραφή
    fp.write('Hello universe!')
    fp.seek(0)
    print(fp.read())
# File is now closed and removed


# In[39]:


with TemporaryDirectory() as tmpdir:
    print('Created temporary directory ', tmpdir)
    print(tmpdir)
    print(os.path.exists(tmpdir))


# Directory contents have been removed


# Αφού έχουμε εξέλθει από τον block κώδικα _with_ το προσωρινό directory παύει να υπάρχει

# In[40]:



os.path.exists(tmpdir)


# ## Διαγραφή αρχείων και φακέλων

# Με την μέθοδο unlink() μπορούμε να διαγράψουμε έναν **άδειο** κατάλογο ή ένα αρχείο.

# In[41]:


data_file = Path('./data_04.txt')

if data_file.is_file():
    print ("Το αρχείο υπάρχει και θα διαγραφεί")
    data_file.unlink()
else:
    print ("Το αρχείο δεν υπάρχει")


# Για την διαγραφή άδειου φακέλου καλούμε την μέθοδο rmdir() στο Path object.

# In[42]:



my_dir = Path('./tmp')

if my_dir.is_dir():
    print ("Το directory υπάρχει και θα διαγραφεί")
    my_dir.rmdir()
else:
    print ("Το directory δεν υπάρχει")


# Αν θέλουμε να διαγράψουμε έναν κατάλογο ο οποίος περιλαμβάνει και περιεχόμενα τότε χρησιμοποιούμε η συνάρτηση _rmtree()_ από την βιβλιοθήκη shutil.

# In[43]:


# διαγραφή φακέλου με περιεχόμενα

dest = Path('./tmp2')
shutil.rmtree(dest, ignore_errors=True)


# ## Αντιγραφή αρχείων και φακέλων

# Ταυτόχρονα μπορούμε να αντιγράψουμε αρχεία με την συνάρτηση copy() πάλι από το άρθρωμα shutil.

# In[44]:


# Αντιγραφή αρχείου

src = 'admin.py'
dst = 'admin2.py'
shutil.copy(src, dst)


# ή ολόκληρους καταλόγους μέσω της συνάρτησης copytree() πάλι από το ίδιο άρθρωμα.

# In[45]:


try:
    shutil.copytree('sub_dir', 'sub_dir3')
except:
    print("Σφάλμα κατά την αντιγραφη")


# ## Μετακίνηση

# ή ακόμα και να μετακινήσουμε αρχεία και καταλόγους με την συναρτηση move()

# In[46]:


try:
    shutil.move('data_04.txt', 'sub_dir/data_04.txt')
except FileNotFoundError:
    print("File does not exist")


# In[47]:


# μετακίνηση αρχείου και μάλιστα με μετονομασία κατά την μετακίνηση data_04.txt -> data_05.txt

try:
    shutil.move('sub_dir/data_04.txt', 'data_05.txt' )
except FileNotFoundError:
    print("File does not exist")


# In[48]:


# μετακίνηση φακέλου

try:
    shutil.move('tmp2', 'tmp/tmp2') 
except FileNotFoundError:
    print("Directory does not exist")


# In[49]:


# επιστροφή στην θέση του 
try:
    shutil.move('tmp/tmp2','tmp2')
except FileNotFoundError:
    print("Directory does not exist")


# ## Μετονομασία
# Με την χρήση της μεθόδου rename() σε έναν Path αντικείμενο μπορούμε να το μετονομάσουμε.

# In[50]:


# αρχείου
data_file = Path('data_01.txt')
data_file.rename('data.txt')


# In[51]:


# ξανά όπως ήταν
data_file = Path('data.txt')
data_file.rename('data_01.txt')


# ## Βιβλιογραφία

# - Aγγελιδάκης, Ν., 2015. Εισαγωγή στον προγραμματισμό με την Python. Αγγελιδάκης, Ηράκλειο.
# - Working With Files in Python, https://realpython.com/read-write-files-python/, Πρόσβαση: 13/05/2022
# - Reading and Writing Files in Python, https://realpython.com/read-write-files-python, Πρόσβαση: 13/05/2022
