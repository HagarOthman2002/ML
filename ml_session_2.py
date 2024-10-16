# -*- coding: utf-8 -*-
"""ML session 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11_3_SR4scNaq11TVowJuh_xi-Fme1I9E

#import libraries
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

"""#Read Dataset"""

startups = pd.read_csv("/content/50_Startups.csv")
startups.head(10)

"""#EDA

check info
"""

startups.info()

"""check null values"""

startups.isnull().sum()

"""convert state to categorical"""

startups['State'] = startups['State'].astype('category')

startups['State'].unique()

"""one hot_encoding to state column"""

# One-hot encode the 'State' column
startups = pd.get_dummies(startups, columns=['State'], drop_first=True)
startups.head(5)

"""rearrange columns"""

# Rearrange the columns in the desired order
startups = startups[['R&D Spend', 'Administration', 'Marketing Spend', 'State_Florida', 'State_New York', 'Profit']]

# Display the DataFrame with the new column order
startups.head(5)

"""check the correlation between the features"""

corr = startups.corr()
# the diagonal is the relationship of the column with itself

"""heat map of the correlation"""

sns.heatmap(corr , annot=True)

"""- there is strong relationship between R&D spend and the profit : 2 columns are numerical
        -visulaiz the relationship between them using (scatter plot , pairplot)
"""

sns.scatterplot(x= ("R&D Spend") , y=("Profit") , data = startups , color = "red")

startups.describe().T

"""check for duplicates"""

startups.duplicated().sum()

"""check outliers"""

num_cols = startups.select_dtypes("number").columns
num_cols

plt.figure(figsize=(9, 4))
for i, col in enumerate(num_cols):
    plt.subplot(3, 3, i+1)
    plt.title(col)
    sns.boxplot(startups[col], orient="h")
plt.subplots_adjust(hspace=2, wspace=.8)
plt.show()

"""split the dataset"""

x = startups.drop("Profit" , axis = 1)
y = startups['Profit']

x.head()

y.head()

X_train , X_test , y_train , y_test= train_test_split(x , y ,test_size=.3 , random_state=42)

"""#build Model

multi linear regression
"""

from sklearn.linear_model import LinearRegression

lm = LinearRegression()

model = lm.fit(X_train , y_train)

y_predict = model.predict(X_test) #gives y_predict
y_predict

"""#Evaluation"""

from sklearn.metrics import mean_absolute_error , r2_score ,mean_squared_error

MAE = mean_absolute_error(y_test , y_predict)

MAE

MSE = mean_squared_error(y_test , y_predict)
MSE

MRSE = np.sqrt(MSE)
MRSE

model.score(X_train , y_train)

"""#polynomial regression"""

df = pd.read_csv("/content/Position_Salaries.csv")
df

df.info()

df.isna().sum()

df.describe().T

#visulize
#pair plot to visulize the relationship
sns.pairplot(df)
plt.xlabel("level")
plt.ylabel("salary")
plt.title("salary prediction")
plt.show()

"""#split data"""

x  = df.iloc[: , 1:2].values  # values make the series to numpy so we have to apply values on x & y or not apply it at all
y = df.iloc[: , 2].values

X_train , X_test , y_train , y_test =train_test_split( x , y  , test_size = .3 , random_state = 42)

"""#build model"""

from sklearn.linear_model import LinearRegression

linear_model = LinearRegression()
linear_model.fit(X_train , y_train )

y_predict = linear_model.predict(X_test)
y_predict

plt.scatter(X_train , y_train , color = "red")
plt.plot(X_test , y_predict)

"""#Evaluation"""

from sklearn.metrics import mean_absolute_error , mean_squared_error , r2_score

MSE = mean_squared_error(y_test , y_predict)
MSE

RMSE = np.sqrt(MSE)
RMSE

MAE = mean_absolute_error(y_test , y_predict)
MAE

RSQ = r2_score(y_test , y_predict)
RSQ

"""#polynomial regression"""

#first we put the data on polynomial form

from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(x)


poly_model = LinearRegression()
model = poly_model.fit(x_poly , y )


X_poly_predict = poly_model.predict(x_poly)

plt.scatter(x , y , color = 'red')
plt.plot(x , X_poly_predict)

"""#comparison between multi linear regression and polynomial regression"""

df

df[df["Level"]==6]

linear_model.predict([[6]])

poly_model.predict(poly_reg.fit_transform([[6]]))
