#!/usr/bin/env python
# coding: utf-8

# # 9. Γεωεπεξεργασία διανυσματικών δεδομένων

# Ο χώρος και οι γεωμετρικές δομές του μπορούν να αναπαρασταθούν μέσω διανυσματικών δεδομένων (Vector).
# Οι τρείς βασικές δομές δεδομένων είναι:
# - Τα σημεία
# - Οι γραμμές
# - Τα πολύγωνα

# <div>
# <img src="Lesson_8/vector.png" width="600"/>
# </div>

# Επιπλέον αυτά τα γεωμετρικά δεδομένα συνοδεύονται και απο περιγραφικά δεδομένα που αφορούν τις ιδιότητες ή τα χαρακτηριστικά αυτών των δεδομένων.

# <div>
# <img src="Lesson_8/spatial-attribute-tables.png" width="600"/>
# </div>

# Στα Σ.Γ.Π. ο πιο συνηθισμένος τύπος αρχείων αποθήκευσης αυτών των δεδομένων είναι το shapefile. 
# Πλέον έχουν αναπτυχθεί και άλλοι τύποι όπως geojson, geopackage και χωρικές βάσεις (geodatabases) όπως η Postgresql/Postgis.

# Ο προσδιορισμός της γεωγραφικής θέσης στην υδρόγειο γίνεται μέσω ενός ζεύγους γεωγραφικών συντεταγμένων.
# Κάθε σημείο στον χώρο προσδιορίζεται γεωγραφικά από το γεωγραφικό μήκος (λ) και το γεωγραφικό πλάτος (φ).
# 

# <div>
# <img src="Lesson_8/coords.jpg" width="500"/>
# </div>

# Για να αποδοθεί η τρισδιάστατη υδρόγειος σφαίρα σε ένα δυσδιάστατο σύστημα αναφορά χρησιμοποιείται ένα προβολικό σύστημα.

# <div>
# <img src="Lesson_8/437-mapping-projection-types.png" width="600"/>
# </div>

# Κάθε προβολικό σύστημα της σφαίρας στο επίπεδο εισάγει μια σειρά παραμορφώσεων που αφορά το σχήμα των γεωμετρικών δομών, την κλίμακα, την έκταση και τις αποστάσεις. Ανάλογα το προβολικό σύστημα κάποιες από τις παραπάνω παραμορφώσεις εμφανίζονται σε μεγάλο βαθμό και άλλες όχι.
# Οπότε ανάλογα το είδος της έρευνας ο ερευνητής οφείλει να γνωρίζειπαραμορφώσεις εισάγει η κάθε προβολή και ανάλογα να επιλέγει την προβολή με τα λιγότερα σφάλματα.

# ## Python βιβλιοθήκες για διανυσματικά δεδομένα

# Για την ανάγνωση, εγγραφή, επεξεργασία διανυσματικών δεδομένων στην Python έχουν καθιερωθεί μια σειρά βιβλιοθηκών.
# Η αρχαιότερη και βασική βιβλιοθήκη είναι η [GDAL/OGR](https://gdal.org/). Επειδή η βιβλιοθήκη δεν είναι ιδιαίτερα συμβατή σε σχέση με τον τρόπο συγγραφής της Python και επιρρεπής σε σφάλματα έχουν αναπτυχθεί πιο σύγχρονες βιβλιοθήκες όπως η βιβλιοθήκη [Fiona] που είναι ιδιαίτερα χρήσιμη για την ανάγνωση/εγγραφή διανυσματικών δεδομένων [Fiona](https://github.com/Toblerity/Fiona) και η βιβλιοθήκη [Shapely](https://github.com/shapely/shapely) η οποία χρησιμοποιείται για την επεξεργασία και ανάλυση.

# ## Η βιβλιοθήκη Shapely

