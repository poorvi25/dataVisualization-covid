import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# df_india =pd.read_excel('./datasets/finalcomplete.xlsx')
df =pd.read_excel('./datasets/death_newrecord.xlsx')
# print('#############################################################################################################')

# print('Total cases in India:',df_india['New cases'].sum())
# print('Total deaths in India:',df_india['New deaths'].sum())
# print('Total recoveries in India:', df_india['New recovered'].sum())
# print('Total deaths in Indian States:',df_india.groupby(by=['Name of State / UT']).agg({'New deaths':'sum'}))

# print('#############################################################################################################')
#Dates v/s deaths


# print('Total deaths in India till 6 aug 2020:',df['Deaths'].sum())
# p = sns.set_palette('Reds_d')
# sns.lineplot(x='dates', y='Deaths',marker='d', data=df, palette=p)
# plt.show()

# print('#############################################################################################################')

#Dates v/s recovered
#
#
# print('Total recovered in India till 6 aug 2020:',df['Recovered'].sum())
# p = sns.set_palette('Greens_d')
# sns.lineplot(x='dates', y='Recovered',marker='d', data=df, palette=p)
# plt.show()

# print('#############################################################################################################')
#Dates v/s cases


# print('Total new cases in India till 6 aug 2020:',df['New case'].sum())
# p = sns.set_palette('Blues_d')
# sns.lineplot(x='dates', y='New case',marker='d', data=df, palette=p)
# plt.show()

# print('#############################################################################################################')
# In one subplot dates v/s cases, recovered and deaths

# f,axes=plt.subplots(3,figsize=(7, 14))
# sns.lineplot(x="dates",y="New case",data=df,ax=axes[0],marker='o', color='#0000FF')
# sns.lineplot(x="dates",y="Recovered",data=df,ax=axes[1],marker='o', color='#60DE20')
# sns.lineplot(x="dates",y="Deaths",data=df,ax=axes[2],marker='o',color='#F55016')
#
# plt.setp(axes)
# plt.tight_layout()
#
# plt.show()
# print('#############################################################################################################')
# recovery rate
# p = sns.set_palette("Greens_d")
# df = df[:-1]
#
# df['recovery rate'] = df['Recovered']/df['New case']*100
# print("Recovery rate in particular date till august 2020",df)
# sns.lineplot(x='dates', y='recovery rate', data=df,palette=p, marker='D', markeredgecolor='black').set_title('Recovery Rate in India')
# plt.show()

#death rate

# q = sns.set_palette("Reds_d")
# df['death rate'] = df['Deaths']/df['New case']*100
# print("Date rate in particular date till august 2020",df)
# sns.lineplot(x='dates', y='death rate', data=df,palette=q, marker='D', markeredgecolor='black').set_title('Death Rate in India')
# plt.show()

# print('#############################################################################################################')

# Pieplot comparisons
# piedf = pd.DataFrame({"Overall":["Death", "Recovered", "Overall_Case","Active_Case"],
#                       "Value":[40593,1328164,1964273,676782]},
#                     )
# color=["#B80F0A","#008000","#87CEEB","#ED9121"]
# Explode=(0,0,0,0.1)
# overall=piedf["Overall"]
# value = piedf["Value"]
# plt.pie(value,labels=overall,explode=Explode,colors=color,shadow=True,autopct='%1.1f%%',startangle=60)
# plt.title("Death v/s Recovered v/s Overall v/s Active cases in Percentage")
# plt.show()

# print('#############################################################################################################')
#Symptoms for coronavirus
s = pd.read_excel('./datasets/Symptoms.xlsx')
sns.set_theme(style="whitegrid")
print("Symptoms of corona and its percentage are")
print(s)
f,axes=plt.subplots(figsize=(15,8))
ax = sns.barplot(x='Percentage',y='Symptom',data=s,palette="mako",ax=axes)
ax.set(xlabel='Percentages', ylabel='Symptoms', title='Symptoms-percentages of covid')
plt.show()

# print('#############################################################################################################')
# Comparisons
# sns.set_theme(style='white')
# sns.lineplot(x="New case",y="Deaths",marker='D',markeredgecolor='black',data=df,color='Red').set_title('Newly infected v/s newly deaths')
# plt.show()
# sns.lineplot(x="New case",y="Recovered",marker='D',markeredgecolor='black',data=df,color='Green').set_title('Newly infected v/s newly recovered')
# plt.show()
# sns.lineplot(x="Deaths",y="Recovered",marker='D',markeredgecolor='black',data=df,color='Blue').set_title('Newly deaths v/s newly recovered')
# plt.show()
# print('#############################################################################################################')
# Age group percent cases
# d = pd.read_excel('./datasets/IndiaAgeGroupDetails.xlsx')
# sns.barplot(x='AgeGroup',y='TotalCases',data=d,palette='rocket').set_title('Cases in different age group in India')
# plt.show()
#
