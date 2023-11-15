from pages.base_page import BasePage


class AddMatch(BasePage):
    my_team_input_xpath = "//input[@name= 'myTeam']"
    enemy_team_input_xpath = "//input[@name= 'enemyTeam']"
    my_team_score_input_xpath = "//input[@name= 'myTeamScore']"
    enemy_team_score_input_xpath = "//input[@name= 'enemyTeamScore']"
    date_input_xpath = "//input[@name= 'date']"
    radio_math_at_home_xpath = "//*[text()='Match at home']"
    radio_match_out_home_xpath = "//*[text()='Match out home']"
    tshirt_input_xpath = "//input[@name= 'tshirt']"
    league_input_xpath = "//input[@name= 'league']"
    time_layed_input_xpath = "//input[@name= 'timePlayed']"
    number_input_xpath = "//input[@name= 'number']"
    web_match_input_xpath = "//input[@name= 'webMatch']"
    general_input_xpatch = "//input[@name= 'general']"
    rating_input_xpath = "//input[@name= 'rating']"
    submit_button_xpath = "//button[contains (@class, 'MuiButton-containedPrimary')]"
    clear_button_xpath = "//button[contains (@class, 'MuiButton-containedSecondary')]"
    pass