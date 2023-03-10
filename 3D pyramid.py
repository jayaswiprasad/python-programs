vertices = [(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0.5,0.5,1)]

# Draw the pyramid
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 

fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 

ax.scatter3D(vertices[0],vertices[1],vertices[2],color="red") 
ax.scatter3D(vertices[0],vertices[1],vertices[3],color="green") 
ax.scatter3D(vertices[0],vertices[2],vertices[3],color="blue") 
ax.scatter3D(vertices[1],vertices[2],vertices[3],color="yellow") 
ax.scatter3D(vertices[0],vertices[1],vertices[4],color="black") 
ax.scatter3D(vertices[1],vertices[2],vertices[4],color="black") 
ax.scatter3D(vertices[2],vertices[3],vertices[4],color="black") 
ax.scatter3D(vertices[3],vertices[1],vertices[4],color="black") 

plt.show()
