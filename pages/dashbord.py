import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    panel_xpath = "//h6[text() = 'Scouts Panel']"
    expected_panel_element_text = "Scouts Panel"
    players_menu_xpath = "//*[text()='Players']"
    language_menu_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_menu_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    contact_form_xpath = "//span[contains(text(), 'contact')]"
    add_player_xpath = "//span[contains(text(), 'Add')]"
    last_created_player_button_xpath = "//*[text() = 'Last created player']//following :: button[1]"
    last_updated_player_xpath = "//*[text() = 'Last updated player']//following :: button[1]"
    last_created_match_xpath = "//*[text() = 'Last created match']//following :: button[1]"
    last_updated_match_xpatch = "//*[text() = 'Last updated match']//following :: button[1]"
    last_updated_report_xpath = "//*[text() = 'Last updated report']//following :: button[1]"
    #pass

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def panel_check(self):
        time.sleep(4)
        self.assert_element_text(self.driver, self.panel_xpath, self.expected_panel_element_text)


