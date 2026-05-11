import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
 await page.goto('https://demoqa.com/');
 await page.getByRole('link', { name: 'Elements' }).click();
 await page.getByRole('link', { name: 'Check Box' }).click();
 await page.goto('https://demoqa.com/checkbox');
 await page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div/div[3]/div/div/div/div[1]/span[3]').click()
 const resultado = await page.locator('#result');
 expect(resultado).toHaveText("You have selected :homedesktopdocumentsdownloadsnotescommandsworkspaceofficewordFileexcelFilereactangularveupublicprivateclassifiedgeneral");
});