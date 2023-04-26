from urllib import request
import pandas as pd

AI = ['https://en.wikipedia.org/wiki/List_of_counties_in_Alabama', 'https://en.wikipedia.org/wiki/List_of_boroughs_and_census_areas_in_Alaska', 'https://en.wikipedia.org/wiki/List_of_counties_in_Arizona', 'https://en.wikipedia.org/wiki/List_of_counties_in_Arkansas',
        'https://en.wikipedia.org/wiki/List_of_counties_in_California', 'https://en.wikipedia.org/wiki/List_of_counties_in_Colorado', 'https://en.wikipedia.org/wiki/List_of_counties_in_Connecticut', 'https://en.wikipedia.org/wiki/List_of_counties_in_Delaware',
        'https://en.wikipedia.org/wiki/List_of_counties_in_Florida', 'https://en.wikipedia.org/wiki/List_of_counties_in_Georgia', 'https://en.wikipedia.org/wiki/List_of_counties_in_Hawaii', 'https://en.wikipedia.org/wiki/List_of_counties_in_Idaho',
        'https://en.wikipedia.org/wiki/List_of_counties_in_Illinois', 'https://en.wikipedia.org/wiki/List_of_counties_in_Indiana', 'https://en.wikipedia.org/wiki/List_of_counties_in_Iowa', 'https://en.wikipedia.org/wiki/List_of_counties_in_Kansas']
#KN = ['https://en.wikipedia.org/wiki/List_of_counties_in_Kentucky', 'https://en.wikipedia.org/wiki/List_of_parishes_in_Louisiana', 'https://en.wikipedia.org/wiki/List_of_counties_in_Maine','https://en.wikipedia.org/wiki/List_of_counties_in_Maryland',
      #'https://en.wikipedia.org/wiki/List_of_counties_in_Massachusetts']
df_list = []
for url in AI:
    counties = pd.read_html(url, index_col=None, header=None, match='Est.')
    df = pd.DataFrame(counties[0])
    rdf = df.rename(columns={'Borough':'County', 'Est.[2]': 'Est', 'Est.[3]': 'Est', 'Est.[4]': 'Est', 'Est.[5]': 'Est', 'Est.[6]': 'Est', 'Est.[7]': 'Est',
                             'Est.[8]': 'Est', 'Est.[9]': 'Est', 'Est.[10]': 'Est', 'Est.[12]': 'Est', 'Est.[6][12]': 'Est', 'Est.[3][8]': 'Est', 'Est.[4][11]': 'Est'})
    sdf = rdf[['County', 'Est']]
    df_list.append(sdf)

c = pd.concat(df_list, sort=False)
c.head()
print(c.head())
c.to_csv('counties.csv', encoding='utf-8', index=False)

