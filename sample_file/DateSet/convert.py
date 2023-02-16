import csv
import pykakasi 

kakasi = pykakasi.kakasi() # インスタンスの作成


with open('./data1.csv', 'r',encoding = "shiftjis") as f:
    data = csv.reader(f)
    content = [row for row in data] 

#---------------- ローマ字に変換 --------------------#

    # i = 0
    # for voc in content:
    #     result = kakasi.convert(voc[1])
    #     for item in result:
    #         print(i)
    #         content[i][2] = item['hepburn']
    #         print(item['hepburn'])
    #         i = i + 1

#---------------------------------------------------#



#---------------- 数値に変換 -----------------------#


    i = 0
    for voc in content:
        content[i][0] = "id"+ str(i+1)
        result = ''
        for x in voc[2]:
            res = ord(x) - 97
            content[i].append(str(res))
        i = i + 1
        # print(result)


#--------------------------------------------------#


with open('data1.csv', 'w', encoding = 'shiftjis') as f:
    data = csv.writer(f)
    
    data.writerows(content)



