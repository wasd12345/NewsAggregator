from parsers.Scraper import Scraper


def scraper_space(browser, **kwargs):
    """
    Scraper function for the website:
        https://www.space.com/news
        
    which is a space and astronomy news website. Read more about it here:
        https://en.wikipedia.org/wiki/Space.com


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
    URL = 'https://www.space.com/news'
    articles_inds = [i for i in range(1,21) if i!=2] # has ~20 articles and 2nd is an ad w/ different format
    title_xpath = '//*[@id="content"]/section/section/div[2]/div[{ARTICLE_INDEX}]/a/article/div[2]/header/h3'
    abstract_xpath = '//*[@id="content"]/section/section/div[2]/div[{ARTICLE_INDEX}]/a/article/div[2]/p'
    author_time_xpath = '//*[@id="content"]/section/section/div[2]/div[{ARTICLE_INDEX}]/a/article/div[2]/header/p'
    
        
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