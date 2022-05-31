import openpyxl

articuls = []

def work_excel(count_articuls):
    wb = openpyxl.open('TestCopy.xlsx')
    sheet = wb.active

    for line in range(4, count_articuls):
        articuls.append({
            sheet[line][0].value
        })

    return articuls