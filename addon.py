from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

URL1 = "https://rss.art19.com/stephanie-millers-happy-hour-podcast"
URL2 = "https://next.podbay.fm/podcast/1458666669"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
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
    ]

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup1 = mainaddon.get_soup1(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items


@plugin.route('/all_episodes2/')
def all_episodes2():
    """
    contains playable podcasts listed as just-in
    """
    soup2 = mainaddon.get_soup2(URL2)
    
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    
    items = mainaddon.compile_playable_podcast2(playable_podcast2)

    return items


@plugin.route('/all_episodes3/')
def all_episodes3():
    """
    contains playable podcasts listed as just-in
    """
    soup3 = mainaddon.get_soup3(URL3)
    
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    
    items = mainaddon.compile_playable_podcast3(playable_podcast3)

    return items


if __name__ == '__main__':
    plugin.run()
