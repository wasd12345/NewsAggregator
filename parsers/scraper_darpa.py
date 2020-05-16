from parsers.Scraper import Scraper


def scraper_darpa(browser, **kwargs):
    """
    Scraper function for the website:
        https://www.darpa.mil/news
        
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
    URL = 'https://www.darpa.mil/news?ppl=view16' #48
    articles_inds = [i for i in range(16)] # view w either 16 vs. 48 articles, 0 indexed
    title_xpath = '//*[@id="dnn_ctr441_SimpleList_dlListItems_liPM_{ARTICLE_INDEX}_aListingLink_{ARTICLE_INDEX}"]'
    abstract_xpath = '//*[@id="dnn_ctr441_SimpleList_dlListItems_liPM_{ARTICLE_INDEX}_divListingCopy_{ARTICLE_INDEX}"]'
    author_time_xpath = '//*[@id="dnn_ctr441_SimpleList_dlListItems_liPM_{ARTICLE_INDEX}_divListingDate_{ARTICLE_INDEX}"]'
    
    
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