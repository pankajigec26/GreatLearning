import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline

df=pd.read_csv('Telco.csv')
#Calculate Histogram on time spent on day calls by customer 
#CHanging the total day calls as numeric type
#df=pd.to_numeric(['total day calls'], errors='coerce')

#Plotting the histogram in SNS
sns.distplot(df['total day calls'],kde=True, rug=False,bins=100);
plt.show()
#5cg8150m3h


#Q:How do we categorize the churner and non churner for the time spent on day calls (by minutes)

df['churn'].value_counts().plot.bar()
#sns.barplot(df['churn'].value_counts(),orient='h')
#df['churn'].value_counts().plot.bar()
df.plot.bar()
plt.show()

#Find the number of customers who did opt for voice mail plan
df['voice mail plan'].value_counts().plot.bar()
plt.show

#Create a boxplot for a categorical variable(international plan) and continuous variable(area code).
#Box plot for categorical variable(international plan) and continious variable(area code)
sns.boxplot(df['international plan'], df['area code'], hue=df['international plan'])
plt.show()

#Create a crosstab for the area code to find the churner or non-churner.
df=pd.crosstab(df['area code'],df['churn'])

df.plot.bar(stacked=True)
plt.legend(title='churn')
plt.show()


