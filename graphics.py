import tkinter as tk
from tkinter import messagebox
from  lines import DiscretizationLines
from circle import DiscretizationCircles
from plot import Plot

class App():
    def __init__(self) -> None:
        self.window=tk.Tk()

        self.window.resizable(False,False)
        self.window.title('Discretization algorithms')
        self.window.geometry("700x380+10+10")



        #draw lines
        line_title=tk.Label(self.window,text="Draw line")
        line_title.config(font=("Arial",22))
        line_title.grid(padx=30,pady=10,row=0,column=0)
        line_frame=self.parameters()
        line_frame.grid(padx=5,pady=5,row=1,column=0,sticky=tk.W)

        # draw cicles
        circle_title=tk.Label(self.window,text="Draw circle")
        circle_title.config(font=("Arial",22))
        circle_title.grid(padx=30,pady=10,row=2,column=0,sticky=tk.N)
        circle_frame=self.parametersCircles()
        circle_frame.grid(padx=5,pady=5,row=3,column=0,sticky=tk.W)

        self.window.mainloop()

    def parameters(self):
        frame=tk.Frame(self.window)
        #titles
        t_pos_s_x=tk.Label(frame,text="start px")
        t_pos_s_x.grid(row=0,column=0,padx=30 ,pady=5)
        t_pos_s_x.config(font=("Arial",12))

        t_pos_s_y=tk.Label(frame,text="start py")
        t_pos_s_y.grid(row=0,column=1,padx=30 ,pady=5)
        t_pos_s_y.config(font=("Arial",12))

        t_pos_f_x=tk.Label(frame,text="finish px")
        t_pos_f_x.grid(row=0,column=2,padx=30 ,pady=5)
        t_pos_f_x.config(font=("Arial",12))

        t_pos_f_y=tk.Label(frame,text="finish py")
        t_pos_f_y.grid(row=0,column=3,padx=30 ,pady=5)
        t_pos_f_y.config(font=("Arial",12))

        #text
        text_s_x=tk.Text(frame,height=1,width=7)
        text_s_x.grid(row=1,column=0,padx=30 ,pady=5)

        text_s_y=tk.Text(frame,height=1,width=7)
        text_s_y.grid(row=1,column=1,padx=30 ,pady=5)

        text_f_x=tk.Text(frame,height=1,width=7)
        text_f_x.grid(row=1,column=2,padx=30 ,pady=5)

        text_f_y=tk.Text(frame,height=1,width=7)
        text_f_y.grid(row=1,column=3,padx=30 ,pady=5)

        #list box
        alg=("basic","dda","bresenham")
        list_algorithms=tk.Listbox(frame,listvariable=tk.Variable(value=alg),width=14,height=5)
        list_algorithms.grid(row=1,column=4,padx=10 ,pady=5)

        send=lambda: self.__sendInfoLine(list_algorithms.curselection(),
                                     ((text_s_x.get('1.0','end'),text_s_y.get('1.0','end')),(text_f_x.get('1.0','end'),text_f_y.get('1.0','end')))) #x and y passed for the user      

        button_plot=tk.Button(frame,text="Graph",command=send)
        button_plot.grid(row=1,column=5,padx=10 ,pady=5)

        return frame 

    def __sendInfoLine(self,algorithm:str,points:tuple):
        start_point,finish_point=points
        print(algorithm)
        
        try:
            start_point=(int(start_point[0]),int(start_point[1]))
            finish_point=(int(finish_point[0]),int(finish_point[1]))
            print(start_point)
            print(finish_point)
            points_p:list=[]
            if algorithm==(0,):
                points_p=DiscretizationLines.basicAlgorithm(start_point,finish_point)
            elif algorithm==(1,):
                points_p=DiscretizationLines.ddaAlgorithm(start_point,finish_point)
            else:
                points_p=DiscretizationLines.bresenhamsAlgorithm(start_point,finish_point)
            print(points_p)
            Plot.draw(points_p)
        except:
            messagebox.showerror(title="error",message="fill all fields or type only integers",parent=self.window)

    def parametersCircles(self):
        frame=tk.Frame(self.window)
        #titles
        t_pos_s_x=tk.Label(frame,text="central px")
        t_pos_s_x.grid(row=0,column=0,padx=30 ,pady=5)
        t_pos_s_x.config(font=("Arial",12))

        t_pos_s_y=tk.Label(frame,text="central py")
        t_pos_s_y.grid(row=0,column=1,padx=30 ,pady=5)
        t_pos_s_y.config(font=("Arial",12))

        t_radius=tk.Label(frame,text="radius")
        t_radius.grid(row=0,column=2,padx=30 ,pady=5)
        t_radius.config(font=("Arial",12))

        #text
        text_s_x=tk.Text(frame,height=1,width=7)
        text_s_x.grid(row=1,column=0,padx=30 ,pady=5)

        text_s_y=tk.Text(frame,height=1,width=7)
        text_s_y.grid(row=1,column=1,padx=30 ,pady=5)

        text_r=tk.Text(frame,height=1,width=7)
        text_r.grid(row=1,column=2,padx=30 ,pady=5)

        #list box
        alg=("mid point","bresenham")
        list_algorithms=tk.Listbox(frame,listvariable=tk.Variable(value=alg),width=14,height=5)
        list_algorithms.grid(row=1,column=4,padx=10 ,pady=5)

        send=lambda: self.__sendInfoCircles(list_algorithms.curselection(),
                                     ((text_s_x.get('1.0','end'),text_s_y.get('1.0','end')),text_r.get('1.0','end') )) #x and y passed for the user      

        button_plot=tk.Button(frame,text="Graph",command=send)
        button_plot.grid(row=1,column=5,padx=10 ,pady=5)

        return frame 

    def __sendInfoCircles(self,algorithm:str,points:tuple):
        start_point,radius=points
        print(points)
        
        try:
            radius=int(radius)
            start_point=(int(start_point[0]),int(start_point[1]))
            points_p:list=[]
            if algorithm==(0,):
                points_p=DiscretizationCircles.midPointAlgorithm(start_point[0],start_point[1],radius)
            else:
                points_p=DiscretizationCircles.bresenhamAlgorithm(start_point[0],start_point[1],radius)
            print(points_p)
            Plot.draw(points_p)
        except:
            messagebox.showerror(title="error",message="fill all fields or type only integers",parent=self.window)












