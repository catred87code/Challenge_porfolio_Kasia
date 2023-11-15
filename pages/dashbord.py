from pages.base_page import BasePage


class Dashboard(BasePage):
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
    pass