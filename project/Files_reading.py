import pandas as pd
def in_csv_encoding(filepath)->str:
    try :
        pd.read_csv(filepath,encoding='utf-8',header = None,on_bad_lines = "skip")
    except UnicodeDecodeError:
        try:
            pd.read_csv(filepath,encoding='gbk',header = None,on_bad_lines = "skip")
        except Exception as e :
            print(f"{filepath}均不是'utf-8','gbk'编码格式")
            pass
        else:
            return 'gbk'
    return 'utf-8'
def csv_read(filepath,encoding_type:str):
    pd_1 = pd.read_csv(filepath,encoding=encoding_type,header = None,on_bad_lines = "skip")
    index = pd_1.shape[0]
    pd_2 = pd.read_csv(filepath,encoding=encoding_type,header = index,dtype=str,on_bad_lines = "skip")
    return pd_2
if __name__ == '__main__':
    pass
