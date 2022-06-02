import openpyxl

articuls = []



def set_worksheet():
    wb = openpyxl.open('TestCopy.xlsx')
    sheet = wb.active
    return sheet, wb

def work_excel(start_line, count, website):
    sheet, wb = set_worksheet()

    for line in range(start_line, count):

        if website == 1:
            articuls.append({
                sheet[line][0].value
            })
        elif website == 2:
            articuls.append({
                (sheet[line][0].value).pop[0]
            })

    return articuls

def input_to_worksheet(info, start_line, count, website):
    sheet, wb = set_worksheet()

    i = 0
    for line in range(start_line, count):
        if website == 1:
            sheet[line][1].value = info[i]['title']
            sheet[line][2].hyperlink = info[i]['main_photo']
            sheet[line][3].hyperlink = info[i]['photos']
            sheet[line][4].value = int(info[i]['price'].replace(' ', ''))
            sheet[line][10].value = info[i]['material']
        elif website == 2:
            sheet[line][0].value = info[i]['articulate']
            sheet[line][1].value = info[i]['title']
            sheet[line][2].value = int(info[i]['price'].replace(' ', ''))
            sheet[line][8].value = info[i]['material']

        i+=1

    wb.save('TestCopy.xlsx')