import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

class Plot():

    @staticmethod
    def __map_points(dimx:int,dimy:int, point:tuple)->tuple:
        px=5+ 
        py=5+
        return (px,py)


    @staticmethod
    def drawLine(points:list):

        max_x,min_x=(max(points,key=lambda w: w[0])[0],min(points,key=lambda w: w[0])[0])
        max_y,min_y=(max(points,key=lambda w: w[1])[1],min(points,key=lambda w: w[1])[1])


        data=np.zeros((max_x-min_x+10,max_y-min_y+10))
        data[1,1]=11
        data[1,2]=12
        data[0,0]=13

        cmap = colors.ListedColormap(['white', 'red'])
        bounds = [1,10,20]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        fig, ax = plt.subplots()
        ax.imshow(data, cmap=cmap, norm=norm)

        plt.show()

Plot.drawLine([(1,1),(1,2),(1,3)])
