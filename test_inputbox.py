import pytest
from playwright.sync_api import expect,Page

# def test_inputbox(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/")
#     text_box=page.locator("#name")

    #visibility and  enable
    # expect(text_box).to_be_visible()
    # expect(text_box).to_be_enabled()
    #
    # #check the attribute of the elements
    # expect(text_box).to_have_attribute("maxlength","15")
    #
    # #get an attribute of the element
    # maxlength=text_box.get_attribute("maxlength")
    # print(maxlength)
    #
    # #fill the text
    # text_box.fill("john")
    #
    # #capture value from the input box
    # enteredvalue=text_box.input_value()
    # print("value entered is:", enteredvalue)
    #
    # page.wait_for_timeout(5000)

###########check for radio button

# def test_radiobutton(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/")
#     male_radiobutton=page.locator("#male")
#
#     #visibility and enable
#     expect(male_radiobutton).to_be_visible()
#     expect(male_radiobutton).to_be_enabled()
#
#     #male radio button should not be checked(default)
#     expect(male_radiobutton).not_to_be_checked()
#
#     #select radio button (action)
#     male_radiobutton.check()
#
#     # male radio button should be checked(default)
#     expect(male_radiobutton).to_be_checked()
#
#################checkbox

def test_checkbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    male_checkbox=page.locator("#male")

    #select specific checkbox

    # sunday_checkbox=page.get_by_label("Sunday")
    # sunday_checkbox.check()
    # expect(sunday_checkbox).to_be_checked()
    # page.wait_for_timeout(5000)

    #count number of checkbox

    days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    checkboxes=[]

    for i in days:
        checkbox=page.get_by_label(i)
        checkboxes.append(checkbox)
        print(checkboxes)

## select all the checkbox and assert each checkbox is selected

    for checkbox in checkboxes:
        checkbox.check()
        expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)

#check last 3 checkbox
    for checkbox in checkboxes[-3:]:
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()

    page.wait_for_timeout(5000)

#toggle checkbox
    for checkbox in checkboxes:
        if checkbox.is_checked():
            checkbox.uncheck()
        expect(checkbox).not_to_be_checked()
    else:
        checkbox.check()
        expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)