# ### shapely from WKT
# 
# Μπορούμε να δημιουργήσουμε αντικείμενα shapely που αναπαριστούν σημεία ή γραμμές ή πολύγωνα μέσω WKT. Η γλώσσα (https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)[WKT] είναι μια ειδική διάλεκτος για την περιγραφή διανυσματικών αντικειμένων. Εισάγουμε τις απαραίτητες υπο-βιβλιοθήκες (geometry και wkt) από την βιβλιοθήκη shapely. 

# In[1]:


import shapely.geometry
import shapely.wkt


# #### Πολύγωνα

# Καλούμε την μέθοδο *shapely.wkt.loads()* για να δημιουργήσουμε shapely objects από wkt

# In[2]:


pol1 = shapely.wkt.loads("POLYGON ((0 0, 0 -1, 7.5 -1, 7.5 0, 0 0))")


# In[3]:


pol1


# Η εκτύπωση του shapely αντικειμένου επιστρέφει μία περιγραφή σε μορφή WKT. 

# In[4]:


print(pol1)


# Εκτύπωση του τύπου του αντικειμένου pol1

# In[5]:


type(pol1)


# In[6]:


pol2 = shapely.wkt.loads("POLYGON ((0 1, 1 0, 2 0.5, 3 0, 4 0, 5 0.5, 6 -0.5, 7 -0.5, 7 1, 0 1))")
print(pol2)


# In[7]:


pol2


# Δημιουργία MultiPolygon shapely object από αντίστοιχη συλλογή πολυγώνων MULTIPOLYGON

# In[8]:


pol3 = shapely.wkt.loads("""
MULTIPOLYGON
(((40 40, 20 45, 45 30, 40 40)),
((20 35, 10 30, 10 10, 30 5, 45 20, 20 35), (30 20, 20 15, 20 25, 30 20)))
""")


# In[9]:


type(pol3)


# In[10]:


pol3


# In[11]:


type(pol3)


# #### Σημεία

# In[12]:


pnt1 = shapely.wkt.loads("""
POINT (30 10)
""")


# In[13]:


pnt1


# Συλλογή σημείων

# In[14]:


pnt2 = shapely.wkt.loads("""
MULTIPOINT(0 0,1 1)
""")


# In[15]:


pnt2


# #### Γραμμές

# In[16]:


line1 =shapely.wkt.loads("""
LINESTRING(1.5 2.45,3.21 4)
""")

line1


# Συλλογή γραμμών

# In[17]:


line2 =shapely.wkt.loads("""
MULTILINESTRING((0 0,-1 -2,-3 -4, -3 -8),(2 3,3 4,6 7))
""")

line2


# ### Shapely μέσω συναρτήσεων  

# In[18]:


from shapely.geometry import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon


# Κάθε συνάρτηση λαμβάνει διαφορετικά ορίσματα ανάλογα με την συνάρτηση.
# 
# Στην συνέχεια ακολουθεί η δημιουργία ενός αντικειμένου shapely γεωμετρία σημείου.

# In[19]:


pnt1 = shapely.geometry.Point((2, 0.5))
pnt1


# Για την δημιουργία συλλογής σημείων `multipoint` δίνουμε σαν όρισμα στην συνάρτηση *[shapely.geometry.MultiPoint](https://shapely.readthedocs.io/en/stable/manual.html#collections-of-points)* μία λίστα από πλειάδες (tuples). Η κάθε πλειάδα `(x,y)`αντιστοιχεί στις συντεταγμένες ενός σημείου.

# In[20]:


coords = [(2, 0.5), (1, 1), (-1, 0), (1, 0)]
pnt2 = shapely.geometry.MultiPoint(coords)
pnt2


# Για την δημιουργία γραμμών χρησιμοποιείται πάλι μία λίστα από tuples που περιγράφουν τις κορυφές της γραμμής. Στο παρακάτω παράδειγμα χρησιμοποιούμαι την προηγούμενη πλειάδα αλλά πλέον χρησιμοποιούμε την μέθοδο *shapely.geometry.LineString* για την δημιουργία γραμμής και όχι την μέθοδο *hapely.geometry.MultiPoint* που δημιουργεί συλλογές σημείων.

