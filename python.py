import pandas as pd
import matplotlib.pyplot as plt

with open('infant_mortality.json', 'r', encoding='ascii') as f:
    text = f.read()
import json
mortality = json.loads(text)



ARB1990 = mortality[0]['Value']
ARB1991 = mortality[1]['Value']
ARB1992 = mortality[2]['Value']
ARB1993 = mortality[3]['Value']



data=[["1990", ARB1990, 16.154032957905, 45.6],
      ["1991", ARB1991, 15.6211573687443, 42.62257683928],
      ["1992", ARB1992, 15.1357487828739, 41.6633631534576],
      ["1993", ARB1993, 14.7576168439386, 40.5433811555997]
     ]

df=pd.DataFrame(data,columns=["Years","Arab World","Central Europe and the Baltics","East Asia & Pacific"])
df.plot(x="Years", y=["Arab World","Central Europe and the Baltics", "East Asia & Pacific"], kind="bar",figsize=(9,8))
plt.ylabel('Infant Mortality Rate')
plt.show()



'''https://pkgstore.datahub.io/world-bank/sp.dyn.imrt.in/data_json/data/cdde32275190fb6e53e4a7ea2b77d4ba/data_json.json'''



with open('speeches.json', 'r', encoding='ascii') as f:
    text = f.read()
import json
speeches = json.loads(text)


list = speeches['results'][0]['body'].split()
empty = []
violence_counts = 0
law_counts = 0
justice_counts = 0
victim_counts = 0
country_counts = 0


for char in list:
    if char == 'violence' or char == 'Violence':
        violence_counts += 1

for char in list:
    if char == 'law' or char == 'Law':
        law_counts += 1

for char in list:
    if char == 'justice' or char == 'Justice':
        justice_counts += 1

for char in list:
    if char == 'victim' or char == 'Victim':
        victim_counts += 1

for char in list:
    if char == 'country' or char == 'Country':
        country_counts += 1

#plot
xs = ['violence', 'law', 'justice', 'victim', 'country']
ys = [violence_counts, law_counts, justice_counts, victim_counts, country_counts]

fig, ax = plt.subplots()
ax.plot(xs, ys)
plt.xlabel('types of words used')
plt.ylabel('number of times used')
plt.show()













    


