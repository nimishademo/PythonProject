import pytest
from playwright.sync_api import Page,expect

def test_xpath_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

  #absolute xpath (full path) - not recommended
    logo=page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()

  #relative xpath  //tagname[@attribute='value]

    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.wait_for_timeout(5000)

  #xpath with contain()
    products=page.locator("//h2//a[contains(@href,'computer')]")
    print("Products count:", products.count())
    expect(products).to_have_count(products.count())

    print("First Computer Product:",products.first.text_content())
    print("Last Computer Product:", products.last.text_content())
    print("N-th Computer Product:", products.nth(2).text_content()) #n take index from 0

    products_title=products.all_text_contents()
    print("Product titles:",products_title)

    print("printing product title using looping statement")
    for i in products_title:
        print((i))

    #product start- with()

    building_products=page.locator("//h2//a[starts-with(@href,'/build')]")
    print(building_products.count())
    expect(building_products).to_have_count(building_products.count())

    #xpath with text() -is representing inner text of te element

    registration_link=page.locator("//a[text()='Register']")
    expect(registration_link).to_be_visible()

    page.wait_for_timeout(5000)

    #xpath with last()

    googleppluslink=page.locator("//div[@class='column follow-us']//Li[Last()]")
    expect(googleppluslink).to_have_text("Google+")

    #xoath with position
    twitterlink= page.locator("//div[@class='column follow-us']//Li[position()=2]")
    expect(twitterlink).to_have_text("Twitter")