# In[21]:


line1 = shapely.geometry.LineString(coords)
line1


# Κατασκεύη γραμμής από Point Objects:

# In[22]:


p1 = shapely.wkt.loads("POINT (0 0)")
p2 = shapely.wkt.loads("POINT (1 1)")
p3 = shapely.wkt.loads("POINT (2 -1)")
p4 = shapely.wkt.loads("POINT (2.5 2)")
p5 = shapely.wkt.loads("POINT (1 -1)")

shapely.geometry.LineString([p1, p2, p3, p4, p5])


# Αντίστοιχα μπορούμε να δημιουργήσουμε συλλογές γραμμών. 
# 
# Δημιουργούμε ξεχωριστά αντικείμενα γραμμών shapely και στην συνέχεια καλούμε την συνάρτηση *shapely.geometry.MultiLineString* όπου ορίζουμε σαν όρισμα μια λίστα με τις μεμονωμένες γραμμές.

# In[23]:


l1 = shapely.geometry.LineString([(2, 0.5), (1, 1), (-1, 0), (1, -1)])
l2 = shapely.geometry.LineString([(-2, 1), (2, -0.5), (3, 1)])
line2 = shapely.geometry.MultiLineString([l1, l2])
line2


# Αντίστοιχα δημιουργούμε πολυγωνικά αντικείμενα  μέσω μια λίστας με πλειάδες σημείων που χρησιμοποιείται σαν όρισμα στην συνάρτηση *shapely.geometry.Polygon*

# In[24]:


coords = [(0, 0), (0, -1), (7.5, -1), [7.5, 0], (0, 0)]
shapely.geometry.Polygon(coords)


# Αν θέλουμε μπορούμε να περάσουμε μία δεύτερη λίστα η οποία περιλαμβανει επιμέρους λίστες με πλειάδες σημείων τα οποία περιγράφουν τρύπες μέσα στο πολύγωνο.

# In[25]:


coords_exterior = [(0, 0), (0, -1), (7.5, -1), [7.5, 0], (0, 0)]
coords_interiors = [[(0.4, -0.3), (5, -0.3), (5, -0.7), (0.4, -0.7), (0.4, -0.7)]]
shapely.geometry.Polygon(coords_exterior, coords_interiors)


# Με την συνάρτηση *shapely.geometry.MultiPolygon* δημιουργούμε αντίστοιχα συλλογές πολυγώνων από μεμονωμένα αντικείμενα shapely.geometry.polygon.Polygon

# In[26]:


multipolygon1 = shapely.geometry.MultiPolygon([pol2, pol3])
multipolygon1


# In[27]:


print(multipolygon1)


# Σύμφωνα με τις προδιαγραφές [simple features](https://en.wikipedia.org/wiki/Simple_Features) το παραπάνω object δεν είναι έγκυρο γιατί ένα πολύγωνο τέμνει ένα άλλο σε άπειρο αριθμό σημείων. Μπορούμε να ελέγξουμε την εγκυρότητα ενός αντικειμένου με την κλήση τις ιδιότητας *is_valid*. Επίσης κατά την οπτικοποίηση στο προηγούμενο βήμα του αντικειμένου multipolygon1 αυτό εμφανίζεται με κόκκινο (αντί για πράσινο). Ένδειξη ότι δεν ειναι valid.

# In[28]:


multipolygon1.is_valid


# Ταυτόχρονα μπορούμε να φτιάξουμε σύνθετες συλλογές από επιμέρους αντικείμενα shapely.

# In[29]:


geo_collection = shapely.geometry.GeometryCollection([multipolygon1,line2,pnt1])


# In[30]:


geo_collection


# ### Shapely μέσω shape
# 

