import csv

list = ['English_News_Dev', 'English_News_Test', 'English_News_Train', 'English_WikiNews_Dev', 'English_WikiNews_Test', 'English_WikiNews_Train', 'English_Wikipedia_Dev', 'English_Wikipedia_Test', 'English_Wikipedia_Train']
header = ['Number', 'Word', 'Rating']

csvFile = open("dataSets.csv", 'w')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(header)

count = 1
for tsvName in list:
    tsvFile = open("C:\\Users\prabh\\CWI\\cwidatasets\\data\\CWIG3G2-Data\\English\\" + tsvName + ".tsv", encoding="utf8")
    for i in tsvFile:
        splitSentence = i.split('\t')
        if(" " in splitSentence[4]): continue
        splitSentence[7] = splitSentence[7].rstrip()
        splitSentence[4] = splitSentence[4].lower()
        csvRow = [count, splitSentence[4], splitSentence[7]]
        csvRow[1] = csvRow[1].encode('ascii', 'ignore').decode()
        csvWriter.writerow(csvRow)
        print(tsvName, " ", csvRow)
        count += 1 

tsvFile.close()
csvFile.close()



