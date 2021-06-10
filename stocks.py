# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# from pprint import pprint

# from pyasn1.type.univ import Null


# scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

# creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\dbaks\OneDrive\Desktop\creds.json", scope)

# client = gspread.authorize(creds)

# sheet = client.open("stockPrices").sheet1  # Open the spreadhsheet
# # data = sheet.get_all_records()
# # row = sheet.row_values(1000)
# # cell = sheet.cell(1,2).value

# # insertRow = ["hhello", 4, "orange", "blue"]
# # sheet.insert_row(row, 4)
# # sheet.insert_row([1,1,1,1,1,1,1,1], 10)
# # pprint(row)
# r = open(r"C:\Users\dbaks\OneDrive\Desktop\tickers.txt", "r")
# list = r.read().split()
# formula = '=GOOGLEFINANCE("NASDAQ:{}", "price", DATE(2021,1,1), DATE(2021,6,8), "DAILY")'
# index = 0
# new_list = []
# for i in list:
#     new_list.append(formula.format(i))
#     new_list.append('')
#     if(index == 100):
#         break
#     index+=1

# sheet.insert_row(new_list, 1)

# # print(li)


# # li = []
# # for i in range(4728):
# #     temp = input()
# #     i = 0
# #     while(temp[i]!='|'):
# #         i+=1
# #     li.append(temp[:i])
# # r.write(" ".join(li))
# # r.close()

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as pt
import time

api_key = 'WQ1NYMOA5E7JH1SM'

ts = TimeSeries(key=api_key, output_format='pandas')

# data, meta_data = ts.get_daily(symbol='F', outputsize = 'full')
r = open(r"C:\Users\dbaks\OneDrive\Desktop\tickers.txt", "r")
list = r.read().split()
# print(list)

tot = 0
for i in list:
    data, meta_data = ts.get_daily(symbol=i, outputsize = 'full')
    if(tot == 4):
        break
    tot+=1
    pt.plot(data.index, data["1. open"])    
pt.show()

# print(data.index)
# print(data["1. open"])



# data = data.reindex(index=data.index[::-1])
# print(data)
# data.to_excel(r"C:\Users\dbaks\OneDrive\Desktop\output.xlsx")
# i = 1
# while i==1:
#    data, meta_data = ts.get_intraday(symbol='GOOG', interval = '1min', outputsize = 'full')
#    data.to_excel(r"C:\Users\dbaks\OneDrive\Desktop\output.xlsx")
#    time.sleep(60)
#    break