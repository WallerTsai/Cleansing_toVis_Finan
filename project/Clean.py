import pandas as pd
import numpy as np
import os
import re
from pandas import DataFrame
from typing import Union,List
in_dict = {
    "时间":["时间","交易时间"],
    "类型":["类型","交易类型","交易分类"],
    "交易对方":["交易对方","交易对象"],
    "商品":["商品","商品说明"],
    "收/支":["收/支","收支"],
    "金额":["金额","金额(元)"],
    "支付方式":["支付方式","收/付款方式"]
           }
def Cleaning_1(df:DataFrame,user_lists:list)->DataFrame :
    columns = df.columns
    columns_list = columns.tolist()
    global Dicts
    Dicts = in_dict
    new_df_with_col = pd.DataFrame(columns=user_lists)
    for key,value in Dicts.items():
        if key in user_lists:
            for list in columns_list:
                if list in value:
                    new_df_with_col[key] = df[list]
    return new_df_with_col
def WeChat_label(df:DataFrame)->DataFrame :
    df["服务方"] = "微信"
    return df
def alipay_label(df:DataFrame)->DataFrame :
    df["服务方"] = "支付宝"
    return df
def other_label(df:DataFrame)->DataFrame :
    df["服务方"] = "其他"
    return df
def clean_amount(value)->float:
    cleaned_value = re.sub(r'[^0-9.]', '', value)
    try:
        cleaned_value = "{:.2f}".format(float(cleaned_value))
    except ValueError:
        cleaned_value = None  
    return float(cleaned_value)
def Cleaning_2(df:DataFrame,user_lists:list)->DataFrame:
    df_1 = df.drop_duplicates(inplace = False)  
    if "金额" in user_lists:
        df_1["金额"] = df_1["金额"].apply(clean_amount) 
    if "时间" in user_lists:
        df_1["时间"] = pd.to_datetime(df_1["时间"])     
        df_1.sort_values(by="时间",inplace = True)      
    df_1.reset_index(drop=True,inplace=True)            
    return df_1
def solution_cash_flow(df:DataFrame) -> None:
    mapping = {'收入': 1, '支出': -1}
    df['收/支'] = df['收/支'].map(mapping).fillna(0).astype(int)
def find_years(df:DataFrame)->list:
    df['时间'] = pd.to_datetime(df['时间'], errors='coerce')
    years = df['时间'].dt.year.dropna().unique()
    years_list = sorted(years.tolist())
    return years_list
def sum_by_month(df:DataFrame,col:Union[str,List[str]])->DataFrame:
     if '时间' not in df.columns or not pd.api.types.is_datetime64_any_dtype(df['时间']):
        raise ValueError("DataFrame must contain a datetime column named '时间'.")
     df['月份'] = df['时间'].dt.month
     new_df = df.groupby('月份')[col].sum()
     return new_df
def sum_by_day(df:DataFrame,col:Union[str,List[str]])->DataFrame:
     if '时间' not in df.columns or not pd.api.types.is_datetime64_any_dtype(df['时间']):
        raise ValueError("DataFrame must contain a datetime column named '时间'.")
     df['日'] = df['时间'].dt.day
     new_df = df.groupby('日')[col].sum()
     return new_df
def filter_data(df, year=None, month=None)->DataFrame:
    if year is not None and not isinstance(year, int):
            raise ValueError("Year should be an integer.")
    if month is not None and (not isinstance(month, int) or month < 1 or month > 12):
            raise ValueError("Month should be an integer between 1 and 12.")
    if year is not None and month is None:
        new_df = df[df['时间'].dt.year == year]
    elif year is not None and month is not None:
        new_df = df[(df['时间'].dt.year == year) & (df['时间'].dt.month == month)]  
    else:
        new_df = df  
    new_df = new_df.reset_index(drop = True)    
    return new_df
def sum_cash_flow(df:DataFrame,col:Union[str,List[str]])->DataFrame:
    if (isinstance(col, list) and not set(col).issubset(df.columns)) or (not isinstance(col, list) and col not in df.columns):
        raise ValueError(f"DataFrame must contain a column or columns named {col}.")
    new_df = df.groupby('收/支')[col].sum()
    return new_df
def calculate_label_with_sum(df, label_column, amount_column = None)->DataFrame:
    if amount_column is not None:
        pivot_df = df.pivot_table(index=label_column, 
                                values=amount_column, 
                                aggfunc={'size', 'sum'}).rename(columns={'size': 'Count', 'sum': 'Total Amount'})
        pivot_df['Percentage'] = (pivot_df['Count'] / pivot_df['Count'].sum()) * 100
        pivot_df['Amount Percentage'] = (pivot_df['Total Amount'] / pivot_df['Total Amount'].sum()) * 100
    else:
        pivot_df = df.pivot_table(index=label_column, aggfunc='size').reset_index(name='Count')
        pivot_df.set_index(label_column,inplace = True)
        pivot_df['Percentage'] = (pivot_df['Count'] / pivot_df['Count'].sum()) * 100
    return pivot_df
if __name__ == '__main__':
    data = {
    '收/支':[1, 1, 0, -1, 0, 1, -1, -1, 0, 0, 1, -1] * 30,  
    '金额': [100, 200, 150, 300, 250, 180, 210, 190, 280, 320, 150, 200] * 30,  
    '收入': [50, 80, 100, 120, 90, 110, 130, 140, 160, 180, 200, 220] * 30,  
    '支出': [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140] * 30  
    }
    df = pd.DataFrame(data)
    result_pivot = calculate_label_with_sum(df, '收/支',"金额")
    print(result_pivot)
    pass
