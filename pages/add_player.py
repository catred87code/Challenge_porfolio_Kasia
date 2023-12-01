import time

from pages.base_page import BasePage

class AddPlayer(BasePage):
    add_player_xpath = "//span[contains(text(), 'Add')]"
    add_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    expected_title = "Add player"


    def click_add_player(self):
        self.click_on_the_element(self.add_player_xpath)

    def title_of_page(self):
        #time.sleep(4)
        assert self.get_page_title(self.add_url) == self.expected_title

