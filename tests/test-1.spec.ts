import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
 await page.goto('https://demoqa.com/');
 await page.getByRole('link', { name: 'Elements' }).click();
 await page.getByRole('link', { name: 'Check Box' }).click();
 await page.goto('https://demoqa.com/checkbox');
 await page.getByRole('checkbox', { name: 'Select Home' }).click();
 const resultado = await page.locator('#result');
 expect(resultado).toHaveText("You have selected :homedesktopdocumentsdownloadsnotescommandsworkspaceofficewordFileexcelFilereactangularveupublicprivateclassifiedgeneral");
});