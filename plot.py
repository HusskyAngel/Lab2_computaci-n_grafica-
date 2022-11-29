import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import lines

class Utils():
    @staticmethod
    def map_points(dimx:tuple,dimy:tuple, point:tuple)->tuple:
        """
        dimx-> tuple(maxx,minx)
        dimy-> tuple(maxy,miny)
        """
        x,y=point
        px=(x-dimx[1])  
        py=dimy[0]-(y-dimy[1])
        return (px,py)

class Plot():

    @staticmethod
    def drawLine(points:list):

        max_x,min_x=(max(points,key=lambda w: w[0])[0],min(points,key=lambda w: w[0])[0])
        max_y,min_y=(max(points,key=lambda w: w[1])[1],min(points,key=lambda w: w[1])[1])


        data=np.zeros((max(max_y-min_y,1),max(max_x-min_x+1,1)))
        print(data.shape)
        #y,x 
        for w in points:
            px,py=Utils.map_points((max_x,min_x),(max_y,min_y),w)
            print("x "+str(px)+", py "+str(py))
            data[py][px]=11
            

        cmap = colors.ListedColormap(['white', 'red'])
        bounds = [1,10,20]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        fig, ax = plt.subplots()
        ax.imshow(data, cmap=cmap, norm=norm)
        ax.set_xticks(np.arange(min_x-5, max_x+5, 1));
        ax.set_yticks(np.arange(min_y-5,max_y+5 , 1));
        ax.invert_yaxis()

        plt.show()

Plot.drawLine([(1,1),(1,2),(1,3)])
