from parse import parse
from excel_work import *

count_lines = 9

articuls = work_excel(count_lines)
info = parse(articuls)

input_to_worksheet(info, count_lines)

print(info)