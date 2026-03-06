from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class BookingPage(BasePage):

    # Nagłówek strony rezerwacji – używany do sprawdzenia, czy strona się załadowała.
    HEADER = (By.XPATH, '//h2[contains(text(), "Book this room")]')

    # Pole "First name" w formularzu.
    FIRST_NAME = (By.XPATH, '//input[@id="firstname"]')

    # Przycisk "Submit" wysyłający formularz.
    SUBMIT_BUTTON = (By.XPATH, '//button[contains(text(), "Submit")]')

    # Sprawdza, czy strona rezerwacji jest widoczna.
    # Używa is_visible() z BasePage.
    def is_loaded(self):
        return self.is_visible(self.HEADER)

    # Wpisuje imię do pola "First name".
    # Używa type() z BasePage.
    def fill_first_name(self, name):
        self.type(self.FIRST_NAME, name)

    # Kliknięcie przycisku "Submit".
    # Używa click() z BasePage.
    def submit(self):
        self.click(self.SUBMIT_BUTTON)