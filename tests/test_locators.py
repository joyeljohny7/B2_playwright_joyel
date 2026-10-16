 #1. .evn why how when
#2. requirement .txt why wht how to use
#3. HTML
#4. locators
#5. click()/type()

# from pygments.formatters import img

import os
# import pytest_asyncio
# import pytest
# from utils.config import BASE_URL,USERNAME,PASSWORD
# @pytest.mark.asyncio
# async def test_demo(async_page):
#     await async_page.goto(BASE_URL)
    #web_ele : we can get with the help of locators
#Locators-->
#HTML--> 1)tags any <input>,<button>,<div>,<a> 2)attributes id="email",pwd="pass" type="button" value="search" 3)Elements
#What is attribute names(an) id,pwd,type,value
#What is attribute value(av) pass,button,search
#text -- >forgotpassword, >login,>books.<welcome
#playwright official website
 #css and xpath
 #get by role
 #<button> type:button clickme
 #<a link
 #<img
import playwright.async_api as playwright
# utils methods
import pytest
from utils.config import BASE_URL,USERNAME,PASSWORD
#
# @pytest.mark.asyncio
# async def test_evn(async_page):
#     await async_page.goto(os.getenv("BASE_URL")) #-- dotenv --loads the .env
#     await async_page.goto(BASE_URL)
#     print(await async_page.title())
# from dotenv import load_dotenv
# load_dotenv()
    #---------------------------------#
    #python -m pip freeze>requirements.txt
    #imp --> python,playwright, pytest versions to be noted
    #---------------------------------#
            #how to setup
    #python -m venv .venv
    #.venv\Scripts\Activate.ps1
    #pip install -r requirements.txt
    #---------------------------------#
    #python -m pip install python-dotenv
    #un:-abc@gmail.com
    #pwd:-abc@123
    #https://demoweb.tricentis.com/
    #.env :-
#HTML Attributes
#page.getByRole()to locate by explicit and implicit accessibility attributes
# import pytest
# from playwright.async_api  import expect
#
#
# @pytest.mark.asyncio
# async def test_getbyrole(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     reg_link=async_page.get_by_role("link",name="Register")
#     await expect(reg_link).to_be_visible()
#     #click on it
#     await reg_link.click()
#     await expect(async_page).to_have_title("Demo Web Shop. Register")

#page.getByText()
# @pytest.mark.asyncio
# async def test_getByText(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     excellent=async_page.get_by_text("Excellent")
#     await expect(excellent).not_to_be_checked()
#     await excellent.click()
#     await expect(excellent).to_be_checked()
#     await async_page.wait_for_timeout(5000)
#     vb= async_page.get_by_role("radio",name="Very bad")
#     await expect(vb).to_be_visible()
#     await vb.click()
#page.getByLabel()  working
# @pytest.mark.asyncio
# async def test_getBylabel(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     reg_link = async_page.get_by_text("Register")
#     await expect(reg_link).to_be_visible()
#     await reg_link.click()
#     g = async_page.get_by_text("Male").nth(0)
#     await expect(g).to_be_visible()
#     await g.click()
#     fn = async_page.get_by_label("First name:")
#     await expect(fn).to_be_visible()
#     await fn.fill("Nevin")
#     ln = async_page.get_by_label("Last name:")
#     await expect(fn).to_be_visible()
#     await ln.fill("Jude Jose")
#     em = async_page.get_by_label("Email:")
#     await expect(em).to_be_visible()
#     await em.fill("nevin.jude@benzyinfotech.com")
#     pwd = async_page.get_by_label("Password:").nth(0)
#     await expect(pwd).to_be_visible()
#     await pwd.fill("Abc@123")
#     cpwd = async_page.get_by_label("Confirm Password:").nth(0)
#     await expect(cpwd).to_be_visible()
#     await cpwd.fill("Abc@123")
#     await async_page.wait_for_timeout(5000)
# page.getByLabel() to locate a form control by associated label's text. (Ashwini code)
# @pytest.mark.asyncio
# async def test_getBylabel(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/")
#    reg_link =  async_page.get_by_text("Register")
#    await expect(reg_link).to_be_visible()
#    await reg_link.click()
#    g = async_page.get_by_text("Female")
#    await expect(g).to_be_visible()
#    await g.click()
#    fn = async_page.get_by_label("First name:")
#    await expect(fn).to_be_visible()
#    await fn.fill("Abc")
#    ln = async_page.get_by_label("Last name:")
#    await expect(ln).to_be_visible()
#    await ln.fill("Abc")
#    email = async_page.get_by_label("Email:")
#    await expect(email).to_be_visible()
#    await email.fill("abc@gmail.com")
#    pwd = async_page.get_by_label("Password:").nth(0) # [pwd,cpwd]
#    await expect(pwd).to_be_visible()
#    await pwd.fill("Abc@123")
#    cpwd = async_page.get_by_label("Confirm password:")
#    await expect(cpwd).to_be_visible()
#    await cpwd.fill("Abc@123")
#    await async_page.wait_for_timeout(5000)
#page.getByPlaceHolder() not working

@pytest_asyncio.fixture
async def test_getByPlaceHolder(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    search_tb=async_page.get_by_placeholder("Search store")
    await expect(async_page).to_be_visible()
    await search_tb.fill("Books")
    print(search_tb.input_value())
     await expect(search_tb.input_value()).to_be_have_a_value
# page.getByPlaceholder() to locate an input by placeholder. working
# @pytest.mark.asyncio
# async def test_getByPlaceholder(async_page):
#    await async_page.goto("https://www.amazon.in/")
#    search_tb = async_page.get_by_placeholder("Search Amazon.in")
#    await expect(search_tb).to_be_visible()
#    await search_tb.fill("Books")
#    print(search_tb.input_value())
#    await async_page.wait_for_timeout(5000)
#page.getByAltText()
# @pytest.mark.asyncio
# async def test_getByAltText(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/")
#    img=async_page.get_by_alt_text("Picture of 14.1-inch Laptop")
#    await expect(img).to_be_visible()
#    await img.click()
#    await expect(async_page).to_have_url("https://demowebshop.tricentis.com/141-inch-laptop")
#    await async_page.wait_for_timeout(5000)
#page.getByTitle()
# @pytest.mark.asyncio
# async def test_getByTitle(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/")
#    img=async_page.get_by_title("Show details for Build your own cheap computer")
#    await expect(img).to_be_visible()
#    await img.click()
#    await expect(async_page).to_have_url("https://demowebshop.tricentis.com/build-your-cheap-own-computer")
#    await async_page.wait_for_timeout(5000)
