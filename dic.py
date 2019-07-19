dic=dict()
dic["mouse"]='chuot'
dic["computer"]='may tinh'
dic["keyboard"]='ban phim'
while True:
    tu=input("nhập từ cần tra ")
    if(tu in ['exit','quit']):
        break
    if tu in dic.keys():
        print(dic[tu])
    elif tu in dic.values():
        print("có từ đã nhập trong từ điển")
    else:
        print("từ đã nhập không có trong từ điển")


print()