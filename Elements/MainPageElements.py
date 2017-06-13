class MainPageElements:

    def clickSeeNumberBtn(self):
        self.see_number_btn = self.driver.find_element_by_link_text("See a number").click()

    def clickInfoBtn(self):
        self.info_btn = self.driver.find_element_by_link_text("Info").click()

    def clickAnotherNumberBtn(self):
        self.another_number = self.driver.find_element_by_link_text("Another number").click()

    def clickBackToMainMenu(self):
        self.back_to_main = self.driver.find_element_by_link_text("Back to Main").click()
