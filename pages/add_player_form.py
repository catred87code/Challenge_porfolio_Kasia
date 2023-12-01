from pages.base_page import BasePage
import time

class FillAddPlayerForm(BasePage):
    name_input_xpath = "//input[@name='name']"
    surname_input_xpath = "//input[@name='surname']"
    main_position_input_xpath = "//input[@name='mainPosition']"
    submit_button_xpath = "//button/span[text() = 'Submit']"
    age_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[7]/div/p"
    age_warning = "Required"
    clear_button_xpath = "//button/span[text() = 'Clear']"




    def type_in_name(self, name):
        self.field_send_keys(self.name_input_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_input_xpath, surname)

    def type_in_main_position(self, position):
        self.field_send_keys(self.main_position_input_xpath, position)

    def click_submit(self):
        self.click_on_the_element(self.submit_button_xpath)


    def age_check(self):
        self.wait_for_element_to_be_visible(self.submit_button_xpath)
        self.assert_element_text(self.driver, self.age_input_xpath, self.age_warning)

    def clear_form(self):
        self.click_on_the_element(self.clear_button_xpath)





