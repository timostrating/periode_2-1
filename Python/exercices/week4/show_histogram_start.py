from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename

def show_result():
    analyze_file(filename.get())

def analyze_file(filename):
    try:
        infile = open(filename, "r")
    
        # your code
        counts = {0 : 3, 1 : 7, 2 : 5}

        # display a histogram for counts
        show_histogram(counts)
    except IOError:
        tkinter.messagebox.showwarning("Analyze File", "File " + filename + " does not exist") 

def open_file(): 
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)
        
def show_histogram(counts): 
    numberOfBars = len(counts)
    width = int(canvas["width"])
    height = int(canvas["height"])
    heightBar = 0.75 * height
    widthBar = width - 20
    maxCounts = max(counts)
    
    for i in range(numberOfBars):
        canvas.create_rectangle(i * widthBar / numberOfBars + 10, height - 20 - counts[i] * heightBar / maxCounts, (i + 1) * widthBar / numberOfBars + 10, height - 20)
        canvas.create_text(i * widthBar / numberOfBars + 10 + 0.5 * widthBar / numberOfBars, height - 10, text = chr(i + ord('a')))
    
window = Tk()
window.title("Words Frequency Histogram")

frame1 = Frame(window)
frame1.pack()
canvas = Canvas(frame1, width = 500, height = 200)
canvas.pack()

frame2 = Frame(window)
frame2.pack()

Label(frame2, text = "Enter a filename: ").pack(side = LEFT)
filename = StringVar()
Entry(frame2, width = 40, textvariable = filename).pack(side = LEFT)
Button(frame2, text = "Browse", command = open_file).pack(side = LEFT)
Button(frame2, text = "Show Result", command = show_result).pack(side = LEFT)

window.mainloop()