# Μπορούμε να δημιουργήσουμε αντικείμενα shapely μέσω της συνάρτησης *shapely.geometry.shape* η οποία δέχεται σαν όρισμα ένα λεξικό μορφής [GEOJSON](https://en.wikipedia.org/wiki/GeoJSON) το οποίο πρέπει να έχει τις εξής δύο ιδιότητες.
# 
# * Την ιδιότητα `"type"` που περιγράφει τον τύπο γεωμετρίας
# * Την ιδιότητα  `"coordinates"` που περιγράφει τις γεωμετρίες και τις συντεταγμένες τους σαν λίστες ή πλειάδες.

# In[31]:


d = {"type": "Point", "coordinates": (0, 1)}
shapely.geometry.shape(d)


# Δημιουργία αντικειμένου MultiPolygon μέσω GEOJSON λεξικού:

# In[32]:


d = {
  "type": "MultiPolygon",
  "coordinates": [
    [
      [[40, 40], [20, 45], [45, 30], [40, 40]]
    ],
    [
      [[20, 35], [10, 30], [10, 10], [30, 5], [45, 20], 
      [20, 35]], 
      [[30, 20], [20, 15], [20, 25], [30, 20]]
    ]
  ]
}
pol3 = shapely.geometry.shape(d)
pol3


# ## Γεωμετρικός τύπος δεδομένων

# H ιδιότητα `.geom_type` ενός αντικειμένου shapely περιγράφει τον γεωμετρικό τύπο της:

# In[33]:


pol1.geom_type


# In[34]:


line1.geom_type


# geo_collection.geom_type

# ## Συντεταγμένες

# Για να ανακτήσουμε τις συντεταγμένες ενός shapely αντικειμένου καλούμε με διαφορετικό τρόπο τις ανάλογες συναρτήσεις ανάλογα την πολυπλοκότητα του κάθε τύπου.

# Για ένα Point object καλούμε άμεσα την ιδιότητα coords η οποία επιστρέφει ένα *shapely.coords.CoordinateSequence* object.

# In[35]:


pnt1.coords


# Μπορούμε να λάβουμε ως λίστα τις πλειάδες συντεταγμένων που το απαρτίζουν

# In[36]:


list(pnt1.coords)


# Αντίστοιχα για γραμμή

# In[37]:


list(line1.coords)


# Για να ελέγξουμε σε ένα αντικείμενο συλλογών γεωμετρίας (MultiPoint, MultiPolygon κτλ) πόσες επιμέρους γεωμετρίες περιλαμβάνει:

# In[38]:


len(line2.geoms)


# Για να λάβουμε το πρώτο αντικείμενο γεωμετρίας:

# In[39]:


line2.geoms[0]


# In[40]:


type(line2.geoms[0])


# In[41]:


line2.geoms[0].geom_type


# Και λαμβάνουμε τις συντεταγμένες της πρώτης γεωμετρίας:

# In[42]:


list(line2.geoms[0].coords)


# ή της δεύτερης

# In[43]:


list(line2.geoms[1].coords)


# Για τα πολύγωνα ακολουθούμε διαφορετική προσέγγιση. Ένα πολύγωνο αποτελεί από το εξωτερικό περίγραμμα (exterior) ή και ένα ή περισσότερα περιγράμματα εσωτερικών τρυπών (interiors). Κατά συνέπεια έχουμε συντεταγμένες που περιγράφουν το κάθε περίγραμμα.

# Το εξωτερικό περίγραμμα του pol1 αντικειμένου:

# In[44]:


pol1.exterior


# Και οι συντεταγμένες του:

# In[45]:


list(pol1.exterior.coords)


# Το pol1 όμως δεν έχει εσωτερικές τρύπες γι αυτό και το παρακάτω επιστρέφει μηδέν.

# In[46]:


len(pol1.interiors)


# Έστω το παρακάτω MultiPolygon object που δημιουργήσαμε σε προηγούμενο στάδιο.

# pol3

# Περιλαμβάνει δύο ξεχωριστά γεωμετρικά αντικείμενα:

# In[47]:


len(pol3.geoms)


# Ας πάρουμε το πρώτο:

# In[48]:


pol3.geoms[0]


