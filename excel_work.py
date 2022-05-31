import openpyxl

articuls = []

def set_worksheet():
    wb = openpyxl.open('TestCopy.xlsx')
    sheet = wb.active
    return sheet

def work_excel(count):
    sheet = set_worksheet()

    for line in range(4, count):
        articuls.append({
            sheet[line][0].value
        })

    return articuls

def input_to_worksheet(info, count):
    sheet = set_worksheet()

    i = 0
    for line in range(4, count):
        sheet[line][1] = info[i]['title']

    i+=1

    sheet.save