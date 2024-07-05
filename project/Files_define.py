import Files_reading as fr
import Clean as cl
from pandas import DataFrame
class FileReader:
    def __init__(self,path:str,user_list:list) -> None:
        self.path = path        
        self.list = user_list   
    def read_data(self) -> DataFrame:
        pass
    def needs_label_choose(self) -> DataFrame:
        pass
class CsvFileReader(FileReader):
    def read_data(self) -> DataFrame:
        encoding = fr.in_csv_encoding(self.path)
        df = fr.csv_read(filepath= self.path,encoding_type=encoding)
        return df
    def needs_label_choose(self) -> DataFrame:
        df = self.read_data()
        columns = df.columns
        columns_list = columns.tolist()
        if columns_list == ['交易时间', '交易类型', '交易对方', '商品', '收/支', 
                            '金额(元)', '支付方式', '当前状态', '交易单号', '商户单号', '备注']:
            df2 = cl.Cleaning_1(df,self.list)
            df3 = cl.WeChat_label(df2)
        elif columns_list ==['交易时间', '交易分类', '交易对方', '对方账号', 
                            '商品说明', '收/支', '金额', '收/付款方式', '交易状态', 
                            '交易订单号', '商家订单号', '备注', 'Unnamed: 12']:
            df2 = cl.Cleaning_1(df,self.list)
            df3 = cl.alipay_label(df2)
        else:
            df2 = cl.Cleaning_1(df,self.list)
            df3 = cl.other_label(df2)
        return df3
class XlsxFileReader(FileReader):
    pass
if __name__ == '__main__':
    pass
