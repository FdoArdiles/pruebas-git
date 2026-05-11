import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/checkbox")
       # checkbox = page.get_by_role("checkbox", name="Select Home")
        checkbox = page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div/div[3]/div/div/div/div[1]/span[3]')
        await checkbox.check()
        await checkbox.screenshot(path="screenshots/checkboxes.png")
        #-Assertions
        await expect(checkbox).to_be_checked()
        await expect(page.locator("#result")).to_have_text("You have selected :homedesktopdocumentsdownloadsnotescommandsworkspaceofficewordFileexcelFilereactangularveupublicprivateclassifiedgeneral")
        #-Stoping Tracing
        await context.tracing.stop(path = "logs/trace.zip")
        #-Closing browser
        await browser.close()

asyncio.run(main())