from playwright.sync_api import sync_playwright
 
def test_form_inputs(playwright):
    try:
        browser = playwright.chromium.launch(channel="chrome")
        page = browser.new_page()
        page.goto("https://www.lambdatest.com/selenium-playground/simple-form-demo")
 
        title = page.title()
        print(title)
        assert("Selenium") in title
    except AssertionError as err:
        print("Error:: Word not in title")
    else:
        try:
            print("Title confirmed")
            page.locator('input[placeholder="Please enter your Message"] >> nth = 0').fill('Idowu Omisola')
            page.locator('button:has-text("Get Checked value")').click()
 
            page.locator('input[placeholder="Please enter your Message"] >> nth = 1').fill('5')
            page.locator('input[placeholder="Please enter your Message"] >> nth = 2').fill('10')
            page.locator('button:has-text("Get values")').click()
        except Exception as err:
            print(err)
 
    browser.close()
   
   
with sync_playwright() as playwright:
    test_form_inputs(playwright)
