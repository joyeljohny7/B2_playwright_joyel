import pytest
#
# @pytest.mark.asyncio
# async def test_static_dropdown(async_page):
#     await async_page.goto("https://www.amazon.in/")
#     drop_down = async_page.locator("#searchDropdownBox")
#     await drop_down.select_option(label="Beauty")
#     await drop_down.select_option(label="search-alias=computers")
#     await drop_down.select_option(index = 5)
#     await async_page.wait_for_timeout(5000)

# @pytest.mark.asyncio
# async def test_static_dropdown(async_page):
#     await async_page.goto("https://www.amazon.in/")
#     drop_down = async_page.locator("//select[@id='searchDropdownBox']")
#     await drop_down.select_option(label="Beauty")
#     await drop_down.select_option("search-alias=computers")
#     await drop_down.select_option(index = 5)
#     await async_page.wait_for_timeout(5000)

# @pytest.mark.asyncio
# async def test_static_dropdown(async_page):
#     await async_page.goto("https://www.amazon.in/")
#     drop_down = async_page.locator("//select[@id='searchDropdownBox']")
#     await drop_down.select_option(label="Beauty")
#     await drop_down.select_option("search-alias=computers")
#     await drop_down.select_option(index = 5)
#     await async_page.wait_for_timeout(5000)
#     await expect(drop_down).to_have_value("search-alias=amazon-pharmacy")

# @pytest.mark.asyncio
# async def test_static_drop_down_selectmul(async_page):
#     await async_page.goto("https://www.amazon.in/")
#     drop_down = async_page.locator("//select[@id='searchDropdownBox']")
#     await drop_down.select_option(
#         label=["Amazon Devices","Amazon Pharmacy"]
#     )


# @pytest.mark.asyncio
# async def test_static_drop_down_selectmul(async_page):
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     drop_down = async_page.locator("//select[@id='colors']")
#     await drop_down.select_option(
#         label=["Red","Yellow"]
#     )
#
#     allele =await drop_down.all_inner_texts()
#     print(allele)

# @pytest.mark.asyncio
# async def test_static_drop_down_selectmul(async_page):
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     drop_down = async_page.locator("//select[@id='colors']")
#     await drop_down.select_option(
#         label=["Red", "Yellow"]
#     )
#
#     allele = await drop_down.all()
#     print(allele)  # all options
#     # slected
#     selected_op = await drop_down.locator("option:checked").all_text_contents()
#
#     values = []
#     for i in selected_op:
#         values.append(i.strip())
#
#     assert "Red" in values
#     assert "Yellow" in values


# @pytest.mark.asyncio
# async def test_dynamic_dropdown(async_page):
#     await async_page.goto("https://www.amazon.in/")
#     search_box = async_page.locator("//input[@id='twotabsearchtextbox']")
#     await search_box.fill("Books")
#     await async_page.wait_for_timeout(5000)
#
#     ops =   async_page.locator("//div[@class='s-suggestion-container']")
#     ops.first.wait_for(state="visible")
#     allops = await ops.all_text_contents()
#     print(allops)


# @pytest.mark.asyncio
# async def test_dynamic_dropdown(async_page):
#     await async_page.goto("https://www.amazon.in/")
#     search_box = async_page.locator("//input[@id='twotabsearchtextbox']")
#     await search_box.fill("Books")
#     await async_page.wait_for_timeout(5000)
#
#     ops =   async_page.locator("//div[@class='s-suggestion-container']")
#     allops = await ops.all_text_contents()
#     print(allops)
#     op =  await ops.all()# all op ele
#     for i in op:
#         text = await i.inner_text()
#         if text ==  "books for kids 9-12 years":
#             await i.click()
#             break
#     assert await search_box.input_value() ==   "books for kids 9-12 years"

# @pytest.mark.asyncio
# async def test_dynamic_dropdown(async_page):
#     await async_page.goto("https://www.amazon.in/")
#     search_box = async_page.locator("//input[@id='twotabsearchtextbox']")
#     await search_box.fill("Books")
#     await async_page.wait_for_timeout(5000)
#
#     ops =   async_page.locator("//div[@class='s-suggestion-container']")
#     allops = await ops.all_text_contents()
#     print(allops)
#     op =  await ops.all()# all op ele
#     for i in op:
#         text = await i.inner_text()
#         if text ==  "books for kids 9-12 years":
#             await i.click()
#             break
#     else:
#         print("op not match")
#     assert await search_box.input_value() ==   "books for kids 9-12 years"

# @pytest.mark.asyncio
# async def test_check_box(async_page):
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     check_locator = async_page.locator("//div[@class='form-check form-check-inline']//input[@type='checkbox']/following-sibling::label")
#     await expect(check_locator.first).not_to_be_checked()
#     await check_locator.first.check()
#     await expect(check_locator.first).to_be_checked()
#     all_check_boxes = await check_locator.all_inner_texts()
#     print(all_check_boxes)
#
#
#
# @pytest.mark.asyncio
# async def test_check_box_input_list(async_page):
#     text_check_box = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     for i in text_check_box:
#         check_locator = async_page.locator(f"//input[@id='{i.lower()}']")
#         await expect(check_locator).not_to_be_checked()
#         await check_locator.check()
#         await expect(check_locator).to_be_checked()


# import pytest
# from playwright.async_api import expect
#
#
# @pytest.mark.asyncio
# async def test_check_box_input_list(async_page):
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     async_page.once(
#         "dialog",lambda dialog:(
#            print("type of alert = " , dialog.type),
#             print("msg = " , dialog.message),
#             dialog.accept()
#         )
#     )
#     await async_page.get_by_text("Simple Alert").click()
#
#     ele = async_page.locator("#sunday")
#     await  expect(ele).not_to_be_checked()
#     await ele.click()
#     await  expect(ele).to_be_checked()

# async def handle_aletrs(dialog):
#     print("alert type = " , dialog.type)
#     print("alter msg" , dialog.message)
#     await dialog.accept()
#
#
# @pytest.mark.asyncio
# async def test_check_box_input_list(async_page):
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     async_page.on("dialog", handle_aletrs)
#     await async_page.get_by_text("Simple Alert").click()
#
#     ele = async_page.locator("#sunday")
#     await  expect(ele).not_to_be_checked()
#     await ele.click()
#     await  expect(ele).to_be_checked()

# async def handle_aletrs(dialog):
#     print("alert type = ", dialog.type)
#     print("alter msg", dialog.message)
#     await dialog.accept()
#
#
# @pytest.mark.asyncio
# async def test_alert(async_page):
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     async_page.on("dialog", handle_aletrs)
#     await async_page.get_by_text("Confirmation Alert").click()
#
#     ele = async_page.locator("#sunday")
#     await  expect(ele).not_to_be_checked()
#     await ele.click()
#
#     async def handle_aletrs(dialog):
#         print("alert type = ", dialog.type)
#         print("alter msg", dialog.message)
#         await dialog.accept()

?