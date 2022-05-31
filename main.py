from parse import parse
from excel_work import work_excel

articuls = []

articuls = work_excel(603)

parse(articuls)

print(articuls)