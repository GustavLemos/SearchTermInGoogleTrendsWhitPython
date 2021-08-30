from pandas import plotting
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

plt.style.use('bmh')
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#input on term
term = input('\nDigite o term desejado:')

# connect to google
pytrends = TrendReq(hl='pt-BR', tz=360)
# keywords to search for
pytrends.build_payload(kw_list=[term])

# dataframe
time_df = pytrends.interest_over_time()

# creating graph
fig, ax = plt.subplots(figsize=(12, 6))
time_df[term].plot(color='purple')
# adding title and labels
plt.title('Total de pesquisas do Google  por "'+ term +'"', fontweight='bold')
plt.xlabel('Ano')
plt.ylabel('Total Pesquisa')
plt.show()
