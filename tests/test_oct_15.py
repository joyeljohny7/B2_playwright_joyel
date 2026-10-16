import pytest

# @pytest.mark.asyncio
# async def test_drag_and_drop(async_page):
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     s = async_page.locator("//div[@id = 'draggable']")
#     d = async_page.locator("//div[@id = 'droppable']")
#     await s.drag_to(d)

# @pytest.mark.asyncio
# async def test_scroll(async_page):
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     s = async_page.locator("//div[@id = 'draggable']")
#     await s.scroll_into_view_if_needed()
#     d = async_page.locator("//div[@id = 'droppable']")
#     await s.drag_to(d)

# @pytest.mark.asyncio
# async def test_scroll(async_page):
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     s = async_page.locator("//div[@id = 'draggable']")
#     await s.scroll_into_view_if_needed()
#     d = async_page.locator("//div[@id = 'droppable']")
#     await s.drag_to(d)
#     await async_page.mouse.wheel(0,1000)
#     await async_page.wait_for_timeout(500)
#     await async_page.mouse.wheel(0,-1000)
#     await async_page.wait_for_timeout(5000)

# @pytest.mark.asyncio
# async def test_scroll_infinite(async_page):
#     await async_page.goto("https://www.playwrightautomation.com/infinite-scroll.html")
#     loading = async_page.locator("//div[@id='loading-indicator']")
#     end_of_catalog = async_page.get_by_text("End of Catalog")
#     scroll = async_page.locator("#scroll-sentinel")
#
#     while(True):
#        try:
#             if await end_of_catalog.is_visible():
#                 print("scroll till end")
#                 break
#        except Exception as e:
#            await scroll.scroll_into_view_if_needed()
#            print("one more scroll needed")
#            await async_page.wait_for_timeout(5000)

# @pytest.mark.asyncio
# async def test_date_picker(async_page):
#     await async_page.goto("https://jqueryui.com/datepicker/")
#     fl = async_page.frame_locator("demo-frame")
#     date = fl.locator("//input[@id='datepicker']")
#     await date.click()
#     day = fl.locator("//a[text()='17']")
#     await day.click()


# @pytest.mark.asyncio
# async def test_date_picker(async_page):
#     await async_page.goto("https://jqueryui.com/datepicker/")
#     fl = async_page.frame_locator(".demo-frame")
#     date = fl.locator("//input[@id='datepicker']")
#     await date.click()
#     day = fl.locator("//a[text()='17']")
#     await day.click()
#     #//input[@id='datepicker']


# @pytest.mark.asyncio
# async def test_date_picker(async_page):
#     um = "December"
#     uy = "2026"
#     ud = "12"
#
#     await async_page.goto("https://jqueryui.com/datepicker/")
#     fl = async_page.frame_locator(".demo-frame")
#     date = fl.locator("//input[@id='datepicker']")
#     await date.click()
#
#     cm = await fl.locator(".ui-datepicker-month").inner_text()
#     cy = await fl.locator(".ui-datepicker-year").inner_text()
#     print(cm)
#     print(cy)
#     while (True):
#         if (uy == cy and um == cm):
#             await fl.locator(f"//a[text()='{ud}']").click()
#             break
#
#         await fl.locator("//span[text()='Next']").click()
#         cm = await fl.locator(".ui-datepicker-month").inner_text()
#         cy = await fl.locator(".ui-datepicker-year").inner_text()

# @pytest.mark.asyncio
# async def test_range_slider(async_page):
#     await async_page.goto("https://jqueryui.com/resources/demos/slider/range.html?utm_source")
#     min = 100
#     max = 400
#
#     slider = async_page.locator("//div[@id='slider-range']/span")
#     await slider.nth(0).focus()
#     await slider.nth(0).press("Home")
#
#     for i in range(min):
#         await slider.nth(0).press("ArrowRight")
#
#     await slider.nth(1).focus()
#     await slider.nth(1).press("End")
#     for i in range(500,max):
#         await slider.nth(0).press("ArrowLeft")


@pytest.mark.asyncio
async def test_end_to_end(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")

    # =============================================================================
    # ====================== Reg
    # =================================================================================
    await async_page.locator("//a[text()='Register']").click()
    await async_page.get_by_label("First name:").fill("abc")
    await async_page.get_by_label("Last name:").fill("abc")
    await async_page.get_by_label("Email:").fill("abcd1234@gmail.com")
    await async_page.get_by_label("Password:").nth(0).fill("abc@123")
    await async_page.get_by_label("Confirm password:").fill("abc@123")
    await async_page.locator("#register-button").click()

    try:
        await async_page.get_by_text("Log out").is_visible()

    except Exception:
          print(await async_page.locator("//span[@class='field-validation-error']").all_text_contents())

    # =============================================================================
    # ====================== login
    # =================================================================================
    await async_page.get_by_text("Log in").click()
    await async_page.get_by_label("Email:").fill("joyeljohny@gmail.com")
    await async_page.get_by_label("Password:").fill("abc@123")
    await async_page.locator("//input[@value='Log in']").click()
    try:
        await async_page.get_by_text("Log out").is_visible()

    except Exception:
        print(await async_page.locator("//span[@class='field-validation-error']").all_text_contents())