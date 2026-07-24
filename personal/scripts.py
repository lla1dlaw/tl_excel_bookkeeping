import xlwings as xw
from xlwings import script


@script(name="Run Test Script", include=["Sum"])
def test(book: xw.Book):
    print("Test Worked!")


@script(name="Sheet Search", include=["Sum"])
def sheet_search(book: xw.Book):
    book.

