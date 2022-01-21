import pandas as pd

from pmaw import PushshiftAPI

api = PushshiftAPI()

submissions = api.search_submissions(subreddit="twosentencehorror", limit=30000)

sub_df = pd.DataFrame(submissions)

sub_df.to_csv('./data/twosentencehorror_subs.csv', header=True, index=False, columns=list(sub_df.axes[1]))