# Δεν περιλαμβάνει καμία τρύπα στο εσωτερικό του. Ας πάρουμε τις συντεταγμένες από το περίγραμμά του (exterior)

# In[49]:


pol3.geoms[0].exterior.coords


# Και ας τις επιστρέψουμε σαν λίστα πλειάδων από ζεύγη της μορφής `(x,y)`

# In[50]:


list(pol3.geoms[0].exterior.coords)


# Ας δοκιμάσουμε το δεύτερο αντικείμενο γεωμετρίας. Ας το δούμε:

# In[51]:


pol3.geoms[1]


# Λαμβάνουμε τις συντεταγμένες του εξωτερικού περιγράμματος:

# In[52]:


list(pol3.geoms[1].exterior.coords)


# Ας δούμε πόσες τρύπες έχει στο εσωτερικό του:

# In[53]:


len(pol3.geoms[1].interiors)


# Παίρνουμε το περίγραμμα της τρύπας

# In[54]:


pol3.geoms[1].interiors[0]


# Και τις συντεταγμένες της

# In[55]:


list(pol3.geoms[1].interiors[0].coords)


# ### Ιδιότητες αντικειμένων

# #### Υπολογισμός ορίων (bounds)

# In[56]:


geo_collection


# In[57]:


geo_collection.bounds


# In[58]:


shapely.geometry.box(*geo_collection.bounds)


# In[59]:


line1


# In[60]:


line1.bounds


# In[61]:


pnt1


# In[62]:


pnt1.bounds


# In[63]:


list(pnt1.coords)


# #### Υπολογισμός μήκους γραμμής

# In[64]:


line1.length


# In[65]:


line2.geoms[0].length


# #### Υπολογισμός εμβαδού

# In[66]:


pol1.area


# In[67]:


pol2.area


# ### Νέες γεωμετρίες

# #### Κεντροειδές πολυγώνου (centroid)

# In[68]:


pol2


# In[69]:


pol2.centroid


# In[70]:


shapely.geometry.GeometryCollection([pol2, pol2.centroid])


# #### Περιμετρική ζώνη (buffer)

# In[71]:


pnt1.buffer(5)


# In[72]:


shapely.geometry.GeometryCollection([pnt1,pnt1.buffer(5)])


# In[73]:


pol1.buffer(5)


# In[74]:


shapely.geometry.GeometryCollection([pnt1,pnt1.buffer(5)])


# #### Convex hull

# In[75]:


pol3


# In[76]:


pol3.convex_hull


# ## Σχέσεις μεταξύ αντικειμένων

# In[77]:


shapely.geometry.GeometryCollection([pol1,pol3])


# In[78]:


pol1.intersects(pol3)


# In[79]:


pol1.intersects(pol2)


# In[80]:


shapely.geometry.GeometryCollection([pol1,pol2])


# ## Γεωμετρικές πράξεις

# In[81]:


x = shapely.geometry.Point((0, 0)).buffer(1)
y = shapely.geometry.Point((1, 0)).buffer(1)
shapely.geometry.GeometryCollection([x, y])


# In[82]:


x.intersection(y)


# In[83]:


x.difference(y)


# In[84]:


x.union(y)


# In[85]:


pol1.union(pol2)


# Υπολογισμός απόστασης ανάμεσα σε δύο αντικείμενα

# In[86]:


shapely.geometry.GeometryCollection([pol1, pol3])


# In[87]:


pol1.distance(pol3)


# In[88]:


pol3.distance(pol1) 


# In[89]:


import pyproj

from shapely.geometry import Point
from shapely.ops import transform

wgs84_pt = Point(39.35858398397631, 22.932070043920394)

wgs84 = pyproj.CRS('EPSG:4326')
greek_grid = pyproj.CRS('EPSG:2100')

project = pyproj.Transformer.from_crs(wgs84, greek_grid, always_xy=True).transform
projected_point = transform(project, wgs84_pt)


# In[90]:


print(projected_point)


# In[ ]:





# In[91]:


import folium

coords = list(wgs84_pt.coords)[0]

