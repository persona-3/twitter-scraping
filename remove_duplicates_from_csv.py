import pandas as pd

df = pd.read_csv(r'C:\Users\91893\Downloads\twitter_scraper\merged_login_data.csv')
print(len(df['wallet']))
df.drop_duplicates(inplace=True)
print(len(df['wallet']))
