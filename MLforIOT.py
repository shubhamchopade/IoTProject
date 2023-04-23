# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16JtKtOoAwAATu4vXgfwtZnsEZy8BOJ82
"""

# Generic inputs for most ML tasks
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
import time

pd.options.display.float_format = '{:,.2f}'.format

# setup interactive notebook mode
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

from IPython.display import display, HTML

# Generic inputs for most ML tasks
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn import tree
import graphviz
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import xgboost as xgb

pd.options.display.float_format = '{:,.2f}'.format

# setup interactive notebook mode
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

from IPython.display import display, HTML

# fetch data 

crop_data = pd.read_csv('Crop_recommendation.csv')

crop_data.head()

unique_count = crop_data['label'].unique()

unique_count

len(crop_data)

crop_data.isna().sum()

le = preprocessing.LabelEncoder()

crop_data['Column_name_encoded'] = le.fit_transform(crop_data['label'])

# Print the unique encoded values
print(list(le.classes_))

# Print the transformed column values
print(crop_data['Column_name_encoded'])

# Replace the original column with the encoded values
crop_data['label'] = crop_data['Column_name_encoded']

# Drop the encoded column
crop_data = crop_data.drop(columns=['Column_name_encoded'])

crop_data.head(200)

X_train, X_test, y_train, y_test = train_test_split(crop_data.drop('label' ,axis=1),crop_data['label'], stratify = crop_data['label'], test_size=0.20, random_state = 50)

X_train.head()
X_test.head()
y_train.head()
y_test.head()

X_train.columns
gb = GradientBoostingClassifier(random_state=50, min_samples_split = 12, min_samples_leaf = 6, max_depth = 4, n_estimators = 100)

gb = gb.fit(X_train, y_train) 
gb.score(X_train, y_train) 

# gb.feature_importances_
feat_imp = pd.Series(gb.feature_importances_, X_train.columns.values).sort_values(ascending=False)

feat_imp_table = pd.DataFrame(feat_imp)
feat_imp_table = feat_imp_table.reset_index()
feat_imp_table.columns = ['Features', 'Values']
feat_imp.plot(kind='bar', title='Feature Importances')
# plt.ylabel('Feature Importance Score')
# plt.figure(figsize=[40,20], dpi = 50)
feat_imp.head(12)

test_output = pd.DataFrame(gb.predict(X_test), index = X_test.index, columns = ['pred_Y'])

test_output.head()
test_output = test_output.merge(y_test, left_index = True, right_index = True)
test_output.head()
print('Fraction of correct classification ')
gb.score(X_test, y_test)

y_test.nunique()



X_train.columns
rf = RandomForestClassifier(random_state=50, min_samples_leaf = 6, max_features = "sqrt", n_estimators = 100)

rf = rf.fit(X_train, y_train) 
rf.score(X_train, y_train) 

# rf.feature_importances_
feat_imp = pd.Series(rf.feature_importances_, X_train.columns.values).sort_values(ascending=False)

feat_imp_table = pd.DataFrame(feat_imp)
feat_imp_table = feat_imp_table.reset_index()
feat_imp_table.columns = ['Features', 'Values']
feat_imp.plot(kind='bar', title='Feature Importances')
# plt.ylabel('Feature Importance Score')
# plt.figure(figsize=[40,20], dpi = 50)
feat_imp.head(12)

test_output = pd.DataFrame(rf.predict(X_test), index = X_test.index, columns = ['pred_Y'])

test_output.head()
test_output = test_output.merge(y_test, left_index = True, right_index = True)
test_output.head()
print('Fraction of correct classification ')
rf.score(X_test, y_test)

X_test

sum(test_output['label'] == 0)
sum(test_output['label'] == 1)

"""# Testing labels for Station 1



"""

data =pd.read_csv("station1.csv",sep=';')

df_grouped = data.groupby("Timestamp").first()

df_grouped.head()

df_test_one = df_grouped.drop('Entity Name', axis=1)

df_test_one.head()

#checking for null values in staion csv 2 
df_test_one.isna().sum()

df_test_one = df_test_one.dropna(how='any')

df_test_one = df_test_one.rename(columns={'k': 'K', 'n': 'N', 'p': 'P'})

df_test_one.head()

df_test_one= df_test_one.reset_index(drop=True)

df_test_one = df_test_one.reindex(columns=X_train.columns)

test_output.head()

test_output = pd.DataFrame(rf.predict(df_test_one), index = df_test_one.index, columns = ['pred_Y'])

test_output.head()

test_output.value_counts()

predicted_crop_station_1 = list(le.inverse_transform([9]))
predicted_crop_station_1



"""# Testing labels for Station 2 """

data =pd.read_csv("station2.csv",sep=';')

data.isna().sum()

df_grouped = data.groupby("Timestamp").first()

df_grouped.head()

df_test_two = df_grouped.drop('Entity Name', axis=1)

df_test_two.head()

#checking for null values in staion csv 2 
df_test_two.isna().sum()

df_test_two = df_test_two.dropna(how='any')

df_test_two = df_test_two.rename(columns={'k': 'K', 'n': 'N', 'p': 'P'})

df_test_two.head()

df_test_two = df_test_two.reset_index(drop=True)

df_test_two = df_test_two.reindex(columns=X_train.columns)

test_output.head()

test_output = pd.DataFrame(rf.predict(df_test_two), index = df_test_two.index, columns = ['pred_Y'])
# RecommendationRecommendation
test_output.head()

test_output.value_counts()

predicted_crop_station_2 = list(le.inverse_transform([18,12]))
predicted_crop_station_2

"""# Testing labels for Station 3"""

data =pd.read_csv("station3.csv",sep=';')

data.isna().sum()

df_grouped = data.groupby("Timestamp").first()

df_grouped.head()

df_test_three = df_grouped.drop('Entity Name', axis=1)

df_test_three.head()

#checking for null values in staion csv 2 
df_test_three.isna().sum()

df_test_three = df_test_three.dropna(how='any')

df_test_three = df_test_three.rename(columns={'k': 'K', 'n': 'N', 'p': 'P'})

df_test_three.head()

df_test_three = df_test_three.reset_index(drop=True)

df_test_three = df_test_three.reindex(columns=X_train.columns)

test_output.head()

test_output = pd.DataFrame(rf.predict(df_test_three), index = df_test_three.index, columns = ['pred_Y'])
# RecommendationRecommendation
test_output.head()

test_output.value_counts()

predicted_crop_station_3 = list(le.inverse_transform([1]))
predicted_crop_station_3

import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def get_data():
    data = {"crop1": [predicted_crop_station_1], "crop2": [predicted_crop_station_2],"crop3":[predicted_crop_station_3] }
    json_data = json.dumps(data)
    print(json_data)
    return jsonify(json.loads(json_data))

# accept the crop name as a parameter
@app.route('/predict/<crop>')
def get_crop(crop):
    time.sleep(2)
    if crop == 'farmer1':
        # sleep for 5 seconds
        data = {"data": [predicted_crop_station_1]}
    elif crop == 'farmer2':
        data = {"data": [predicted_crop_station_2]}
    elif crop == 'farmer3':
        data = {"data": [predicted_crop_station_3]}
    json_data = json.dumps(data)
    print(json_data)
    response = jsonify(json.loads(json_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# open the port 5000

if __name__ == '__main__':
    app.run(port=3005, debug=True)