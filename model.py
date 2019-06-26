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
0.8276611151339609
correctpredic=df['']
dflr.coef_
array([[ 1.89187706, -5.15593322]])

corrcd = countdata.corr()
corrcd
  lognomi	logwon	logfil	residwon	residnom
lognomi	1.000000	0.157070	7.520392e-01	-3.887637e-01	6.591184e-01
logwon	0.157070	1.000000	6.160576e-01	7.877011e-01	-4.646048e-01
logfil	0.752039	0.616058	1.000000e+00	-3.096118e-15	-5.978103e-15
residwon	-0.388764	0.787701	-3.096118e-15	1.000000e+00	-5.898237e-01
residnom	0.659118	-0.464605	-5.978103e-15	-5.898237e-01	1.000000e+00

