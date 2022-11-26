
class DiscretizationLines():

    @staticmethod 
    def basicAlgorithm(start_point:tuple, finish_point:tuple)-> list:
        """
        start_point--> tuple(x,y)
        finish_point--> tuple(x,y)
        Return a list of tuples, every tuple is like (x,y) point, where the line will be printed 
        """
        start_x,start_y=start_point
        finish_x,finish_y=finish_point
        slope=(finish_y-start_y)/(finish_x-start_x)
        line_ecuation=lambda r:(slope*r)-(slope*finish_x)-finish_y 

        assert(type(start_x)==int)
        assert(type(finish_x)==int)
        assert(type(start_y)==int)
        assert(type(finish_y)==int)
       
        aux_return=[start_point]

        if start_x > finish_x:
            for x in range(start_x+1,finish_x):    
               aux_return.append((x,round(line_ecuation(x)))) 
        else:
            for x in range(start_x-1,finish_x,-1): 
               aux_return.append((x,round(line_ecuation(x)))) 
        aux_return.append(finish_point)    
            
        return aux_return

    @staticmethod
    def ddaAlgorithm(start_point:tuple, finish_point:tuple)-> list:
        """
        start_point--> tuple(x,y)
        finish_point--> tuple(x,y)
        Return a list of tuples, every tuple is like (x,y) point, where the line will be printed 
        """
        assert(type(start_point[0])==int)
        assert(type(start_point[1])==int)
        assert(type(finish_point[0])==int)
        assert(type(finish_point[1])==int)

        dx=finish_point[0]-start_point[0]
        dy=finish_point[1]-start_point[1]
        steps=abs(dx) if abs(dx) >abs(dy) else abs(dy) 

        xinc=dx/steps
        yinc=dy/steps

        aux_return=[start_point]

        x_count,y_count=start_point
        for x in range(steps):
            x_count+=xinc 
            y_count+=yinc
            aux_return.append((x_count,y_count))
        aux_return.append(finish_point)

        return aux_return

    @staticmethod
    def bresenhamsAlgorithm(start_point:tuple, finish_point:tuple)-> list:
        """
        start_point--> tuple(x,y)
        finish_point--> tuple(x,y)
        Return a list of tuples, every tuple is like (x,y) point, where the line will be printed 
        """
        dx=finish_point[0]-start_point[0]
        dy=finish_point[1]-start_point[1]

        pk=2*dy-dx 

        aux_return=[start_point]
        x_count=start_point[0]
        y_count=start_point[1]
        it=0
        while (x_count,y_count)!=finish_point and  it!=(dx-1): 
            if pk<0:
                pk+=2*dy
                x_count+=pk
                y_count+=pk
            else: 
                pk+=2*dy -2*dx
                x_count+=pk
                y_count+=pk
            it+=1
            aux_return.append((x_count,y_count))
        aux_return.append(finish_point)
        return aux_return






