import pytest

# @pytest.mark.asyncio
# async def text_typing(async_page):
#     await async_page.goto("https://parabank.parasoft.com/")
#     register = async_page.get_by_text("register")
#     await register.click()
#     fn=async_page_





# @pytest.mark.asyncio
# async def test_typing(async_page):
#     await async_page.goto("https://parabank.parasoft.com/parabank/index.htm")
#     register = async_page.get_by_text("Register")
#     await register.click()
#     fn = async_page.locator("//input[@id='customer.firstName']")
#     await fn.fill("Mahi")
#     await async_page.wait_for_timeout(5000)
#     ln = async_page.locator("//input[@id='customer.lastName']")
#     await ln.type("H")
#     add = async_page.locator("//input[@id='customer.address.street']")
#     await add.fill("SriNagar")
#     city = async_page.locator("//input[@id='customer.address.city']")
#     await city.type("Mysore")
#     state = async_page.locator("//input[@id='customer.address.state']")
#     await state.type("Karnataka")
#     zipcode =  async_page.locator("//input[@id='customer.address.zipCode']")
#     await zipcode.type("12345")
#     ph_num = async_page.locator("//input[@id='customer.phoneNumber']")
#     await ph_num.type("12345678999")
#     ssn = async_page.locator("//input[@id='customer.ssn']")
#     await ssn.type("123456789")
#     un = async_page.locator("//input[@id='customer.username']")
#     await un.type("Mahi@123")
#     pwd = async_page.locator("//input[@id='customer.password']")
#     await pwd.fill("123456789")
#     cpwd = async_page.locator("//input[@id='repeatedPassword']")
#     await cpwd.fill("123456789")
#     submit = async_page.locator("(//input[@type='submit'])[2]")
#     await submit.click()
#     await async_page.wait_for_timeout(5000)
#     msg = async_page.locator("//p[text()='Your account was created successfully. You are now logged in.']")
#     await expect(msg).to_be_visible()
#     print(await msg.inner_text())
#     title = async_page.locator("//h1[@class='title']")
#     print(await title.inner_text())
#     await async_page.wait_for_timeout(5000)


# @pytest.mark.asyncio
# async def test_ele_methods(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     ele =  async_page.get_by_text("Register")
#     text_of_ele = await ele.inner_text()
#     print("text of the ele is inner text" ,text_of_ele)
#     text_of_ele = await ele.inner_html()
#     print("text of the ele is html text", text_of_ele)
#     text_of_ele = await ele.text_content()
#     print("text of the ele is text content ", text_of_ele)

#     @pytest.mark.asyncio
#     async def test_mul_ele_methods(async_page):
#         await async_page.goto("https://demowebshop.tricentis.com/")
#         products = async_page.locator("//h2[@class='product-title']")
#         print(products)
#         # await products.first.click()
#         # await async_page.wait_for_timeout(5000)
#         # await products.last.click()
#         # await async_page.wait_for_timeout(5000)
#         await products.nth(1).click()
#         await async_page.wait_for_timeout(5000)
#
# books = ["Computing and Internet","Fiction","Health Book"]

# @pytest.mark.asyncio
# async def test_mul_ele_methods(async_page)
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     ele =async_page.get_by_text("register").wait_for(
#         state ="visible"
#     )

import pytest

# @pytest.mark.asyncio
# async def test_freams(async_page):
#     await async_page.goto("https://jqueryui.com/datepicker/")
#
#     frame = async_page.frame_locator(".demo-frame")
#
#     await frame.locator("//input[@id='datepicker']").click()
#     await frame.locator("//a[text()='14']").click()



# @pytest.mark.asyncio
# async def test_file_upload(async_page):
#     await async_page.goto("https://practice.expandtesting.com/upload#google_vignette")
#     await async_page.locator("#fileInput").set_input_files("/home/joyel/Downloads/XMLViewer.xls")
#     await async_page.locator("#fileSubmit").click()
#     msg = async_page.get_by_text("File Uploaded!")
#     await expect(msg).to_be_visible()


from pathlib import Path
@pytest.mark.asyncio
async def test_file_upload(async_page):
    await async_page.goto("https://demo.automationtesting.in/FileDownload.html#google_vignette")
    # down file:-->
    download_dir = (Path("downloads"))
    download_dir.mkdir(parents=True, exist_ok=True)

    async with async_page.expect_download() as download_dir_info:
        await async_page.locator("(//a[text()='Download'])[1]").click()

    download_ = await download_dir_info.value
    save_path = download_dir / download_.suggested_filename
    await download_.save_as(str(save_path))
    print("file downloaded = " , save_path)
    print("file is exists " , save_path.exists())
    print("down failed" , await download_.failure())
