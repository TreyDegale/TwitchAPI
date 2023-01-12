import tkinter as tk
import subprocess, sys

p = subprocess.run(["powershell.exe", "C:\\twitchAPIExploration.ps1"], stdout=sys.stdout) #run API request

with open(r"onlineStreamsInfo.txt", 'r') as fp:
    num_lines = sum(1 for line in fp) #get number of lines of file, for looping later

f = open("onlineStreamsInfo.txt", "r") #open file with API response

tempList = [] #list to hold current index
nestList = [] #nested list that will contain combined indexs
global index
index = 0
global e

#Go to main function to follow the program from beginning of execution

def caseIndex(acc):
    global index
    if (index == 1 or index == 2): #end of line or "|" reached, the accumulator is now useful information
        tempList.append(acc)
    else:
        tempList.append(acc)
        tempListCopy = tempList.copy()
        nestList.append(tempListCopy)
        tempList.clear()
        index = 0

#responsible for correct index management as well as sectioning information
#c = character, acc = accumulator
def evalChar(c, acc):
    if c == "|" or c == "\n":
        global index
        index += 1
        caseIndex(acc)
        acc = ""
        return acc
    else:
        acc += c
        return acc

def simpleGUI():
    root = tk.Tk()
    canvas = tk.Canvas(root, height = 700, width = 700, bg = "black")
    canvas.pack()
    frame = tk.Frame(root, bg = "#123234")
    frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

    names = []  # create list of names
    btn = []  # creates list to store the buttons ins

    for x in range(len(nestList)):
        names.append(nestList[x][0])

    for i in range(len(names)):  # this says for *counter* in *however many elements there are in the list files*
        # the below line creates a button and stores it in an array we can call later, it will print the value of it's own text by referencing itself from the list that the buttons are stored in
        btn.append(tk.Button(frame, text=names[i], command=lambda c=i: buttonOnClick(btn[c].cget("text"))))
        btn[i].pack()  # this packs the buttons

    Label = tk.Label(frame, bg = "#aa40ff",  text="Streamer Name")
    Label.pack()

    global e
    e = tk.Entry(frame)
    e.pack()
    notButton = tk.Button(frame, text="Enter", command=actOnInput)
    notButton.pack()

    root.mainloop()

def actOnInput():
    global e
    subprocess.call(r"%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe streamlink twitch.tv/{} best".format(e.get()), shell=True)

def buttonOnClick(name):
    subprocess.call(r"%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe streamlink twitch.tv/{} best".format(name), shell=True)

def main():
    acc = ""
    for x in range(num_lines):
        for c in f.readline():
            acc = evalChar(c, acc)
    f.close()
    simpleGUI()

main()