#Create the map
my_map = folium.Map(location = coords, zoom_start = 13)

# Add marker
folium.Marker(coords, popup = 'Volos').add_to(my_map)

#Display the map
my_map


# ## Η βιβλιοθήκη Geopandas
# 
# Μέχρι τώρα είδαμε πως μπορούμε να διαχειριζόμαστε γεωμετρικά δεδομένα με την βιβλιοθήκη shapely.
# 
# Όμως τα γεωγραφικά δεδομένα δεν περιλαμβάνουν μόνο της γεωγραφική πληροφορία και την γεωμετρική τους δομή αλλά συνοδεύονται από μια σειρά περιγραφικών δεδομένων.
# 
# Η βιβλιοθήκη [geopandas](https://geopandas.org/) είναι μια βιβλιοθήκη της Python η οποία υποστηρίζει την ανάγνωση, επεξεργασία, ανάλυση και εγγραφή γεωγραφικών και παράλληλα περιγραφικών δεδομένων. Αποτελεί επέκταση της βιβλιοθήκης [pandas](https://pandas.pydata.org/) και "κληρονομεί" τα χαρακτηριστικά και τις δυνατότητές της.
# 
# Στην υφιστάμενη δομή της pandas, η geopandas υποστηρίζει την γεωμετρία με την προσθήκη μιας νέας στήλης και το γεωγραφικό σύστημα αναφοράς.

# <div>
# <img src="pandas-data-structure.svg" width="500"/>
# </div>

# <div>
# <img src="Lesson_8/dataframe.svg" width="500"/>
# </div>

# Εισάγουμε την βιβλιοθήκη με τον παρακάτω τρόπο

# In[92]:


import geopandas as gpd


# Για να διαβάσουμε ένα αρχείο shapefile χρησιμοποιούμε την συνάρτηση *gpd.read_file*. Το αντικείμενο που προκύπτει είναι τύπου *geopandas.geodataframe.GeoDataFrame*

# In[93]:


# Import shapefile using geopandas
dhmoi = gpd.read_file("Lesson_8/spatial_data/dhmoi.gpkg")

type(dhmoi)


# Η στήλη της γεωμετρίας ονομάζεται προκαθορισμένα geometry και είναι αντικείμενο *geopandas.geoseries.GeoSeries* που περιλαμβάνει αντικείμενα shapely.

# In[94]:


type(dhmoi["geometry"])


# Με την μέθοδο *geom_type* μπορούμε να δούμε τον γεωμετρικό τύπο κάθε εγγραφής.

# In[95]:


dhmoi.geom_type


# Ας δούμε τις αρχικές εγγραφές του αρχείου

# In[96]:


dhmoi.head()


# In[97]:


dhmoi.plot();


# Χαρτογραφική απόδοση σε διαδραστικό χάρτη

# In[98]:


dhmoi.explore(legend=False)


# Εκτύπωση λεπτομερειών για το γεωγραφικό σύστημα αναφοράς το οποίο όπως φαίνεται παρακάτω είναι το ΕΓΣΑ '87 (EPSG:2100)

# In[99]:


dhmoi.crs


# Μπορούμε να μετασχηματίσουμε τα δεδομένα σε ένα διαφορετικό προβολικό σύστημα με κλήση της μεθόδου *to_crs*

# In[100]:


dhmoi_wgs84 = dhmoi.to_crs(4326)
dhmoi_wgs84.crs


# In[101]:


dhmoi.geom_type


# Εκτύπωση των γεωγραφικών ορίων του αρχείου oikismoi που είναι στο σύστημα αναφορά ΕΓΣΑ '87.

# In[102]:


dhmoi.total_bounds


# Εκτύπωση των γεωγραφικών ορίων του αρχείου oikismoi που είναι στο σύστημα αναφορά WGS'84.

# In[103]:


dhmoi_wgs84.total_bounds


# Η μέθοδος *shape* μας επιστρέφει τον πλήθος των γραμμών (325) και των στηλών (15).

