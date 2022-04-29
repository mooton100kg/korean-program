import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import sub,sys,tkinter.messagebox
from PIL import Image, ImageTk

'''----------------------------------------------------'''
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(size=10)
        self.geometry('+550+300')
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.grid()

        self.frames = {}
        for F in (StartPage, text, file, create,merge):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")
        
        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

'''-----------------------------------------------------'''

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        def close():
            parent.destroy()
            controller.destroy()
            sys.exit()
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.controller = controller
        myfont = tkfont.Font(size=15)
        
        _text = tk.Button(self, text="text",command=lambda: controller.show_frame("text"))
        _file = tk.Button(self, text="file",command=lambda: controller.show_frame("file"))
        _create = tk.Button(self, text="create",command=lambda: controller.show_frame("create"))
        _merge = tk.Button(self, text="merge",command=lambda: controller.show_frame("merge"))
        _close = tk.Button(self, text="close",command=close,bg='red',fg='white')
        name = tk.Label(self, text='Cr: Pukpasut')

        _text['font'] = myfont
        _file['font'] = myfont
        _create['font'] = myfont
        _merge['font'] = myfont
        _close['font'] = myfont

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
                
        _text.grid(row=0,sticky='ewns')
        _file.grid(row=1,sticky='ewns')
        _create.grid(row=2,sticky='ewns')
        _merge.grid(row=3,sticky='ewns')
        _close.grid(row=4,sticky='ewns')
        name.grid(row=5)
    
        
class text(tk.Frame):
    
    def __init__(self, parent, controller):
        def submit():
            first = _text.get('1.0','end')
            sub.text(first)
            ans = tkinter.messagebox.showinfo('','finish')
            if ans == 'ok':
                parent.destroy()
                controller.destroy()
                sys.exit()
                                 
        tk.Frame.__init__(self, parent)
        self.controller = controller
    
        myfont = tkfont.Font(size=10)
        
        _text = tk.Text(self,width=30,height=10)
        _submit = tk.Button(self,text='submit',command = submit,bg='blue',fg='white')
        back = tk.Button(self, text="back",command=lambda: controller.show_frame("StartPage"),bg='red',fg='white')
        
        self.grid_rowconfigure(1, weight=1)
        
        _text.grid(row=0,column=0,columnspan=2)
        _submit.grid(row=1,column=0,sticky='ewsn')
        back.grid(row=1,column=1,sticky='wesn')
                
        _text['font'] = myfont
        _submit['font'] = myfont
        back['font'] = myfont
        
        
class file(tk.Frame):
    
    def __init__(self, parent, controller):
        def submit():
            print(type(_file))
            file = _file.get()
            sub.file(file)
            ans = tkinter.messagebox.showinfo('','finish')
            if ans == 'ok':
                parent.destroy()
                controller.destroy()
                sys.exit()
                    
        tk.Frame.__init__(self, parent)
        self.controller = controller

        myfont = tkfont.Font(size=10)

        image = Image.open('img1.png')
        imag = image.resize((120,120))
        image_ = ImageTk.PhotoImage(imag)
        
        file = tk.Label(self, text='file : ')
        _file = tk.Entry(self,width=25)
        _submit = tk.Button(self,text='submit',command = submit,bg='blue',fg='white')
        back = tk.Button(self, text="back",command=lambda: controller.show_frame("StartPage"),bg='red',fg='white')
        label = tk.Label(self, image=image_)

        label.image = image_
        self.grid_rowconfigure(3, weight=1)
        
        file.grid(row=0,column=0)
        _file.grid(row=0,column=1,sticky='we')
        _submit.grid(row=1,column=0,sticky='wens',columnspan=3)
        back.grid(row=2,column=0,sticky='wesn',columnspan=3)
        label.grid(row=3,columnspan=2)
                
        file['font'] = myfont
        _file['font'] = myfont
        _submit['font'] = myfont
        back['font'] = myfont

class create(tk.Frame):
    
    def __init__(self, parent, controller):
        def submit():
            file = _create.get()
            _write = create2.get('1.0','end')
            sub.create(_write,file)
            ans = tkinter.messagebox.askquestion('','next?')
            if ans == 'no':
                parent.destroy()
                controller.destroy()
                sys.exit()
            else:
                sub.file(file)
                ans = tkinter.messagebox.showinfo('','finish')
                if ans == 'ok':
                    parent.destroy()
                    controller.destroy()
                    sys.exit()   
                                 
        tk.Frame.__init__(self, parent)
        self.controller = controller

        myfont = tkfont.Font(size=10)
        
        _create = tk.Entry(self)
        create2 = tk.Text(self,width=30,height=8)
        _submit2 = tk.Button(self,text='submit',command=submit,bg='blue',fg='white')
        back = tk.Button(self, text="back",command=lambda: controller.show_frame("StartPage"),bg='red',fg='white')
        
        _create.grid(row=0,sticky='we')
        create2.grid(row=1)
        _submit2.grid(row=2,sticky='we')
        back.grid(row=3,column=0,sticky='wesn')
                
        _create['font'] = myfont
        create2['font'] = myfont
        _submit2['font'] = myfont
        back['font'] = myfont

class merge(tk.Frame):
    
    def __init__(self, parent, controller):
        def submit():
            au1 = _audio1.get()
            au2 = _audio2.get()
            ok = tkinter.messagebox.askquestion('',au1+'<<<'+au2+'    correct?')
            if ok == 'yes':
                sub.merge(au1,au2)            
                ans = tkinter.messagebox.showinfo('','finish')
                if ans == 'ok':
                    parent.destroy()
                    controller.destroy()
                    sys.exit()
                                 
        tk.Frame.__init__(self, parent)
        self.controller = controller

        myfont = tkfont.Font(size=10)

        image = Image.open('img2.png')
        imag = image.resize((100,100))
        image_ = ImageTk.PhotoImage(imag)
        
        audi1 = tk.Label(self,text='first : ')
        _audio1 = tk.Entry(self)
        audi2 = tk.Label(self,text='secound : ')
        _audio2 = tk.Entry(self)
        _submit2 = tk.Button(self,text='submit',command=submit,bg='blue',fg='white')
        back = tk.Button(self, text="back",command=lambda: controller.show_frame("StartPage"),bg='red',fg='white')
        label = tk.Label(self, image=image_)

        label.image = image_
        self.grid_rowconfigure(4, weight=1)
        
        audi1.grid(row=0,column=0)
        _audio1.grid(row=0,column=1)
        audi2.grid(row=1,column=0)
        _audio2.grid(row=1,column=1)
        _submit2.grid(row=2,column=0,columnspan=2,sticky='w'+'e')
        back.grid(row=3,column=0,sticky='wesn',columnspan=2)
        label.grid(row=4,columnspan=2)
                
        audi1['font'] = myfont
        _audio1['font'] = myfont
        audi2['font'] = myfont
        _audio2['font'] = myfont
        _submit2['font'] = myfont
        back['font'] = myfont
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
