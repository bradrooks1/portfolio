# Importing necessary libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the data
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# Data Preprocessing

# Fill missing values
train_data['Age'].fillna(train_data['Age'].median(), inplace=True)
train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)
test_data['Age'].fillna(test_data['Age'].median(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].median(), inplace=True)

# Convert categorical variables into numeric
train_data['Sex'] = train_data['Sex'].map({'female': 1, 'male': 0})
test_data['Sex'] = test_data['Sex'].map({'female': 1, 'male': 0})

# Feature engineering
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]
X = train_data[features]
y = train_data["Survived"]

# Model Selection
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=1)

# Train the Model
model.fit(X, y)

# Make Predictions and Evaluate (here, using a part of the training set for evaluation)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=1)
model.fit(X_train, y_train)
predictions = model.predict(X_val)

# Evaluate the model
print(f"Model Accuracy: {accuracy_score(y_val, predictions)}")

# Prepare the test data and make predictions
X_test = test_data[features]
test_predictions = model.predict(X_test)

# Create submission file for Kaggle
output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': test_predictions})
output.to_csv('submission.csv', index=False)
print("Your submission was successfully saved!")
