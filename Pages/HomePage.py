from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage


class HomePage(BasePage):
    # LOCAKALIZATORY

    URL = "https://automationintesting.online/"

    BOOK_NOW = (By.XPATH, "//a[contains(@href, '#booking')]")
    CHECK_AVAILABILITY = (By.XPATH, "//a[contains(@class,'openBooking')]")
    CHECK_IN = (By.XPATH, "//input[@id='checkin']")
    CHECK_OUT = (By.XPATH, "//input[@id='checkout']")
    WELCOME_TEXT = (By.XPATH, "//p[contains(@class,'lead')]")

    # METODY

    def open(self):
        self.driver.get(self.URL)

    def click_check_availability_to_booking(self):
        self.click(self.CHECK_AVAILABILITY)

    # Metoda sprawdzająca czy tekst się nie zmienił
    def get_text(self, locator):
        # Znajdujemy element na stronie
        element = self.driver.find_element(*locator)
        # Sprawdzamy, czy jest widoczny
        assert element.is_displayed()
        # Czekamy aż Selenium potwierdzi widoczność i zwracamy tekst
        return self.wait.until(EC.visibility_of_element_located(locator)).text