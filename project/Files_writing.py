from pandas import DataFrame
import os
def csv_write(filepath:str, df:DataFrame,folder_name:str) -> None :
    if os.path.isdir(filepath):
        parent_dir = os.path.dirname(filepath)
        new_dir = os.path.join(parent_dir, folder_name)
    else:
        parent_dir = os.path.dirname(filepath)
        new_dir = os.path.join(parent_dir, folder_name)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    new_file_path = os.path.join(new_dir, 'data.csv')
    df.to_csv(new_file_path,index=False,encoding="utf-8")
