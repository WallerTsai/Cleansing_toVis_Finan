import os
def traverse(filepath:str,list:list = list(),filetypes = None) -> list:
    pre_list = list
    if filetypes is None:
        filetypes=[".csv",".xlsx"] 
    files = os.listdir(filepath)
    for file in files:
        fi_d = os.path.join(filepath, file)
        if os.path.isdir(fi_d):  
            if os.listdir(fi_d) :  
                traverse(fi_d,pre_list,filetypes=filetypes)  
        else:
            file_1 = os.path.join(filepath, fi_d)
            if os.path.getsize(file_1) != 0:  
                others,extension = os.path.splitext(file_1)
                if extension in filetypes:
                    pre_list.append(file_1)
    pre_list.sort() 
    return pre_list
if __name__ == '__main__':
    pass