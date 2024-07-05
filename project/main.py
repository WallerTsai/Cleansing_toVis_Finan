import tkinter as tk
from tkinter import filedialog, messagebox,simpledialog
import os
import pandas as pd
import numpy as np
import Files_define as fd
import Files_preparation as fp
import Files_writing as fw
import Clean
import Function_define as fun
import Charts_show as cs
from pandas import DataFrame
from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType
def select_folder():
    global selected_folder_path
    global cleaned_df
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return  
    if not os.path.isdir(folder_path):
        messagebox.showerror("错误", "请选择一个文件夹")
    else:
        selected_folder_path = folder_path
        cleaned_df = save_clean_book(selected_folder_path)
        show_options_button()
def save_clean_book(path:str)->DataFrame:
    global text_list
    text_list =["金额","时间","交易对方","类型","收/支","支付方式","商品"]
    new_df_with_col = pd.DataFrame(columns=text_list)
    for list in fp.traverse(path,filetypes=[".csv"]):
        df = fd.CsvFileReader(list,text_list).needs_label_choose()
        new_df_with_col = pd.concat([new_df_with_col,df],ignore_index=True)
    df_2 = Clean.Cleaning_2(new_df_with_col,text_list)
    fw.csv_write(path,df_2,"记账本")
    return df_2
def show_options():
    global cleaned_df
    if cleaned_df is None:
        messagebox.showerror("错误", "请先选择文件夹")
        return
    global class_1
    class_1 = fun.Function(cleaned_df,text_list)
    options_window = tk.Toplevel()
    options_window.title("选择图表类型")
    button1 = tk.Button(options_window, text="各年收入支出图", command=lambda: function1())
    button1.pack(pady=10)
    button2 = tk.Button(options_window, text="年月柱柱状图", command=lambda: function2())
    button2.pack(pady=10)
    button3 = tk.Button(options_window, text="年月支出类型饼图", command=lambda: function3())
    button3.pack(pady=10)
    button4 = tk.Button(options_window, text="年月支出商品饼图", command=lambda:function4())
    button4.pack(pady=10)
    options_window.mainloop()
def function1():
    df_1 = cleaned_df
    years_list= Clean.find_years(df_1)
    timeline = Timeline({"theme":ThemeType.MACARONS})
    for year in years_list:
        income,outcome = class_1.sum_by_choosed(year)
        list_come = [income,outcome]
        bar1 = Bar()
        bar1.add_xaxis(['收入','支出'])
        bar1.add_yaxis("金额",list_come,label_opts=LabelOpts(position="right"))
        bar1.reversal_axis()
        timeline.add(bar1,year)
    timeline.render("各年收入支出图.html")
def function2():
    year = simpledialog.askinteger("输入年份", "请输入年份")
    if year is None:
        return  
    month = simpledialog.askinteger("输入月份", "请输入月份（可选）", minvalue=1, maxvalue=12)
    if month is not None:
        df_income2,df_outcome2 = class_1.classify_sum_by_choosed(year,month)
        bar_2 = cs.chart_2(df_income2,df_outcome2,year,month)
        bar_2.render(f"{year}年{month}月收入支出柱形图.html")
    else:
        df_income1,df_outcome1 = class_1.classify_sum_by_choosed(year)
        bar_1 = cs.chart_1(df_income1,df_outcome1,year)
        bar_1.render(f"{year}年收入支出柱形图.html")
def function3():
    year = simpledialog.askinteger("输入年份", "请输入年份")
    if year is None:
        return  
    month = simpledialog.askinteger("输入月份", "请输入月份（可选）", minvalue=1, maxvalue=12)
    df_outcome = class_1.sizeAndsum_by_labels(year,month)
    pie_1 = cs.chart_3(df_outcome)
    pie_2 = cs.chart_4(df_outcome)
    if month is not None:
        pie_1.render(f"{year}年{month}月支出类型金额饼图.html")
        pie_2.render(f"{year}年{month}月支出类型次数饼图.html")
    else:
        pie_1.render(f"{year}年支出类型金额饼图.html")
        pie_2.render(f"{year}年支出类型次数饼图.html")
def function4():
    year = simpledialog.askinteger("输入年份", "请输入年份")
    if year is None:
        return  
    month = simpledialog.askinteger("输入月份", "请输入月份（可选）", minvalue=1, maxvalue=12)
    df_outcome = class_1.sizeAndsum_by_products(year,month)
    pie_1 = cs.chart_5(df_outcome)
    pie_2 = cs.chart_6(df_outcome)
    if month is not None:
        pie_1.render(f"{year}年{month}月支出商品金额饼图.html")
        pie_2.render(f"{year}年{month}月支出商品次数饼图.html")
    else:
        pie_1.render(f"{year}年支出商品金额饼图.html")
        pie_2.render(f"{year}年支出商品次数饼图.html")
def show_options_button():
    options_button = tk.Button(root, text="选择功能", command=show_options)
    options_button.grid(row=1, column=0, columnspan=2, pady=10)
def main():
    selected_folder_path = ""
    cleaned_df:DataFrame = None
    text_list = list()
    global root
    root = tk.Tk()
    root.title("选择文件夹")
    path_entry = tk.Entry(root, width=50)
    path_entry.grid(row=0, column=0, padx=10, pady=10)
    browse_button = tk.Button(root, text="浏览", command=select_folder)
    browse_button.grid(row=0, column=1, padx=10, pady=10)
    root.mainloop()
if __name__ == '__main__':
    main()
