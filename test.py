import os
url = 'https://twitter.com/BornToDieGame/status/1627907110619996160'
csv_file_name = url.split('/')[3] + ".csv"

print(os.path.join(os.getcwd(), csv_file_name))