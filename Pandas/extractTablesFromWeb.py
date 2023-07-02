#Extract CSV files and Tables from Websites
#https://en.wikipedia.org/wiki/Adventure_Time
import pandas as pd
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
print(simpsons[1].head())
