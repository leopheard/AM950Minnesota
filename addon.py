from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL1 = "https://rss.art19.com/stephanie-millers-happy-hour-podcast"
URL2 = "https://next.podbay.fm/podcast/1458666669"
URL3 = "http://www.am950radio.com/category/podcasts/atheists-talk/feed/"
URL4 = "http://www.am950radio.com/category/podcasts/accomplishers/feed/"
URL5 = "http://www.am950radio.com/category/podcasts/best-of-interviews/feed/"
URL6 = "http://weactradio.libsyn.com/rss"
URL7 = "https://www.bradblog.com/podcastgen/bradcast/feed.xml"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(10000), 
            'path': "http://am950radio.com/stream.m3u",
            'thumbnail': "http://www.am950radio.com/wp-content/uploads/2016/07/AM-simple-logo-white.png", 
            'is_playable': True},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://content.production.cdn.art19.com/images/5f/c5/af/0e/5fc5af0e-b096-4aa4-ace8-68153018dfe3/b6e871ec40e5529fc31fb1e93ecce7cb6fbebe3ef22a62c2b4691c22c973a7a986e6566916aedc6f6963957a73d68fe12ab842ee18dd7c7b76e052be5da2e23d.jpeg"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('all_episodes2'),
            'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Music123/v4/14/18/f0/1418f032-425f-8d31-9473-f310edf32d4b/source/400x400bb.jpg"},
        {
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('all_episodes3'),
            'thumbnail': "http://www.am950radio.com/wp-content/uploads/2017/09/atheists.jpg"},
        {
            'label': plugin.get_string(30004), 
            'path': plugin.url_for('all_episodes4'),
            'thumbnail': "http://www.am950radio.com/wp-content/uploads/2019/04/MISSION-ACCOMPLISHERS-large-only-for-itunes-dont-use.jpg"},
        {
            'label': plugin.get_string(30005), 
            'path': plugin.url_for('all_episodes5'),
            'thumbnail': "http://www.am950radio.com/wp-content/uploads/2018/04/Best-of-1400.jpg"},
        {
            'label': plugin.get_string(30006), 
            'path': plugin.url_for('all_episodes6'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/8/a/b/1/8ab1668ee74fb2c0/logo-print_NEW.jpg"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('all_episodes7'),
            'thumbnail': "http://bradblog.com/podcastgen/bradcast/images/itunes_image.jpg"},
    ]
    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/all_episodes2/')
def all_episodes2():
    soup2 = mainaddon.get_soup2(URL2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/all_episodes3/')
def all_episodes3():
    soup3 = mainaddon.get_soup3(URL3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

@plugin.route('/all_episodes4/')
def all_episodes4():
    soup4 = mainaddon.get_soup4(URL4)
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items

@plugin.route('/all_episodes5/')
def all_episodes5():
    soup5 = mainaddon.get_soup5(URL5)
    playable_podcast5 = mainaddon.get_playable_podcast3(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items

@plugin.route('/all_episodes6/')
def all_episodes6():
    soup6 = mainaddon.get_soup6(URL6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items

@plugin.route('/all_episodes7/')
def all_episodes7():
    soup7 = mainaddon.get_soup6(URL7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7)
    items = mainaddon.compile_playable_podcast6(playable_podcast7)
    return items

if __name__ == '__main__':
    plugin.run()
