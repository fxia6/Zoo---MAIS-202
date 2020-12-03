import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from joblib import dump

# read data from csv files
zoo_data = pd.read_csv('zoo.csv')
class_data = pd.read_csv('class.csv')

### data preprocessing
# remove the first column 'animal_name' and exclude the label column to obtain X
X = zoo_data.iloc[:,1:17]
# extract the label column to obtain y
y = zoo_data.iloc[:,17]

# fill up missing values, if any
# We will assume any missing values take on value 0, which is equivalent to False in boolean
for feature_name in X.columns:
    for i in range(len(X[feature_name].isnull())):
        if X[feature_name].isnull()[i] == True:
            X[feature_name][i] = 0

### building a ML model
# training/validation/test splits
X_train = X.iloc[:150]
X_test = X[150:214]
y_train = y.iloc[:150]
y_test = y.iloc[150:214]
rdf = RandomForestClassifier(oob_score=True, n_estimators = 1200,min_samples_split=2,min_samples_leaf=1,max_features='auto',max_depth = 4)
rdf.fit(X_train,y_train)
print(rdf.score(X_train,y_train))
print(rdf.score(X_test,y_test))

save_model_path = './model/results/model.pth'
dump(rdf, 'zoo_model.joblib')
