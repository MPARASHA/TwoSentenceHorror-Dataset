import json

with open('./data/twosentencehorror_subs.json') as fi:
        fo = open('./data/twosentencehorror_filtered.json', 'w')
        data = json.load(fi)

        count = 0
        goodStories = []

        for story in data:
            if len(story["selftext"]) < 500 and "\n" not in story["selftext"] and "[removed]" not in story["selftext"]:
                storyFormat = {}
                storyFormat["title"] = story["title"]
                storyFormat["body"] = story["selftext"]
                storyFormat["score"] = int(story["score"])
                storyFormat["link"] = story["full_link"]
                goodStories.append(storyFormat)
                count+=1
        
        goodStoriesJson = json.dumps(goodStories, indent=4, sort_keys=True)
        fo.write(goodStoriesJson)
        print(count)