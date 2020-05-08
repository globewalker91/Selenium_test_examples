#execute $ python -m unittest -v test_basic_search.GoogleSearch

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class GoogleSearch(unittest.TestCase):
    """
    1. open google.com
    2. search for a term
    3. Get the search result count and search time from "About 531,000,000 results (0.62 seconds)"
    4. Get a list of urls from the first page of results.

    """
    def test_verify_google_search(self):
        # create chromedriver instance and goto google.com
        self.driver = webdriver.Firefox()
#        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com/')

        # get the search box element, enter term = "Selenium" and hit the enter key to initiate search
        search_box = self.driver.find_element_by_css_selector('input[aria-label="Search"]')
        search_box.send_keys('python')
        search_box.send_keys(Keys.ENTER)

        # find the result stats element, convert it to text
        self.driver.implicitly_wait(10)
        results = self.driver.find_element_by_id('result-stats')
        results_text = results.text

        # print out the results text (just for debug purposes)
        print(results_text)
        x = results_text.split()
#        print(x)
        how_many = x[1].replace(',', '')
        how_long = x[3].replace('(', '')
        print('Returned', how_many, 'results')
        print('Took', how_long, 'seconds')

        # assert some value
        self.assertTrue(results_text)
        self.assertGreater(int(how_many), 99999)
        self.assertLess(float(how_long), 5)

        # get all url/url text and print
        url_text = [x.text for x in self.driver.find_elements_by_css_selector('a[href^="http"] h3') if x.text]
        for index, url in enumerate(url_text):
            print('\n{}. {}'.format(index+1, url))
            self.assertIn('python'.upper(), url.upper())

        # assert some value
        self.assertGreater(len(url_text), 5)
        self.driver.implicitly_wait(10)

        self.driver.quit()


#execute $ python -m unittest -v test_basic_search.GoogleSearch