import pytest
from  playwright.sync_api import  sync_playwright,expect, Page

def test_static_table(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #locating table
    table=page.locator("table[name = 'BookTable'] tbody")
    expect(table).to_be_visible()

    #count no of row in table

    rows=table.locator("tr")
    expect(rows).to_have_count(7)

    row_count = rows.count()
    print(row_count)

    #count total number of column
    columns=rows.locator("th")
    expect(columns).to_have_count(4)

    column_count=columns.count()
    print(column_count)

    #read all the data from 2nd row
    second_row = rows.nth(2).locator('td')

    print("2nd row data", second_row.all_inner_texts())

    expect(second_row).to_have_text(
        ['Learn Java', 'Mukesh', 'Java', '500']
    )

    #read all rows and column

    data=rows.all()
    # for row in data[1:]:
    #      col=row.locator('td').all_inner_texts()
    #      print(col)

  # print Book names whose author is 'Mukesh'
    for row in data[1:]:
         author_name=row.locator('td').nth(0).inner_text()
         if author_name=='Mukesh':
            book_name=row.locator('td').nth(0).inner_text()
            print(f"{author_name} \t {book_name}")

  # calculate total price of all the books
    total_price =0
    for row in data[1:]:
        price=row.locator('td').nth(3).inner_text()
        total_price=total_price+price




