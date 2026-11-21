import pytest
from playwright.sync_api import Page,expect

def test_handle_dynamic_elements(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")


    for i in range(5):
        button=page.locator("//button[text()='START' or text()='STOP']")
        button.click()

        page.wait_for_timeout(5000)
