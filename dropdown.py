import pytest
from playwright.sync_api import Page,expect,sync_playwright

def test_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    ##3 ways
    #page.locator("#country").select_option("India")  #by label
    #page.locator("#country").select_option(label="India")

    #page.locator("#country").select_option("germany") #by value
    #page.locator("#country").select_option(value="germany")


    #page.locator("#country").select_option(index=3) #by index

    #check number of options in dropdown

    dropdown_options=page.locator("#country>option")
    expect(dropdown_options).to_have_count(10)

    options_text=[text.strip()for text in dropdown_options.all_text_contents()]

    #print countries using loop

    for options in options_text:
        print(options)

    page.wait_for_timeout(5000)