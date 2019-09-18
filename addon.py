from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://rss.art19.com/stephanie-millers-happy-hour-podcast"
url2 = "https://rss.art19.com/the-randi-rhodes-after-hours-podcast"
url3 = "http://www.am950radio.com/category/podcasts/atheists-talk/feed/"
url4 = "http://www.am950radio.com/category/podcasts/accomplishers/feed/"
url5 = "http://www.am950radio.com/category/podcasts/best-of-interviews/feed/"
url6 = "http://weactradio.libsyn.com/rss"
url7 = "https://www.bradblog.com/podcastgen/bradcast/feed.xml"
url8 = "https://rss.art19.com/the-hartmann-report"
url9 = "http://feeds.soundcloud.com/users/soundcloud:users:69152263/sounds.rss"
url10 = "http://feeds.feedburner.com/davidpakmanshow"
url11 = "https://www.democracynow.org/podcast.xml"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': "http://am950radio.com/stream.m3u",
            'thumbnail': "http://www.am950radio.com/wp-content/uploads/2016/07/AM-simple-logo-white.png", 
            'is_playable': True},
        {
            'label': plugin.get_string(30009),
            'path': plugin.url_for('episodes9'),
            'thumbnail': "https://is1-ssl.mzstatic.com/image/thumb/Podcasts123/v4/4a/8c/26/4a8c26f3-736d-941f-e616-a9e9c61b0de1/mza_2910619107549141.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Music123/v4/14/18/f0/1418f032-425f-8d31-9473-f310edf32d4b/source/400x400bb.jpg"},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://content.production.cdn.art19.com/images/5f/c5/af/0e/5fc5af0e-b096-4aa4-ace8-68153018dfe3/b6e871ec40e5529fc31fb1e93ecce7cb6fbebe3ef22a62c2b4691c22c973a7a986e6566916aedc6f6963957a73d68fe12ab842ee18dd7c7b76e052be5da2e23d.jpeg"},
        {
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('episodes3'),
            'thumbnail': "http://www.am950radio.com/wp-content/uploads/2017/09/atheists.jpg"},
        {
            'label': plugin.get_string(30004), 
            'path': plugin.url_for('episodes4'),
            'thumbnail': "http://www.am950radio.com/wp-content/uploads/2019/04/MISSION-ACCOMPLISHERS-large-only-for-itunes-dont-use.jpg"},
        {
            'label': plugin.get_string(30005), 
            'path': plugin.url_for('episodes5'),
            'thumbnail': "http://www.am950radio.com/wp-content/uploads/2018/04/Best-of-1400.jpg"},
        {
            'label': plugin.get_string(30006), 
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/8/a/b/1/8ab1668ee74fb2c0/logo-print_NEW.jpg"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('episodes7'),
            'thumbnail': "http://bradblog.com/podcastgen/bradcast/images/itunes_image.jpg"},
        {
            'label': plugin.get_string(30008),
            'path': plugin.url_for('episodes8'),
            'thumbnail': "https://is2-ssl.mzstatic.com/image/thumb/Podcasts123/v4/61/16/2f/61162f9a-0e85-1706-d763-391945aa49a6/mza_6098482171161442518.jpeg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30010),
            'path': plugin.url_for('episodes10'),
            'thumbnail': "http://static.libsyn.com/p/assets/7/2/8/0/72802e4963645d76/DPS_Podcast_new.jpg"},
        {
            'label': plugin.get_string(30011),
            'path': plugin.url_for('episodes11'),
            'thumbnail': "http://assets.democracynow.org/assets/DN-Podcast-AUDIO-1d5df65d8936dcfd1387274443b3e0713c5f15dd3fa400331229f4ab39b5c19e.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items

@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items

@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(url6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items

@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(url7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7)
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items

@plugin.route('/episodes8/')
def episodes8():
    soup8 = mainaddon.get_soup8(url8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items

@plugin.route('/episodes9/')
def episodes9():
    soup9 = mainaddon.get_soup9(url9)
    playable_podcast9 = mainaddon.get_playable_podcast9(soup9)
    items = mainaddon.compile_playable_podcast9(playable_podcast9)
    return items

@plugin.route('/episodes10/')
def episodes10():
    soup10 = mainaddon.get_soup10(url10)
    playable_podcast10 = mainaddon.get_playable_podcast10(soup10)
    items = mainaddon.compile_playable_podcast10(playable_podcast10)
    return items

@plugin.route('/episodes11/')
def episodes11():
    soup11 = mainaddon.get_soup11(url11)
    playable_podcast11 = mainaddon.get_playable_podcast11(soup11)
    items = mainaddon.compile_playable_podcast11(playable_podcast11)
    return items

if __name__ == '__main__':
    plugin.run()
