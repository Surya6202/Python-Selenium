'''
To read the excel files in selenium, we have to import xlrd

Go to cmd prompt --> pip install xlrd==1.2.0

STEPS :
    i) create the workbook object
    ii) create the worksheet object
    iii) read the data of the entire worksheet as the generator object
    iv) Typecast/traverse/next
    v) read the cells seperately
'''

#--------------------------------------------------------------
import xlrd

path = r"C:\Users\Ramya\OneDrive\Desktop\example_excelfile.xlsx"

## opening the excel file
work_book = xlrd.open_workbook(path)
# print(work_book)        ## <xlrd.book.Book object at 0x000001BA7B9397D0>

## create the instance of the worksheet
work_sheet = work_book.sheet_by_name('Sheet1')
# print(work_sheet)       ## <xlrd.sheet.Sheet object at 0x000001BA7B95CED0>

rows_ = work_sheet.get_rows()
# print(rows_)            ## <generator object Sheet.get_rows.<locals>.<genexpr> at 0x0000020804D73060>

## looping through the generator object

for row in rows_:
    print(row)

## op-->
## [text:'name', text:'place', text:'salary']
## [text:'Ram', text:'Bengaluru', number:40000.0]
## [text:'Raavan', text:'Tumkur', number:50000.0]
## [text:'Bharath', text:'Mysore', number:35000.0]

for row in rows_:
    print(row[0].value, row[1].value, row[2].value)

#-------------------------------------------------------------------------

## reading the data in the form of dictionary

dict_1 = {}
for row in rows_:
    dict_1[row[0].value] = (row[1].value, row[2].value)

print(dict_1)       ##

#---------------
## using dict comprehesion

d = {row[0].value:(row[1].value, row[2].value) for row in rows_}
print(d)        ## {'name': ('place', 'salary'), 'Ram': ('Bengaluru', 40000.0), 'Raavan': ('Tumkur', 50000.0), 'Bharath': ('Mysore', 35000.0)}





