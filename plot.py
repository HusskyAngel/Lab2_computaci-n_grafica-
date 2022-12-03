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
        px=x-dimx[1]
        py=y-dimy[1]
        return (px,py)

class Plot():

    @staticmethod
    def draw(points:list):

        max_x,min_x=(max(points,key=lambda w: w[0])[0],min(points,key=lambda w: w[0])[0])
        max_y,min_y=(max(points,key=lambda w: w[1])[1],min(points,key=lambda w: w[1])[1])

        data=np.zeros((max(max_y-min_y+1,1),max(max_x-min_x+1,1)))
        for w in points:#y,x 
            px,py=Utils.map_points((max_x,min_x),(max_y,min_y),w)
            data[py][px]=11
        data=np.flip(data,axis=0)

        cmap = colors.ListedColormap(['red', 'blue'])
        bounds = [0,10,20]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        fig, ax = plt.subplots()
        ax.imshow(data, cmap=cmap, norm=norm)

# draw gridlines
        #ax.grid()
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        plt.show()


