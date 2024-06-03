import os
class FileOrganizer:
    def organize(self,path=''):
        if path=='':
            path=os.path.abspath(__file__)
            path="\\".join(path.split("\\")[:-1])
        if not os.path.exists(path):
            raise Exception("Path not Found")
        if not os.access(path,os.W_OK):
            raise Exception("Write Permission denied")
        os.chdir(path)
        files=os.listdir()
        i=0
        while "organized_"+str(i) in files:
            i+=1
        path=f"organized_{i}\\"
        os.mkdir(f"organized_{i}")
        madedir=set()
        for i in files:
            if '.' not in i or i==f"organized_{i}":
                continue
            ext=i.split('.')[-1]
            if ext not in madedir:
                madedir.add(ext)
                os.mkdir(path+f"{ext}_files")
            os.rename(i,path+f"{ext}_files\\{i}")
        return 1
    def organize_specific(self,path='',extensions=['*']):
        if path=='':
            path=os.path.abspath(__file__)
            path="\\".join(path.split("\\")[:-1])
        if not os.path.exists(path):
            raise Exception("Path not Found")
        if not os.access(path,os.W_OK):
            raise Exception("Write Permission denied")
        if extensions==['*']:
            self.organize(path)
            return
        os.chdir(path)
        files=os.listdir()
        i=0
        while "organized_"+str(i) in files:
            i+=1
        path=f"organized_{i}\\"
        os.mkdir(f"organized_{i}")
        madedir=set()
        for i in files:
            if '.' not in i or i==f"organized_{i}":
                continue
            ext=i.split('.')[-1]
            if ext not in extensions:
                continue
            if ext not in madedir:
                madedir.add(ext)
                os.mkdir(path+f"{ext}_files")
            os.rename(i,path+f"{ext}_files\\{i}")
        return 1
    def deorganize(self,path):
        if not os.path.exists(path):
            raise Exception("Path not Found")
        os.chdir(path)
        ph=''
        for i in os.listdir():
            if "organized_" in i:
                ph=i
        if ph=='':
            raise Exception("No files named \'organized_\'")
        for i in os.listdir(f"{ph}"):
            for j in os.listdir(f"{ph}\\{i}"):
                os.rename(f"{ph}\\{i}\\{j}",j)
        return 1


                    
                
