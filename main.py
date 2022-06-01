from parse import parse
from excel_work import *

count_lines = 9

articuls = work_excel(count_lines)
info = parse(articuls, count_lines)



input_to_worksheet(info, count_lines)

i = 0
for line in range(4, count_lines):
    print(info[i]['title'])
    i+=1
