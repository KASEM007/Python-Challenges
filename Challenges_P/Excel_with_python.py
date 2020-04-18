import xlwings as xw

# creat a work Book
work_book = xw.Book()
# creat a excel sheet
work_book.save("my_work_book.xlsx")

# TO open exesting excel sheet
# work_book = xw.Book("file_name.xlsx"
# change
# work_book.save()

# fill with data:

st1 = work_book.sheets["Sheet1"]

st1.range("B1").value = [1, 2, 3]
st1.range("A2").options(transpose=True).value = [1, 2, 3]

dataCells = st1.range("B2:D4")
# dataCells.value = 'test'

for cell in dataCells:
    # the next line will return string like ($B$2)
    # so we need to ignore the first $ and then split on it
    address = cell.address[1:].split("$")
    # example :B
    column = address[0]
    # example:2
    row = address[1]

    cell.value = f"=A{row}*{column}1"



# Add Style


wb.save()
