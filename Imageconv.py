import tkinter
from tkinter import filedialog
from tkinter import ttk
from PIL import Image,ImageTk
import os.path
from pathlib import Path

class Image_conv_app():
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.title("Image Conv PCD")
        self.root.geometry("500x500")
        self.root.resizable(False,False)
        self.create_widget()


    def create_widget(self):
        self.img_file_label = tkinter.Label(self.root, text="File to convert:")
        self.img_file_label.grid(row=1, column=0, pady=1, padx=2)
        self.file_name_bar = tkinter.Entry(self.root, width=55)
        self.file_name_bar.grid(row=1, column=1, padx=1, pady=4)
        self.button= tkinter.Button(self.root, text="Browse", width=8, command=self.open_file)
        self.button.grid(row=1, column=2, padx=1, pady=4)

        self.convert_to_label=tkinter.Label(self.root, text="convert to:")
        self.convert_to_label.grid(row=3,column=0,pady=5,padx=2)
        self.n = tkinter.StringVar()
        self.To_filetype = ttk.Combobox(self.root, width=27, textvariable=self.n)
        self.To_filetype['values'] = (".png", ".jpg", '.gif')
        self.To_filetype.grid(row=3, column=1, pady=5, columnspan=2)

        self.canvas = tkinter.Canvas(self.root, width=450, height=350)
        self.image=Image.open("D:\dumac\ImageTester\Testpool\ew file name.png")
        self.image = self.image.resize((450, 350), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)
        self.canvas.image = self.img
        self.canvas.grid(row=4, column=0 ,pady=5,columnspan=3)

        convert_button=tkinter.Button(self.root, text="Convert" , width=5, command=self.convert)
        convert_button.grid(row=5,column=0,pady=5,columnspan=3)


        self.root.mainloop()

    def open_file(self):
        self.file = filedialog.askopenfilename(parent=self.root, title='Choose a file')
        self.file_name_bar.delete(0, "end")
        self.file_name_bar.insert(0,self.file)
        self.image = Image.open(self.file)
        self.image = self.image.resize((450, 350), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)
        self.canvas.image = self.img


        print(self.file)


    def convert(self):
        file_to_be_converted=self.file
        self.selected_folder = filedialog.askdirectory()
        filename = Path(self.file).stem
        to_file_type = self.To_filetype.get()
        #im1 = Image.open(self.file)
        #im1.save(str(self.selected_folder)+"/"+str(filename)+str(to_file_type))



        img = Image.open(file_to_be_converted)
        image_format = img.format.lower()

        if image_format.lower() == "jpeg":
            image_format = "jpg"
        elif image_format.lower() == "ppm":
            image_format = "pgm"
        try:
            if (image_format.lower() == "pgm"):
                img.save(str(self.selected_folder)+"/"+str(filename)+str(to_file_type))

            elif img.mode != 'RGB':
                rgb_img = img.convert('RGB')
                rgb_img.save(str(self.selected_folder)+"/"+str(filename)+str(to_file_type))

            else:
                img.save(str(self.selected_folder)+"/"+str(filename)+str(to_file_type))

        except Exception as e:
            print(e)






app=Image_conv_app()
