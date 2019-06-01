import scrapy

print('PLEASE wait, while we are getting things ready!!!')

class PlayerSpider(scrapy.Spider):
    name = 'player'
    codes=[
        2,25,1,6,5,7,3,8,4,9,
        40,19,29,20,30,27,21,104,41,111,108,42,115,
        12,112,116,117,118,114,43,17,39,44,121,122,
        4082,123,125,126,13,129,4251,10,131,33,133,
        35,135,18,137,1094,142,148,147,22,31,36,4083,
        26,38,159,161,169,16,164,45,165,171,6411,28,32,
        15,173,175,37,183,178,179,185,187,191,192,154,
        194,196,23,197,195,200,201,202,4253,204,205,211,
        207,209,206,34,11,216,215,24,48
    ]
    classes=2
    start_urls=[]
    for code in codes:
        start_urls.append('http://www.espncricinfo.com/ci/content/player/caps.html?country={codeem};class={classem}'.format(codeem=code, classem=classes)) 

    def parse(self, response):
        for player in response.css('li.sep'):
            yield {
                'text': player.css('a.ColumnistSmry::text').get(),
                'link': player.css('a.ColumnistSmry::attr("href")').get(),
            }


