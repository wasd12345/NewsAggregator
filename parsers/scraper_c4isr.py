from parsers.Scraper import Scraper


def scraper_c4isr(browser, **kwargs):
    """
    Scraper function for the website:
        https://www.c4isrnet.com/
        
    which is a Defense industry related news website. Read more about it here:
        https://en.wikipedia.org/wiki/C4ISRNET


    inputs:
        browser - a Selenium browser object, initialized in the main code as:
            browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
            
        kwargs - dict of the relevant parameters for parsing
            
        
    outputs:
        (content, success) - tuple of content (string) and success (boolean).
        content is string containing the parsed information
        success is boolean. True if parsing completed successfully, False otherwise.
        If False, the content will NOT be included in the final email/text message.
    """
    
    # Hard coded params specific to space.com news website:
    URL = 'https://www.c4isrnet.com/'
    articles_inds = [i for i in range(1,8)] # has ~7 articles
    title_xpath = '//*[@id="f0OvfQZXoM31Zr"]/div/ul/li[{ARTICLE_INDEX}]/article/div[3]/div/h5/a'
    abstract_xpath = '//*[@id="f0OvfQZXoM31Zr"]/div/ul/li[{ARTICLE_INDEX}]/article/div[3]/div/p'
    author_time_xpath = '//*[@id="f0OvfQZXoM31Zr"]/div/ul/li[{ARTICLE_INDEX}]/article/div[3]/div/div'
    
        
    #Params from kwargs:
    TITLES_ONLY = kwargs['titles_only']
    index_template = '{ARTICLE_INDEX}'
    params = {'browser':browser, 'url':URL, 'titles_only':TITLES_ONLY,
              'index_template':index_template,
              'title_xpath': title_xpath,
              'abstract_xpath': abstract_xpath,
              'author_time_xpath': author_time_xpath,
              'articles_inds': articles_inds}
    
    #Do the actual parsing:
    sc = Scraper(**params)
    
    return sc.scrape_data() #(content, success)    