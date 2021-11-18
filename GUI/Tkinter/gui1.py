import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.createWidgets()

    def createWidgets(self):
        # instanz der class tkinter.Entry erzeugen
        self.nameEntry = tkinter.Entry(self)
        self.nameEntry.pack()  # Element auf die Oberfläche gebracht
        self.name = tkinter.StringVar()
        self.name.get()
        self.nameEntry["textvariable"] = self.name
        self.ok = tkinter.Button(self)
        self.ok["text"] = "OK"
        self.ok["command"] = self.quit
        self.ok.pack(side="right", padx=5, pady=5)
        self.rev = tkinter.Button(self)
        self.rev["text"] = "Umdrehen"
        self.rev["command"] = self.onReverse
        self.rev.pack(padx=5, pady=5)

    def onReverse(self):
        # renverser une chaine de caractere
        self.name.set("".join(reversed(self.name.get())))
        # self.name.set(self.name.get()[::-1]) #renverse la chaine


root = tkinter.Tk()  # Instanz der Klasse tkinter.Tk erzeugt
app = MyApp(root)
app.mainloop()  # Dialog angezeigt
