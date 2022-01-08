
import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_science/president_polls.csv')

polls = df[['state', 'display_name', 'candidate_party','sponsor_ids', 'pollster_id']]

# sns.relplot() function is used to plot the relationship between columns

sns.regplot(data=polls, x = 'pollster_id', y='sponsor_ids')
sns.boxenplot(x = 'state', y = 'pollster_id', data = polls)
sns.set_theme()

plt.show()