# In[104]:


dhmoi.shape


# Μπορούμε να εγγράψουμε ένα Geopandas Dataframe 

# In[105]:


dhmoi.to_file("Lesson_8/dhmoi.geojson", driver="GeoJSON")


# In[106]:


dhmoi.sort_values(by='PopTot01', ascending=False)


# Ορισμός του index στην στήλη *"CodeELSTAT"*

# In[107]:


dhmoi = dhmoi.set_index("CodeELSTAT")


# Υπολογισμός έκτασης (σε $km^2$) σε μία νέα στήλη με το όνομα area

# In[108]:


dhmoi["area"] = dhmoi.area*10e-6


# In[109]:


dhmoi


# Υπολογισμός του centroid κάθε δήμου σε μια νέα στήλη (centroid)

# In[110]:


dhmoi['centroid'] = dhmoi.centroid


# In[111]:


type(dhmoi['centroid'])


# Χαρτογραφική απόδοση του δείκτη ανεργίας (στήλη UnemrT01)  ανά δήμο

# In[112]:


dhmoi.plot("UnemrT01", legend=True)


# In[113]:


dhmoi.plot("Income01", scheme='quantiles', cmap='YlOrRd',  legend=True, figsize=(12, 10))


# Μπορούμε να οπτικοποιήσουμε διαφορετική στήλη τύπου *geopandas.geoseries.GeoSeries* αφού πρώτα την ορίσουμε με την μέθοδο *set_geometry*.

# In[114]:


dhmoi = dhmoi.set_geometry("centroid")
dhmoi.plot("UnemrT01", legend=True)


# Ορισμός περιμετρικής ζώνης διαμέτρου 20χλμ γύρω από κάθε centroid.

# In[115]:


dhmoi = dhmoi.set_geometry("centroid") # ορισμός default γεωμετρίας η στήλη centroid
dhmoi["buffered"] = dhmoi.buffer(20000) #εκτέλεση περιμετρικών ζωνών

dhmoi = dhmoi.set_geometry("buffered") # ορισμός default γεωμετρίας η στήλη buffered
dhmoi.plot(legend=True) # οπτικοποίηση


# Ξανα ορίζουμε σαν προκαθορισμένη στήλη γεωμετρία την στήλη *geometry*.

# In[116]:


dhmoi = dhmoi.set_geometry("geometry")


# Μπορούμε να φιλτράρουμε γραμμές και στήλες όπως και στην pandas χρησιμοποιώντας το index και το όνομα στήλης:

# In[117]:


lesvos = dhmoi.loc["5301", "geometry"]


# In[118]:


lesvos


# In[119]:


type(lesvos)


# Η παραπάνω διαδικασία επιλογής επέστρεψε ένα shapely MultiPolygon object όπως φαίνεται.
# 

# In[120]:


nomoi = dhmoi.dissolve(by='Perif')


# In[121]:


nomoi.plot()


# In[122]:


nomoi = dhmoi.dissolve(by='Perif', aggfunc='mean')


# In[123]:


nomoi.plot(column = 'Income01', scheme='quantiles', cmap='YlOrRd');


# ##  Βιβλιογραφία:
# 
# - Kalogirou S., 2020, Local Correlation, Spatial Inequalities, Geographically Weighted Regression and Other Tools (R package)
# - GeoPandas, https://geopandas.org/, Πρόσβαση: 29/05/2022
# - Prapas I., Analyze Geospatial Data in Python: GeoPandas and Shapely, https://www.learndatasci.com/tutorials/geospatial-data-python-geopandas-shapely/, Πρόσβαση: 29/05/2022
# - Dorman M., 2022, VECTOR LAYERS, Geometries (shapely), https://geobgu.xyz/py/shapely.html, Πρόσβαση: 29/05/2022
# - Wasser, Leah, Korinek, Nathan, & Palomino, Jenny. (2021). earthlab/earth-analytics-intermediate-earth-data-science-textbook: one more license fix (1.0.4) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.5571001
