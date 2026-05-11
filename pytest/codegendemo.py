from playwright.sync_api import Playwright, sync_playwright, expect
import  pytest

def test_example(page : page) -> None:

    #Go to https://www.saucedemo.com/
    page.goto("https://www.saucedemo.com/")

    #Click [data-test="username"]
    page.locator("[data-test=\"username\"]").click()

    #Fill [data-test="username"]
    page.locator("[data-test=\"username\"]").fill("standard_user")

    #Click [data-test="password"]
    page.locator("[data-test=\"password\"]").click()

    #Fill [data-test="password"]
    page.locator("[data-test=\"password\"]").fill("secret_sauce")

    #Click [data-test="login-button"]
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")



