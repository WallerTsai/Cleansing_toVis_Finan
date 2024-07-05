import pandas as pd
from pandas import DataFrame,Series
from pyecharts.charts import Bar,Pie
from pyecharts import options as opts
def chart_1(pd_income:Series,pd_outcome:Series,year:int,path=None)->Bar:
    months_list = list(range(1,13))
    pd_income = pd_income.reindex(months_list).fillna(int(0))
    pd_outcome = pd_outcome.reindex(months_list).fillna(int(0))
    list_3 = pd_income.values.tolist()
    list_4 = pd_outcome.values.tolist()
    bar1 = Bar()
    bar1.add_xaxis(months_list)
    bar1.add_yaxis("收入",list_3,label_opts=opts.LabelOpts(position="top"))
    bar1.add_yaxis("支出",list_4,label_opts=opts.LabelOpts(position="top"))
    bar1.set_global_opts(title_opts=opts.TitleOpts(title=f"{year} 收入支出图"))
    return bar1
def chart_2(pd_income:Series,pd_outcome:Series,year:int,month:int,path=None)->Bar:
    list_1 = pd_income.index.tolist()
    list_2 = pd_outcome.index.tolist()
    union_list = set(list_1).union(set(list_2))
    pd_income = pd_income.reindex(union_list).fillna(int(0))
    pd_outcome = pd_outcome.reindex(union_list).fillna(int(0))
    list_3 = pd_income.values.tolist()
    list_4 = pd_outcome.values.tolist()
    bar1 = Bar()
    bar1.add_xaxis(union_list)
    bar1.add_yaxis("收入",list_3,label_opts=opts.LabelOpts(position="top",is_show=False))
    bar1.add_yaxis("支出",list_4,label_opts=opts.LabelOpts(position="top",is_show=False))
    bar1.set_global_opts(title_opts=opts.TitleOpts(title=f"{year}年{month}月收入支出图"),datazoom_opts=opts.DataZoomOpts(type_="slider"))
    return bar1
def chart_3(df:DataFrame,path = None)->Pie:
    list_1 = df.index.tolist()
    list_2 = df["Total Amount"].tolist()
    pie1 = (
        Pie()
        .add("",[list(z) for z in zip(list_1,list_2)])
        .set_global_opts(title_opts=opts.TitleOpts(title="支出金额占比"),
                         legend_opts=opts.LegendOpts(orient="vertical",pos_right=True)
                         )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c} {d}%"))
    )
    return pie1
def chart_4(df:DataFrame,path = None)->Pie:
    list_1 = df.index.tolist()
    list_2 = df["Count"].tolist()
    pie1 = (
        Pie()
        .add("",[list(z) for z in zip(list_1,list_2)])
        .set_global_opts(title_opts=opts.TitleOpts(title="支出次数占比"),
                         legend_opts=opts.LegendOpts(orient="vertical",pos_right=True)
                         )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c} {d}%"))
    )
    return pie1
def chart_5(df:DataFrame,path = None)->Pie:
    list_1 = df.index.tolist()
    list_2 = df["Total Amount"].tolist()
    pie1 = (
        Pie()
        .add("",[list(z) for z in zip(list_1,list_2)],center=["30%","50%"],radius=["90%","100%"])
        .set_global_opts(title_opts=opts.TitleOpts(title="支出金额占比"),
                         legend_opts=opts.LegendOpts(orient="vertical",pos_left=550,type_="scroll")
                         )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                         tooltip_opts=opts.TooltipOpts(trigger="item",formatter="{b}: {c} ({d}%)"))
    )
    return pie1
def chart_6(df:DataFrame,path = None)->Pie:
    list_1 = df.index.tolist()
    list_2 = df["Count"].tolist()
    pie1 = (
        Pie()
        .add("",[list(z) for z in zip(list_1,list_2)],center=["30%","50%"],radius=["90%","100%"])
        .set_global_opts(title_opts=opts.TitleOpts(title="支出次数占比"),
                         legend_opts=opts.LegendOpts(orient="vertical",pos_left=550,type_="scroll")
                         )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                         tooltip_opts=opts.TooltipOpts(trigger="item",formatter="{b}: {c} ({d}%)"))
    )
    return pie1
