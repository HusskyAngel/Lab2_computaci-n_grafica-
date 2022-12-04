class Aux():
    @staticmethod
    def aux(arr,xc,yc,x,y):
        arr.append( (xc+x,yc+y))
        arr.append( (xc-x,yc+y))
        arr.append( (xc+x,yc-y))
        arr.append( (xc-x,yc-y))
        arr.append( (xc+y,yc+x))
        arr.append( (xc-y,yc+x))
        arr.append( (xc+y,yc-x))
        arr.append( (xc-y,yc-x))


class DiscretizationCircles(): 
    @staticmethod 
    def midPointAlgorithm(x1, y1, r):
        """
        x1--> integer
        y1--> integer
        r--> integer
        Return a list of tuples, every tuple is like (x,y) point, where the line will be printed 
        """
        x=r
        y=0
        d=0
        aux_return=[]
        while(x>=y):
            aux_return.append( (x1+x,y1+y ))
            aux_return.append( (x1+y,y1+x ))
            aux_return.append( (x1-y,y1+x ))
            aux_return.append( (x1-x,y1+y ))
            aux_return.append( (x1-x,y1-y ))
            aux_return.append( (x1-y,y1-x ))
            aux_return.append( (x1+y,y1-x ))
            aux_return.append( (x1+x,y1-y ))
            if(d<=0):
                y=y+1
                d=d+2*y+1
            if(d>0):
                x=x-1
                d=d-2*x+1
        return aux_return

    @staticmethod 
    def  bresenhamAlgorithm(xc,yc,r):
            """
            xc--> integer
            yc--> integer
            r--> integer
            Return a list of tuples, every tuple is like (x,y) point, where the line will be printed 
            """

            x=0
            y=r
            d=3-2*r
            aux_return=[]
            while(y>=x):
                Aux.aux(aux_return,xc,yc,x,y)
                x=x+1
                print(x,y,d)
                if(d>0):
                    y=y-1
                    d = d + 4 * (x - y) + 10
                else:
                    d = d + 4 * x + 6
                Aux.aux(aux_return,xc,yc,x,y)
            return aux_return

