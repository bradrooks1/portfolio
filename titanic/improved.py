import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the data
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# Feature Engineering

# Fill missing values
train_data['Age'].fillna(train_data['Age'].median(), inplace=True)
train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)

# Create new feature 'FamilySize' as a combination of 'SibSp' and 'Parch'
train_data['FamilySize'] = train_data['SibSp'] + train_data['Parch'] + 1

# Create new feature 'IsAlone'
train_data['IsAlone'] = 1 # initialize to yes/1 is alone
train_data['IsAlone'].loc[train_data['FamilySize'] > 1] = 0 # now update to no/0 if family size is greater than 1

# Categorize Age into bins
train_data['AgeBin'] = pd.cut(train_data['Age'], bins=[0, 12, 20, 40, 120], labels=['Child', 'Teenager', 'Adult', 'Senior'])

# Convert categorical variables into numeric
train_data['Sex'] = train_data['Sex'].map({'female': 1, 'male': 0})
train_data['AgeBin'] = train_data['AgeBin'].map({'Child': 0, 'Teenager': 1, 'Adult': 2, 'Senior': 3})

# Selecting features for the model
features = ["Pclass", "Sex", "AgeBin", "FamilySize", "IsAlone", "Fare"]
X = train_data[features]
y = train_data["Survived"]

# Model Selection
model = RandomForestClassifier(n_estimators=10000, max_depth=50, random_state=1)

# Train the Model
model.fit(X, y)

# Evaluate the model using a part of the training set
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=1)
model.fit(X_train, y_train)
predictions = model.predict(X_val)

# Model Accuracy
print(f"Model Accuracy: {accuracy_score(y_val, predictions)}")
