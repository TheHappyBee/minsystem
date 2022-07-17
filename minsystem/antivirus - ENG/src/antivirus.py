import os
import tkinter as tk
import shutil
import hashlib
import time
class virus_hash:
     def __init__(self):
          self.hash = hashlib.sha256()
     def find_hash(self, filename):
          with open(filename,"rb") as f:
              bytes = f.read() # read entire file as bytes
              readable_hash = hashlib.sha256(bytes).hexdigest();
              return readable_hash
          
     
          
class antivirus:
     def __init__(self, source, direct, hashes):
          self.virus = source
          self.direct = direct
          self.hashes = hashes
     def scan(self):
          filenames = []
          file_path = []
          for root, directories, files in os.walk(self.direct):
               for filename in files:
                    filepath = os.path.join(root, filename)
                    filenames.append(filename)
                    file_path.append(filepath)
                 
          virus = []
          file = open(self.virus, "r")
          hashes = []
          y = open(self.hashes, "r")
          for line in y:
               hashes.append(line.strip('\n'))
          for line in file:
               virus.append(line.strip('\n'))
          x = 0
          for item in filenames:
               if virus_hash().find_hash(file_path[x]) in hashes:
                    if file_path[x] != "C:\\Users\\Liu Home Desktop\\Desktop\\minsystem\\antivirus - ENG\\safe\\quarintine.found\\" + filenames[x]:
                         return [True, filenames[x], file_path[x]]
                    else:
                         return ["quarintine", filenames[x], file_path[x]]
               else:
                    x += 1
          return [False]
     def remove(self, file):
          os.remove(file)
     def quar(self,dir):
          try:
               shutil.move(dir, r"C:\Users\Liu Home Desktop\Desktop\minsystem\antivirus - ENG\safe\quarintine.found")
          except:
               pass
      
          
class interface:
     def __init__(self, direct):
          self.antivirus = antivirus(r"C:\Users\Liu Home Desktop\Desktop\minsystem\antivirus - ENG\src\data\source.txt",
                                     direct,
                                     r"C:\Users\Liu Home Desktop\Desktop\minsystem\antivirus - ENG\src\data\hashes.txt")
     def main(self):
          root = tk.Tk()
          root.title("antivirus")
          
          def scannerdisplay():
               
               if self.antivirus.scan()[0]==True:
                    win64.destroy()
                    win32 = tk.Tk()
                    win32.title("ALERT")
                    s = len(self.antivirus.scan()[2])
                    win32.geometry(str(s)*10 + "x100")
                    l = tk.Label(win32, text = "A virus has been found at:\n " + self.antivirus.scan()[2] + ",\n" + "start taking actions")
                    l.pack()
                    to_remove = self.antivirus.scan()[2]
                    def inter():
                       self.antivirus.remove(to_remove)
                       win32.destroy()
                    def inter2():
                       self.antivirus.quar(to_remove)
                       win32.destroy()
                    b = tk.Button(win32, text = "remove",command = inter)
                    b.place(x = 160, y =50)
                    b2 = tk.Button(win32, text = "quarintine",command = inter2)
                    b2.place(x = 50, y =50)
                    win32.mainloop()
               elif self.antivirus.scan()[0]==False:
                    win32 = tk.Tk()
                    win32.title("safe")
                    l = tk.Label(win32,text="no threats were found")
                    l.pack()
               else:
                    win32 = tk.Tk()
                    win32.title("in quartine")
                    win32.geometry("300x100")
                    l = tk.Label(win32, text = "the virus is now in quarintine\n"+
                                 "it is closely monitored and you can remove it any time")
                    l.pack()
                    to_remove = self.antivirus.scan()[2]
                    def inter():
                       self.antivirus.remove(to_remove)
                       win32.destroy()
                    b = tk.Button(win32, text ="remove", command = inter)
                    b.place(x = 120, y = 50)
          scan = tk.Button(root, text = "start scanning", command = scannerdisplay)
          scan.pack()
          
          root.mainloop()

interface(r'D:\\songs').main()

          
          
          
               


          
