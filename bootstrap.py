import pytest
from playwright.sync_api import sync_playwright,expect,Page

def test_bootstrap(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #login step
    page.locator('input[name="username"]').fill("Admin")
    page.locator('input[name="password"]').fill("admin123")
    page.locator('button[type="submit"]').click()

    page.wait_for_timeout(5000)

    #click on PIM
    page.get_by_text('PIM').click()

    #click on job title dropdown

    page.locator("form i").nth(3).click()  #this will open options from dropdown

    #capture all the options from dropdown

    options = page.locator("div[role='listbox'] span")

    count = options.count()
    print ("number of options:",count)

    expect(options).to_have_count(15) #assertion for counting the options