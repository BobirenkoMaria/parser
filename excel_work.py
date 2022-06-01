import openpyxl

articuls = []



def set_worksheet():
    wb = openpyxl.open('TestCopy.xlsx')
    sheet = wb.active
    return sheet, wb

def work_excel(start_line, count):
    sheet, wb = set_worksheet()

    for line in range(start_line, count):
        articuls.append({
            sheet[line][0].value
        })

    return articuls

def input_to_worksheet(info, start_line, count):
    sheet, wb = set_worksheet()


    i = 0
    for line in range(start_line, count):
        sheet[line][1].value = info[i]['title']
        sheet[line][2].value = info[i]['main_photo']
        sheet[line][4].value = int(info[i]['price'].replace(' ', ''))
        sheet[line][10].value = info[i]['material']

        i+=1

    wb.save('TestCopy.xlsx')