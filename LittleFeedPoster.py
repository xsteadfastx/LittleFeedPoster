import feedparser
from time import sleep


class LittleFeedPoster(object):
    def __init__(self, FeedName, FeedURL):
        self.FeedURL = FeedURL
        self.FeedName = FeedName
        self.OldFeed = feedparser.parse(self.FeedURL)
        self.OldEntry = self.OldFeed['entries'][0]['link']

    def NewItem(self):
        self.NewFeed = feedparser.parse(self.FeedURL)
        NewEntry = self.NewFeed['entries'][0]['link']
        if NewEntry != self.OldEntry:
            self.OldEntry = NewEntry
            return True
        else:
            return False

    def SendNewItem(self):
        if self.NewItem():
            message = self.NewFeed['entries'][0]['title'] + ' ' + self.NewFeed['entries'][0]['link']
            print message
        else:
            pass

def ReadFeedFile(FileName):
    feeds = {}
    with open(FileName, 'r') as FeedList:
        for line in FeedList:
            (key, value) = line.split(' ')
            feeds[key] = value
    return feeds

def GenerateFeeds(FeedList):
    MyFeeds = []
    for key, value in FeedList.items():
        NewFeed = LittleFeedPoster(key, value)
        MyFeeds.append(NewFeed)
    return MyFeeds

if __name__ == "__main__":
    MyFeedList = ReadFeedFile('feeds.list')
    MyFeeds = GenerateFeeds(MyFeedList)

    while True:
        for feed in MyFeeds:
            feed.SendNewItem()
        sleep(60)
