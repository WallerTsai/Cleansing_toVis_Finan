from pandas import DataFrame,Series
import Clean
class Function:
    def __init__(self,df:DataFrame,user_list:list) -> None:
        self.df = df            
        self.list = user_list   
    def sum_by_choosed(self,year=None, month=None):
        df_1 : DataFrame = self.df.copy()
        Clean.solution_cash_flow(df_1)
        if year is not None:
            df_1 = Clean.filter_data(df_1,year,month)
        df_1 = Clean.calculate_label_with_sum(df_1,label_column='收/支',amount_column="金额")
        income = df_1.loc[1,"Total Amount"]
        outcome = df_1.loc[-1,"Total Amount"]
        return int(income) , int(outcome)
    def classify_sum_by_choosed(self,year,month = None)->Series:
        df_2 : DataFrame = self.df.copy()
        Clean.solution_cash_flow(df_2)
        df_2 = Clean.filter_data(df_2,year,month)
        df_income = df_2.loc[df_2["收/支"] == 1]
        df_outcome = df_2.loc[df_2["收/支"] == -1]
        if month is None:
            df_income = Clean.sum_by_month(df_income,"金额")
            df_outcome = Clean.sum_by_month(df_outcome,"金额")
        else:
            df_income = Clean.sum_by_day(df_income,"金额")
            df_outcome = Clean.sum_by_day(df_outcome,"金额")
        return df_income,df_outcome
    def sizeAndsum_by_labels(self,year = None,month = None):
        df_3 : DataFrame = self.df.copy()
        Clean.solution_cash_flow(df_3)
        if year is not None:
            df_3 = Clean.filter_data(df_3,year,month)
        df_outcome = df_3.loc[df_3["收/支"] == -1]
        df_outcome = Clean.calculate_label_with_sum(df_outcome,"类型","金额")
        return df_outcome
    def sizeAndsum_by_products(self,year = None,month = None):
        df_3 : DataFrame = self.df.copy()
        Clean.solution_cash_flow(df_3)
        if year is not None:
            df_3 = Clean.filter_data(df_3,year,month)
        df_outcome = df_3.loc[df_3["收/支"] == -1]
        df_outcome = Clean.calculate_label_with_sum(df_outcome,"商品","金额")
        return df_outcome
