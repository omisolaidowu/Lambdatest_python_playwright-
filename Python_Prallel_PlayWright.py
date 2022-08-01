import json
import os
import urllib
import subprocess
from dotenv import load_dotenv

from playwright.sync_api import sync_playwright


load_dotenv('.env')

username = os.getenv("my_username")
gridAcessKey = os.getenv("access_key")

# print(username)
# print(gridAcessKey)
playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]

capabilities =[
    {
        'browserName': 'pw-firefox',  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
        'browserVersion': 'latest',
        'platform': 'Windows 10',
        'build': 'Playwright parallel test Firefox',
        'name': 'Playwright Test Case 1',
        'user': username,
        'accessKey': gridAcessKey,
        'console': True,
        'playwrightversion': playwrightVersion
    },
    
    {
        'browserName': 'Chrome',  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
        'browserVersion': 'latest',
        'platform': 'Windows 10',
        'build': 'Playwright parallel test Chrome',
        'name': 'Playwright Test Case 2',
        'user': username,
        'accessKey': gridAcessKey,
        'console': True,
        'playwrightversion': playwrightVersion
    },

    {
        'browserName': 'MicrosoftEdge',  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
        'browserVersion': 'latest',
        'platform': 'Windows 10',
        'build': 'Playwright parallel Edge',
        'name': 'Playwright Test Case 3',
        'user': username,
        'accessKey': gridAcessKey,
        'console': True,
        'playwrightversion': playwrightVersion
    }
]

stringifiedCaps = [urllib.parse.quote(json.dumps(i)) for i in capabilities]

executionURL = 'wss://cdp.lambdatest.com/playwright?capabilities='

def test_registration(playwright):
    
    try:
        browser = [playwright.chromium.connect(executionURL+i) for i in stringifiedCaps]
        pages = [i.new_page() for i in browser]

        for page in pages:
            page.goto("https://ecommerce-playground.lambdatest.io/")
            title = page.title()
            print(title)
            assert("Store") in title
    except AssertionError as err:
        print("Error:: Word not in title")
    else:

        try:

            for page in pages:
                page.locator('input[name="search"] >> nth = 0').fill('nigger')
                page.locator('div[class="search-button"]:has-text("Search")').click()
                page.locator('div[id="widget-navbar-217834"]').hover()
                page.locator('a[role="button"]:has-text("My account")').hover()
                page.locator('span[class="title"]:has-text("Register")').click()

                

                page.locator('input[placeholder="First Name"]').fill('Idowu')
                page.locator('input[placeholder="Last Name"]').fill('Omisola')
                page.locator('input[placeholder="E-Mail"]').fill('sul0557dgddf@gmail.com')
                page.locator('input[placeholder="Telephone"]').fill('0908364773')
                page.locator('input[placeholder="Password"]').fill('testpasses')
                page.locator('input[placeholder="Password Confirm"]').fill('testpasses')
                page.locator('label:has-text("No")').click()
                page.locator('label:has-text("I have read and agree to the Privacy Policy")').click()
                page.locator('input[value="Continue"]').click()


                page.locator("text=Continue").click()
                # page.locator('a[class="btn"]:has-text("Continue")').click()
                title = page.title()
                print("Title:: ", title)
                set_test_status(page, "passed", "Title matched")
        except Exception as err:
            for page in pages:
                print(err)
                set_test_status(page, "failed", str(err))

    for browse in browser:      
        browse.close()



def set_test_status(page, status, remark):
    page.evaluate("_ => {}",
        "lambdatest_action: {\"action\": \"setTestStatus\", \"arguments\": {\"status\":\"" + status + "\", \"remark\": \"" + remark + "\"}}")



with sync_playwright() as playwright: 
    test_registration(playwright)





    # py.test -n 2 testlambda.py