import sys
from tkinter import *
from tkinter.font import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
from logic import Logic

class GUI():

    #konstruktor GUI, odpowiada za wszystkie elementy okna
    def __init__(self,master=None):
        #root (Tk) - główne okno aplikacji
        self.root = Tk()

        #ustawienie parametrów dla głównego okna
        self.root.title("Projekt Grupowy - 19@KISI'2018")
        self.root.geometry("1035x770")
        self.root.configure(background="aliceblue")

        #klasa do wykonywania logiki
        self.logic = Logic(self)

        #definiowanie niestandardowych czcionek
        buttonFont = Font(slant=ITALIC,family="Helvetica",size=10)
        labelFont = Font(weight=BOLD,size=10)
        outputLabelFont = Font(weight=BOLD,size=18,family="Arial")

        #zmienna typu boolean mówiąca, czy trwa przetwarzanie
        self.isProcessing = False;

        #definiowanie ramek na elementy
        self.loadingFrame = Frame(self.root,height=310,width=510,bd=5,relief=GROOVE,background="gainsboro")
        self.loadingFrame.place(relx=0.01,rely=0.01)

        self.loadingFrame2 = Frame(self.root,height=310,width=510,bd=5,relief=GROOVE,background="gainsboro")
        self.loadingFrame2.place(relx=0.01,rely=0.4136)

        self.outputFrame = Frame(self.root,height=620,width=505,bd=5,relief=GROOVE,background="gainsboro")
        self.outputFrame.place(relx=0.505,rely=0.01)

        self.optionsFrame = Frame(self.root,height=130,width=1018,bd=5,relief=GROOVE,background="gainsboro")
        self.optionsFrame.place(relx=0.01,rely=0.83)

        #Label zawierający napis "source image" i znajdujący się nad obrazem z treścią
        self.infoLabel1 = Label(self.loadingFrame,text="Source image",background="gainsboro",font=labelFont)
        self.infoLabel1.place(relx=0.0, rely=-0.005, height=40, width=120)

        #Label zawierający napis "style image" i znajdujący się nad obrazem z stylem
        self.infoLabel2 = Label(self.loadingFrame2,text="Style image",background="gainsboro",font=labelFont)
        self.infoLabel2.place(relx=0.0, rely=-0.005, height=40, width=110)

        #Label zawierający napis "output image" i znajdujący się nad obrazem wynikowym
        self.infoLabel3 = Label(self.outputFrame,text="Output image",background="gainsboro",font=outputLabelFont)
        self.infoLabel3.place(relx=0.35, rely=0.1,height=40,width=160)

        #Label zawierający napis "Layer selection" i będący obok wyboru warstw
        self.infoLabel4 = Label(self.optionsFrame,text="Layer selection",background="gainsboro", font=outputLabelFont)
        self.infoLabel4.place(relx=0.015,rely=0.01,height=30,width=200)

        #Label zawierający napis "Progress:" i będący obok paska postępu
        self.infoLabel5 = Label(self.optionsFrame,text="Progress:",background="gainsboro", font=labelFont)
        self.infoLabel5.place(relx=0.6,rely=0.01,height=30,width=110)

        #Labele do wyświetlania obrazów (obrazy wyświetlane są jako ich treść)
        self.srcImgLabel = Label(self.loadingFrame,text="",background="aliceblue",borderwidth=2,relief=SOLID)
        self.srcImgLabel.place(relx=0.22, rely=0.13, height=256, width=272)

        self.styleImgLabel = Label(self.loadingFrame2,text="",background="aliceblue",borderwidt=2,relief=SOLID)
        self.styleImgLabel.place(relx=0.22, rely=0.13, height=256, width=272)

        self.outputImgLabel = Label(self.outputFrame,text="",background="lightskyblue",borderwidth=2,relief=SOLID)
        self.outputImgLabel.place(relx=0.225, rely=0.2, height=256, width=272)

        #pasek postępu przetwarzania
        self.progress = ttk.Progressbar(self.optionsFrame,orient="horizontal",length=290,mode="determinate")
        self.progress.place(relx=0.7,rely=0.05)

        #przyciski używane w interfejsie
        self.srcLoadButton = Button(self.loadingFrame,text="Load image",command=self.logic.srcLoadClick)
        self.srcLoadButton.place(relx=0.78, rely=0.017, height=33,width=100)
        self.srcLoadButton.configure(background="powderblue",font=buttonFont)

        self.styleLoadButton = Button(self.loadingFrame2,text="Load image",command=self.logic.styleLoadClick)
        self.styleLoadButton.place(relx=0.78,rely=0.017,height=33,width=100)
        self.styleLoadButton.configure(background="powderblue",font=buttonFont)

        self.startButton = Button(self.outputFrame,text="Startuj",command=self.logic.startProcessing)
        self.startButton.place(relx=0.4,rely=0.65,height=50,width=100)
        self.startButton.configure(backgroun="powderblue",font=buttonFont)

        self.saveButton = Button(self.outputFrame,text="Save",command=self.logic.saveClick)
        self.saveButton.place(relx=0.77,rely=0.925,height=33,width=100)
        self.saveButton.configure(background="powderblue",font=buttonFont)

        #przyciski odpowiadające za wybór warstw sieci
        self.layerButton64 = Button(self.optionsFrame,text="3x3 conv, 64")
        self.layerButton64.place(relx=0.01,rely=0.28,height=25,width=100)
        self.layerButton64.configure(background="aliceblue")

        self.layerButton64_2 = Button(self.optionsFrame,text="3x3 conv, 64")
        self.layerButton64_2.place(relx=0.01,rely=0.51,height=25,width=100)
        self.layerButton64_2.configure(background="aliceblue")

        self.layerButton128 = Button(self.optionsFrame,text="3x3 conv, 128")
        self.layerButton128.place(relx=0.12, rely=0.28,height=25,width=100)
        self.layerButton128.configure(background="blanchedalmond")

        self.layerButton128_2 = Button(self.optionsFrame,text="3x3 conv, 128")
        self.layerButton128_2.place(relx=0.12,rely=0.51,height=25,width=100)
        self.layerButton128_2.configure(background="blanchedalmond")

        self.layerButton256 = Button(self.optionsFrame,text="3x3 conv, 256")
        self.layerButton256.place(relx=0.23, rely=0.05,height=25,width=100)
        self.layerButton256.configure(background="lavender")

        self.layerButton256_2 = Button(self.optionsFrame,text="3x3 conv, 256")
        self.layerButton256_2.place(relx=0.23, rely=0.28,height=25,width=100)
        self.layerButton256_2.configure(background="lavender")

        self.layerButton256_3 = Button(self.optionsFrame, text="3x3 conv, 256")
        self.layerButton256_3.place(relx=0.23, rely=0.51, height=25, width=100)
        self.layerButton256_3.configure(background="lavender")

        self.layerButton256_4 = Button(self.optionsFrame, text="3x3 conv, 256")
        self.layerButton256_4.place(relx=0.23, rely=0.74, height=25, width=100)
        self.layerButton256_4.configure(background="lavender")

        self.layerButton512 = Button(self.optionsFrame,text="3x3 conv, 512")
        self.layerButton512.place(relx=0.34, rely=0.05,height=25,width=100)
        self.layerButton512.configure(background="mintcream")

        self.layerButton512_2 = Button(self.optionsFrame, text="3x3 conv, 512")
        self.layerButton512_2.place(relx=0.34, rely=0.28, height=25, width=100)
        self.layerButton512_2.configure(background="mintcream")

        self.layerButton512_3 = Button(self.optionsFrame, text="3x3 conv, 512")
        self.layerButton512_3.place(relx=0.34, rely=0.51, height=25, width=100)
        self.layerButton512_3.configure(background="mintcream")

        self.layerButton512_4 = Button(self.optionsFrame, text="3x3 conv, 512")
        self.layerButton512_4.place(relx=0.34, rely=0.74, height=25, width=100)
        self.layerButton512_4.configure(background="mintcream")

        self.layerButton512_5 = Button(self.optionsFrame, text="3x3 conv, 512")
        self.layerButton512_5.place(relx=0.45, rely=0.05, height=25, width=100)
        self.layerButton512_5.configure(background="mistyrose")

        self.layerButton512_6 = Button(self.optionsFrame, text="3x3 conv, 512")
        self.layerButton512_6.place(relx=0.45, rely=0.28, height=25, width=100)
        self.layerButton512_6.configure(background="mistyrose")

        self.layerButton512_7 = Button(self.optionsFrame, text="3x3 conv, 512")
        self.layerButton512_7.place(relx=0.45, rely=0.51, height=25, width=100)
        self.layerButton512_7.configure(background="mistyrose")

        self.layerButton512_8 = Button(self.optionsFrame, text="3x3 conv, 512")
        self.layerButton512_8.place(relx=0.45, rely=0.74, height=25, width=100)
        self.layerButton512_8.configure(background="mistyrose")

        #centrowanie okna
        self.logic.center()
        #główna pętla okna
        self.root.mainloop()

#Kod główny programu, inicjalizujący GUI
guiFrame = GUI()