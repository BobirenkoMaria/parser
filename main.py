from parse2 import get_page_data
from parse import parse
from excel_work import *

start_line = 24
end_line = 603

articuls = work_excel(start_line, end_line)
info = parse(articuls, start_line, end_line)
input_to_worksheet(info, start_line, end_line)

i = 0
for line in range(start_line, end_line):
    print(info[i]['title'])
    i+=1
