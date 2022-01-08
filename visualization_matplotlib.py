
# matplotlib has wide-ranging capabilities and is part of SciPy ecosystem. 

import matplotlib.pyplot as plt
import pandas as pd
# Figures are used to graph data and Axes wher ethe points are. 

import numpy as np
x= [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
y = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# to add styles, both can be used either for example -- or can write dashed:
"""
-- dashed
-. dash-dot
: dotted
- solid line
"""
# to add markers: 
"""
different markers to use: 
. point 
, pixel 
o cicle 
| vline
_hline
+ plus
x x 
d thin_diamond
D diamond
* star
h hexagon1
H hexagon2 
v triangle_down 
^ triangle_up 
< triangle_left 
> triangle_right 
1 tree_down
2 tree_up
3 tri_left
4 tree_right
"""
# choosing colors:
"""
g green
b blue
r red 
c cyan
y yellow
k black 
w white 
m magenta
"""
# using format string 's-.g' s marker, -. linestyle, green color
formatted = 's-.g'
#plt.plot(x, y, marker="d", linestyle= 'dashed', color="y")
plt.plot(x, y, formatted)
plt.show()

# using data frames from pandas 

dt = {
    "Graduating": ['2020', '2021', '2022', '2023', '2024', '2025'],
    "student_height": [180, 170, 167, 178, 166, 173]
}
student_height = pd.DataFrame(dt)
plt.title('students height')
plt.legend('Graduating') 
plt.xlabel('Year')
plt.ylabel('Height in CM')
plt.plot('Graduating', 'student_height', data = student_height, marker="d", linestyle= 'dashed', color="y")
plt.show()