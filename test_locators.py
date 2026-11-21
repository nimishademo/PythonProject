import time

from playwright.sync_api import Page,expect
import time
import re


def test_verify_pwlocators(page:Page):
#     page.goto("https://demo.nopcommerce.com/")
#
#     #time.sleep(5)
#     page.wait_for_timeout(5000)  #500 ms = 5 sec
#
#     # page.get_by_alt_text
#     logo=page.get_by_alt_text("nopCommerce demo store")
#     expect(logo).to_be_visible()
#     page.close()
#
#     #page.get_by_text
#     expect(page.get_by_text("Welcome to our store")).to_be_visible() #full text
#     expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible()#reg expression
#
#    #page.getByRole()
#     page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
#     page.wait_for_timeout(5000)
#     expect(page.get_by_role("heading", name="Register")).to_be_visible()
#
#   #page.get_by_label
#     page.get_by_label("First name:").fill("John")
#     page.get_by_label(("Last name:")).fill("kenedy")
#     page.get_by_label(("Email:")).fill("abc@gmail.com")
#
#   #page.get.by_placeholder
#     page.get_by_placeholder("Search store").fill("mac laptop")
#     page.wait_for_timeout(5000)






    page.goto("https://playwright.dev/")

    element = page.get_by_title("Issues count")
    print(element.count())