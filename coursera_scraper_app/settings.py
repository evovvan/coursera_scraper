BOT_NAME = 'coursera'
SPIDER_MODULES = ['coursera_scraper_app.spiders']
ITEM_PIPELINES = ['coursera_scraper_app.pipelines.Coursera_Pipline']
DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'nfarah86',
    'password': 'dogs123',
    'database': 'coursera_scraper_database'
}