import sys
from tkinter import *
from tkinter.font import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from PIL import ImageTk, Image
from tkinter import messagebox
import time


class Logic():
    def __init__(self, gui):
        #zmienna będące odwołaniem do interfejsu
        self.gui = gui
        #zmienna reprezentująca obraz stylu
        self.styleImage = None
        #zmienna reprezentująca obraz treści
        self.sourceImage = None
        #zmienna reprezentująca obraz wynikowy
        self.outputImage = None
        #typy danych dostepne dla obrazow
        self.fileTypes = [
            ('Wszystkie pliki obrazów','*.jpg;*.jpeg;*.bmp;*.png'),
            ('pliki JPG','*.jpg;*.jpeg'),
            ('pliki BMP','*.bmp'),
            ('pliki PNG','*.png')
        ]

    #funkcja rozpoczęcia przetwarzania
    def startProcessing(self):
        self.gui.isProcessing = not self.gui.isProcessing
        if (self.gui.isProcessing):
            self.gui.startButton.configure(text="Stop",background="orangered")

            # właściwe przetwarzanie - chwilowo tylko przykladowe
            #to tylko efekciarski progress bar xD
            for x in range(1, 101):
                self.gui.progress.step()
                time.sleep(0.01)
                self.gui.root.update_idletasks()

            outputPath = "outputExample.png"
            outputImg = ImageTk.PhotoImage(Image.open(outputPath))

            self.gui.outputImgLabel.configure(image=outputImg)
            self.gui.outputImgLabel.image = outputImg
            self.outputImage = Image.open(outputPath)
            self.gui.startButton.configure(text="Start", background="powderblue")
            self.gui.isProcessing = not self.gui.isProcessing
        else:
            #zatrzymanie przetwarzania
            self.gui.startButton.configure(text="Start",background="powderblue")


    #funkcja ustawienia w danym label podanego obrazu
    def setImage(self,label,image):
        #pobranie szerokosci i wysokosci labela
        labelWidth = label.winfo_width()
        labelHeight = label.winfo_height()
        #dopasowanie rozmiarem obrazu do labela
        resizedImg = image.resize((labelWidth,labelHeight),Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resizedImg)
        #ustawienie obrazu jako tresc labela
        label.configure(image=img)
        label.image = img

    #funkcja wyboru obrazu z okna dialogowego
    def chooseImage(self):
        # wyswietlenie okna dialogowego
        filename = askopenfilename(filetypes=self.fileTypes)
        if not filename:
            return
        # wczytywanie obrazu
        try:
            loadedImg = Image.open(filename)
            return loadedImg
        except IOError:
            messagebox.showerror("Niepoprawny plik!",
                                 "Nie udało się otworzyć tego obrazu. Spróbuj ponownie z użyciem innego pliku.")
            return

    #funkcja zapisu obrazu z okienka output image
    def saveClick(self):
        fileToSave = asksaveasfilename(defaultextension=".png")
        if not fileToSave:
            return
        try:
            self.outputImage.save(fileToSave)
        except ValueError:
            messagebox.showerror("Niepoprawny format pliku!","Wybierz inne zakończenie pliku. Domyślny format to PNG.")
        except AttributeError:
            messagebox.showerror("Brak obrazu wynikowego!", "Spróbuj jeszcze raz, kiedy obraz będzie gotowy.")


    #funkcja ładowania obrazu z stylem
    def styleLoadClick(self):
        originalImg = self.chooseImage()
        if not originalImg:
            return
        self.setImage(self.gui.styleImgLabel,originalImg)
        self.styleImage = originalImg

    #funkcja ładowania obrazu z treścią
    def srcLoadClick(self):
        originalImg = self.chooseImage()
        if not originalImg:
            return
        self.setImage(self.gui.srcImgLabel,originalImg)
        self.sourceImage = originalImg

    # Funkcja służąca do wycentrowania okna
    def center(self):
        self.gui.root.update_idletasks()
        w = self.gui.root.winfo_screenwidth()
        h = self.gui.root.winfo_screenheight()
        size = tuple(int(_) for _ in self.gui.root.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        self.gui.root.geometry("%dx%d+%d+%d" % (size + (x, y)))


