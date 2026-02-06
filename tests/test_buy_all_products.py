import time
import datetime
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

from pages.base_page import BasePage
from pages.cart_page import Cart_page
from pages.main import MainPage

from pages.Samsung_galaxy_s6_page import Samsung_s6_Page
from pages.samsung_galaxy_s7_page import Samsung_s7_Page
from pages.nokia_lumia_page import Nokia_Lumia_Page
from pages.nexus_6_page import Nexus_page
from pages.iphone6_32_page import Iphone6_32_Page
from pages.sony_xperia_z5_page import Sony_xperia_z5
from pages.htc_one_m9_page import Htc_one_m9

from pages.sony_vaio_i5_page import Sony_vaio_i5
from pages.sony_vaio_i7_page import Sony_vaio_i7
from pages.macbook_air_page import Macbook_air
from pages.dell_i7_page import Dell_i7
from pages.dell_2017_page import Dell_2017
from pages.macbook_pro_page import Macbook_pro

from pages.apple_monitor_24_page import Apple_monitor_24
from pages.asus_full_hd_page import Asus_full_hd


def test_buy_all(browser):
    m = MainPage(browser)
    m.open()
    print('Home page open')

    # Add to cart phones
    m.click_phones()
    print('Phones category open')

    # add to cart samsung galaxy s6
    m.click_sgs6()
    print('Click samsung galaxy s6')
    sgs6 = Samsung_s6_Page(browser)
    sgs6.click_sgs6()
    print('add to cart samsung galaxy s6')
    m.go_back()
    print('back to home')

    # add to cart nokia lumia
    m.click_nokia()
    print('Click nokia lumia')
    nokia = Nokia_Lumia_Page(browser)
    nokia.click_nokia()
    print('add to cart samsung galaxy s6')
    m.go_back()
    print('back to home')

    # add to cart  nexus 6
    m.click_nexus()
    print('Click nexus 6')
    nexus = Nexus_page(browser)
    nexus.click_nexus()
    print('add to cart nexus 6')
    m.go_back()
    print('back to home')

    # add to cart samsung galaxy s7
    m.click_sgs7()
    print('Click samsung galaxy s7')
    sgs7 = Samsung_s7_Page(browser)
    sgs7.click_sgs7()
    print('add to cart samsung galaxy s7')
    m.go_back()
    print('back to home')

    # add to cart iphone 6 32gb
    m.click_iphone6_32()
    print('Click iphone 6 32gb')
    iphone = Iphone6_32_Page(browser)
    iphone.click_iphone6_32()
    m.click_iphone6_32()
    print('add to cart iphone 6 32gb')
    m.go_back()
    print('back to home')

    # add to cart sony xperia z5
    m.click_sony_xperia_z5()
    print('Click sony xperia z5')
    xperia = Sony_xperia_z5(browser)
    xperia.click_sxz5()
    print('add to cart sony xperia z5')
    m.go_back()
    print('back to home')

    # add to cart HTC One M9
    m.click_htc_one_m9()
    print('Click sony HTC One M9')
    htc = Htc_one_m9(browser)
    htc.click_htc()
    m.click_htc_one_m9()
    print('add to cart HTC One M9')
    m.go_back()
    print('back to home')


    # add to cart laptops
    m.click_laptops()

    # add to cart Sony vaio i5
    m.click_sony_vaio_i5()
    print('Click Sony vaio i5')
    vaio_i5 =Sony_vaio_i5(browser)
    vaio_i5.click_svi5()
    print('add to cart Sony vaio i5')
    m.go_back()
    print('back to laptops category')

    # add to cart Sony vaio i7
    m.click_sony_vaio_i7()
    print('Click Sony vaio i7')
    vaio_i7 = Sony_vaio_i7(browser)
    vaio_i7.click_svi7()
    print('add to cart Sony vaio i7')
    m.go_back()
    print('back to laptops category')


    # add to cart Sony Macbook Air
    m.click_macbook_air()
    print('Click Sony Macbook Air')
    mair = Macbook_air(browser)
    mair.click_macbook_air()
    print('add to cart Macbook Air')
    m.go_back()
    print('back to laptops category')

    # add to cart Dell i7 8gb
    m.click_dell_i7()
    print('Click Dell i7 8gb')
    dell_i7 = Dell_i7(browser)
    dell_i7.click_dell_i7()
    print('add to cart Dell i7 8gb')
    m.go_back()
    print('back to laptops category')

    # add to cart Dell 2017
    m.click_dell_2017()
    print('Click Dell 2017')
    dell_2017 = Dell_2017(browser)
    dell_2017.click_dell_2017()
    print('add to cart Dell 2017')
    m.go_back()
    print('back to laptops category')

    # add to cart Sony Macbook Pro
    m.click_macbook_pro()
    print('Click Sony Macbook Pro')
    mpro = Macbook_pro(browser)
    mpro.click_macbook_pro()
    print('add to cart Macbook Pro')
    m.go_back()
    print('back to laptops category')



    # add to cart monitors
    m.click_monitor_category()
    print('Monitors category open')

    # add to cart Apple monitor 24
    m.click_apple_monitor_24()
    print('Click Apple monitor 24')
    am24 = Apple_monitor_24(browser)
    am24.click_apple_monitor_24()
    print('add to cart Apple monitor 24')
    m.go_back()
    print('back to monitors category')

    # add to cart Asus Full HD
    m.click_asus_full_hd()
    print('Click Asus Full HD')
    afh = Asus_full_hd(browser)
    afh.click_asus_full_hd()
    print('add to cart Asus Full HD')
    m.go_back()
    print('back to monitors category')

    m.click_cart()
    print('Click cart')

    time.sleep(2)




    # Assert info in cart

    # Assert PHONES

    # Assert Samsung galaxy s6
    m.assert_values(word=sgs6.get_samsung_name(), result="Samsung galaxy s6")
    print('sgs6 Name good')

    price_360 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '360')]")
    m.assert_values(price_360, "360")
    print('sgs6 Price good')


    # Assert Nokia lumia
    m.assert_values(word=nokia.get_nokia_name(), result="Nokia lumia 1520")
    print('Name good')

    price_820 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '820')]")
    m.assert_values(price_820, "820")
    print('Price good')


    # Assert Nexus
    m.assert_values(word=nexus.get_nexus_name(), result="Nexus 6")
    print('Name good')

    price_650 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '650')]")
    m.assert_values(price_650, "650")
    print('Price good')


    # Assert sgs7
    m.assert_values(word=sgs7.get_name_s7(), result="Samsung galaxy s7")
    print('Name good')

    price_800 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '800')]")
    m.assert_values(price_800, "800")
    print('Price good')


    # Assert Iphone 6
    m.assert_values(word=iphone.get_iphone_name(), result="Iphone 6 32gb")
    print('Name good')

    price_790 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '790')]")
    m.assert_values(price_790, "790")
    print('Price good')


    # Assert Sony xperia z5
    m.assert_values(word=xperia.get_sony_xperia_name(), result="Sony xperia z5")
    print('Name good')

    price_320 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '320')]")
    m.assert_values(price_320, "320")
    print('Price good')


    # Assert
    m.assert_values(word=htc.get_htc_name(), result="HTC One M9")
    print('Name good')

    price_700 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '700')]")
    m.assert_values(price_700, "700")
    print('Price good')





    # Assert LAPTOPS

    # Assert Sony vaio i5
    m.assert_values(word=vaio_i5.get_name_svi5(), result="Sony vaio i5")
    print('Name good')

    price_790 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '790')]")
    m.assert_values(price_790, "790")
    print('Price good')


    # Asserty sony vaio i7
    m.assert_values(word=vaio_i7.get_name_svi7(), result="Sony vaio i7")
    print('Name good')

    price_790 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '790')]")
    m.assert_values(price_790, "790")
    print('Price good')


    # Assert Macbook Air
    m.assert_values(word=mair.get_macbook_air_name(), result="MacBook air")
    print('Name good')

    price_700 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '700')]")
    m.assert_values(price_700, "700")
    print('Price good')


    # Assert Dell i7
    m.assert_values(word=dell_i7.get_dell_i7_name(), result="Dell i7 8gb")
    print('Name good')

    price_700 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '700')]")
    m.assert_values(price_700, "700")
    print('Price good')



    # Assert Dell 2017
    m.assert_values(word=dell_2017.get_dell_2017_name(), result="2017 Dell 15.6 Inch")
    print('Name good')

    price_700 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '700')]")
    m.assert_values(price_700, "700")
    print('Price good')


    # Macbook Pro
    m.assert_values(word=mpro.get_macbook_pro_name(), result="MacBook Pro")
    print('Name good')

    price_1100 = browser.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[contains(text(), '1100')]")
    m.assert_values(price_1100, "1100")
    print('Price good')


    cp = Cart_page(browser)
    cp.click_order_button()

    print('Click Place Order')

    cp.send_info()
    print('Information is written')

    cp.click_purchase()
    print('Click Purchase')

    m.assert_values(cp.get_success_text(), 'Thank you for your purchase!')
    print('Success text good')

    time.sleep(1)

    cp.click_ok()
    print('Click ok')

    WebDriverWait(browser, 15).until(Ec.url_to_be("https://www.demoblaze.com/index.html"))
    assert browser.current_url == "https://www.demoblaze.com/index.html"
    print('Home page')