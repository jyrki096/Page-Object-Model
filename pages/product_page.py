from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button has not found"
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def should_be_right_titles(self):
        book_name = self.browser.find_element(*ProductPageLocators.MAIN_TITLE).text
        book_basket = self.browser.find_element(*ProductPageLocators.BASKET_TITLE).text
        assert book_name == book_basket, "Name is not the same"

    def should_be_right_prices(self):
        book_name = self.browser.find_element(*ProductPageLocators.MAIN_PRICE).text
        book_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert book_name == book_basket, "Name is not the same"
