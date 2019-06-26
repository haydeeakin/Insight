import numpy as np
import pandas as pd
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
data = pd.read_csv('....csv')
data.head()
target=data.filter(items=['target1'])
target.columns = ['Target']
target.head()

df=data.filter(items=['Nominated','Index Director Nomination'])
Xtrain, Xtest, ytrain, ytest = train_test_split(df, target, test_size=0.30,random_state=42)
dflr=LogisticRegression(random_state=43,class_weight='balanced', solver='liblinear')
fit_lr=dflr.fit(Xtrain, ytrain.values.ravel())
predicted_lr=fit_lr.predict(Xtest)
acc_log=accuracy_score(predicted_lr, ytest)
acc_log

correctpredic=df['']
dflr.coef_

corrcd = countdata.corr()
corrcd

%config InlineBackend.figure_format='svg'
sns.lmplot(x='Index Director Nomination', y='target1', data=data, logistic=True, y_jitter=.03,hue='target1', )
plt.savefig('target.png',dpi=300,bbox_inches="tight")

