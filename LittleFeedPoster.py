import feedparser
from time import sleep


class LittleFeedPoster(object):
    def __init__(self, feed_name, feed_url):
        self.feed_url = feed_url
        self.feed_name = feed_name
        self.old_feed = feedparser.parse(self.feed_url)
        self.old_entry = self.old_feed['entries'][0]['link']

    def has_new_item(self):
        self.new_feed = feedparser.parse(self.feed_url)
        new_entry = self.new_feed['entries'][0]['link']
        if new_entry != self.old_entry:
            self.old_entry = new_entry
            return True
        else:
            return False

    def send_new_item(self):
        if self.has_new_item():
            message = self.new_feed['entries'][0]['title'] + ' ' + self.new_feed['entries'][0]['link']
            print message
        else:
            pass

def read_feed_file(file_name):
    feeds = {}
    with open(file_name, 'r') as feed_list:
        for line in feed_list:
            (key, value) = line.split(' ')
            feeds[key] = value
    return feeds

def generate_feeds(feed_list):
    my_feeds = []
    for key, value in feed_list.items():
        new_feed = LittleFeedPoster(key, value)
        my_feeds.append(new_feed)
    return my_feeds

if __name__ == "__main__":
    my_feed_list = read_feed_file('feeds.list')
    my_feeds = generate_feeds(my_feed_list)

    while True:
        for feed in my_feeds:
            feed.send_new_item()
        sleep(60)
