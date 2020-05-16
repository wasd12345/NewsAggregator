from selenium import webdriver
from time import sleep


class Scraper():
    """
    Base Class for Web Scraper object
    
    
    inputs:
        browser - a Selenium browser object, initialized in the main code as:
            browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
            
    outputs:
        (content, success) - tuple of content (string) and success (boolean).
        content is string containing the parsed information
        success is boolean. True if parsing completed successfully, False otherwise.
        If False, the content will NOT be included in the final email/text message.
    """
    
    def __init__(self, **kwargs):
        self.browser = kwargs['browser']
        self.url = kwargs['url']
        # self.n_articles = kwargs['n_articles']
        self.articles_inds = kwargs['articles_inds'] #e.g. [1,2,3,...] in general vs. [1,3,4,5,...] for space.com
        self.titles_only = kwargs['titles_only']
        self.success = False
        self.CSS_vs_XPATH = 'XPATH' #'CSS'
        
        self.index_template = kwargs['index_template'] #e.g. '{ARTICLE_INDEX}'
        self.title_xpath = kwargs['title_xpath']
        self.abstract_xpath = kwargs['abstract_xpath']
        self.author_time_xpath = kwargs['author_time_xpath']
        
        self.content = ''

        
    def scrape_data(self):
        # Go to the website in Selenium browser
        self.browser.get(self.url)
        sleep(15) #Sleep a while since lots of graphics which may be slow to load
        for ii in self.articles_inds:
            try:
                if self.CSS_vs_XPATH == 'XPATH':
                    selector_title = self.title_xpath.replace(self.index_template, str(ii))
                    title = self.browser.find_element_by_xpath(selector_title)                
                    if not self.titles_only:
                        selector_abstract = self.abstract_xpath.replace(self.index_template, str(ii))
                        selector_author_time = self.author_time_xpath.replace(self.index_template, str(ii))
                        abstract = self.browser.find_element_by_xpath(selector_abstract)
                        author_time = self.browser.find_element_by_xpath(selector_author_time)        
                title = title.text
                if not self.titles_only:
                    abstract = abstract.text
                    author_time = author_time.text
                    self.content += f"{title}\n{abstract}\n{author_time}\n\n"
                else:
                    self.content += f"{title}\n\n"
            finally:
                sleep(.5)
        self.success = True
        return (self.content, self.success)