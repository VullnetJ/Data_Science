# DataFrame with Pandas -> build on top of the NumPy
# Panda Series consist of columns and rows. 
import pandas as pd

# creating data frame. 
df = pd.DataFrame()
# print(df)
"""
Empty DataFrame
Columns: []
Index: []

"""
names = ['John', 'Ela', 'Helga', 'Will']
surnames = ['Doe', 'Smith', 'Mc', 'Helius']
ages = [24, 30, 39, 20]
df = {'first_name': names, 
    'last_name': surnames,
    'ages': ages}
persons = pd.DataFrame(df)
print(persons)

"""
  first_name last_name  ages
0       John       Doe    24
1        Ela     Smith    30
2      Helga        Mc    39
3       Will    Helius    20
"""

# Opening the CVC from the FiveThirtyEight website, 
polls = pd.read_csv('data_science/president_polls.csv')
# polls.head()


"""
 question_id  poll_id  cycle  ...    candidate_name  candidate_party   pct
0         148910    77173   2024  ...         Joe Biden              DEM  45.0
1         148910    77173   2024  ...      Donald Trump              REP  41.0
2         148839    77168   2024  ...         Joe Biden              DEM  45.0
3         148839    77168   2024  ...      Donald Trump              REP  46.0
4         148894    77168   2024  ...     Kamala Harris              DEM  40.0
..           ...      ...    ...  ...               ...              ...   ...
110       142392    74812   2024  ...      Ron DeSantis              REP  25.0
111       142393    74812   2024  ...         Joe Biden              DEM  44.0
112       142393    74812   2024  ...  Nimrata R. Haley              REP  19.0
113       140691    74681   2024  ...         Joe Biden              DEM  46.4
114       140691    74681   2024  ...      Donald Trump              REP  42.2

[115 rows x 38 columns]

"""
# head() specifies the number of rows to return. 
print(polls.head(6))
"""
   question_id  poll_id  cycle  ... candidate_name  candidate_party   pct
0       148910    77173   2024  ...      Joe Biden              DEM  45.0
1       148910    77173   2024  ...   Donald Trump              REP  41.0
2       148839    77168   2024  ...      Joe Biden              DEM  45.0
3       148839    77168   2024  ...   Donald Trump              REP  46.0
4       148894    77168   2024  ...  Kamala Harris              DEM  40.0
5       148894    77168   2024  ...   Ron DeSantis              REP  42.0
"""

# tail is similar to head but returns rows (from the bottom)

print(polls.tail(5))

"""
     question_id  poll_id  cycle  ...    candidate_name  candidate_party   pct
110       142392    74812   2024  ...      Ron DeSantis              REP  25.0
111       142393    74812   2024  ...         Joe Biden              DEM  44.0
112       142393    74812   2024  ...  Nimrata R. Haley              REP  19.0
113       140691    74681   2024  ...         Joe Biden              DEM  46.4
114       140691    74681   2024  ...      Donald Trump              REP  42.2
"""
# shape of the data:
print(polls.describe())

"""
question_id       poll_id   cycle  ...      race_id  candidate_id         pct
count     115.000000    115.000000   115.0  ...   115.000000    115.000000  115.000000
mean   144846.460870  75971.443478  2024.0  ...  8885.826087  17772.017391   42.595652
std      2133.439922    868.229416     0.0  ...    53.336446   1669.591372    7.562690
min    140691.000000  74681.000000  2024.0  ...  8759.000000  16638.000000    5.000000
25%    142946.000000  74998.000000  2024.0  ...  8914.000000  16651.000000   40.000000
50%    144848.000000  75949.000000  2024.0  ...  8914.000000  16661.000000   43.300000
75%    146302.500000  76752.000000  2024.0  ...  8914.000000  19368.000000   47.600000
max    148910.000000  77173.000000  2024.0  ...  8914.000000  28687.000000   55.200000

[8 rows x 14 columns]
"""

# using percentiles to change the quantiles:
print(polls.describe(percentiles=[0.1, 0.9]))

import numpy as np

# in Pandas is object, and in NumPy is np.object
print(polls.describe(include=[np.object]))

"""
        state                        pollster  ... candidate_name candidate_party
count        28                           115  ...            115             115
unique        6                            19  ...             11               3
top     Florida  Redfield & Wilton Strategies  ...      Joe Biden             DEM
freq         16                            16  ...             43              57

"""
print(polls.describe(include=[object]))

"""
            state                    pollster  ... candidate_name candidate_party
count        28                           115  ...            115             115
unique        6                            19  ...             11               3
top     Florida  Redfield & Wilton Strategies  ...      Joe Biden             DEM
freq         16                            16  ...             43              57

[4 rows x 21 columns]
"""


# statistics for all the columns
print(polls.describe(include='all'))

"""
          question_id       poll_id   cycle  ... candidate_name  candidate_party         pct
count      115.000000    115.000000   115.0  ...            115              115  115.000000
unique            NaN           NaN     NaN  ...             11                3         NaN
top               NaN           NaN     NaN  ...      Joe Biden              DEM         NaN
freq              NaN           NaN     NaN  ...             43               57         NaN
mean    144846.460870  75971.443478  2024.0  ...            NaN              NaN   42.595652
std       2133.439922    868.229416     0.0  ...            NaN              NaN    7.562690
min     140691.000000  74681.000000  2024.0  ...            NaN              NaN    5.000000
25%     142946.000000  74998.000000  2024.0  ...            NaN              NaN   40.000000
50%     144848.000000  75949.000000  2024.0  ...            NaN              NaN   43.300000
75%     146302.500000  76752.000000  2024.0  ...            NaN              NaN   47.600000
max     148910.000000  77173.000000  2024.0  ...            NaN              NaN   55.200000

[11 rows x 38 columns]

"""
# Excluding data types, 'string', 'int', 'float'
print(polls.describe(exclude=['string']))

# From the earlier sample:
# accessing a single column
# names
print(persons.first_name)
"""
0     John
1      Ela
2    Helga
3     Will
Name: first_name, dtype: object
"""

# ages
print(persons.ages)
"""
0    24
1    30
2    39
3    20
Name: ages, dtype: int64
"""

print(persons[['first_name', 'ages']])

"""
  first_name  ages
0       John    24
1        Ela    30
2      Helga    39
3       Will    20

"""

students = persons 

print(students[1: 3])
"""
  first_name last_name  ages
1        Ela     Smith    30
2      Helga        Mc    39
"""
