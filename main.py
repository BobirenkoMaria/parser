from parse2 import get_page_data
from parse import parse
from excel_work import *

start_line = int(input('Начальная строка: '))
end_line = int(input('Конечная строка: '))

print('\nВыберите сайт:\n'
      '1) wasserkraft\n'
      '2) davitamebel')
website = int(input())

articuls = work_excel(start_line, end_line, website)
info = parse(articuls, start_line, end_line, website)
input_to_worksheet(info, start_line, end_line, website)