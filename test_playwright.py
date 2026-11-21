from playwright.sync_api import Page,expect

def test_verifyPageUrl(page:Page):
    page.goto("http://www.automationpractice.pl/index.php")  #passing URL
    myurl=page.url
    print("url of the appliaction:",myurl)
    expect(page).to_have_url("http://www.automationpractice.pl/index.php") #expected URL

def test_verifyTitle(page:Page):
    page.goto("http://www.automationpractice.pl/index.php")
    mytitle=page.title()
    print("title of the page:",mytitle)
    expect(page).to_have_title("My Shop")