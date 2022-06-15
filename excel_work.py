import openpyxl

articuls = []

def set_worksheet():
    wb = openpyxl.open('TestCopy.xlsx', data_only=True)

    sheet = wb.active
    return sheet, wb


def work_excel(start_line, count, website):
    sheet, wb = set_worksheet()

    for line in range(start_line, count):
        articuls.append({
            (str(sheet[line][0].value)).replace(' ', '')})


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
            sheet[line][6].value = info[i]['dimensions']
            sheet[line][10].value = info[i]['material']
            sheet[line][15].value = info[i]['gross weight']
        elif website == 2:
            sheet[line][1].value = info[i]['title']
            sheet[line][2].value = int(info[i]['price'].replace(' ', ''))
            sheet[line][8].value = info[i]['material']
            sheet[line][10].value = info[i]['collection']
            sheet[line][16].value = info[i]['description']

        i+=1

    is_open = True
    while is_open:
        try:
            wb.save('TestCopy.xlsx')
            is_open = False
        except PermissionError:
            print('Закройте эксель файл и нажмите Enter')
            input()
            is_open = True