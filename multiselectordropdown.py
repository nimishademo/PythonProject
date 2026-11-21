

import pytest
from playwright.sync_api import sync_playwright,expect,Page

def test_multiselect(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #multiple options from dropdown

    # page.locator("#colors").select_option(["Red","Blue"]) #by label
    # page.locator("#colors").select_option(label=["Red", "Blue"])

    # page.locator("#colors").select_option(value=["Red", "Blue","green"]) # by value

    # page.locator("#colors").select_option(index=[2,4]) # by index

    dropdown_options = page.locator("#colors > option")

    expect(dropdown_options).to_have_count(7)
    page.wait_for_timeout(5000)