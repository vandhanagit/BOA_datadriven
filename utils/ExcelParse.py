from pandas import *
def excel_parse(file,sheet_num):
    xls = ExcelFile(file)
    df = xls.parse(xls.sheet_names[sheet_num])
    return df

