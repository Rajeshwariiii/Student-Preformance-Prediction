import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

#Loading dataset (college real time data) 
df = pd.read_csv('pccoe_CSE_DivA&B_google_form_dataset.csv')

#Derived feature
df['motivation_score'] = df['Attendance'] * df['Hours Studied']

#Study Pattern
def classify_pattern(row):
    if row['Hours Studied'] > 5:
        return 'Crammer'
    elif row['Hours Studied'] >= 2:
        return 'Consistent'
    else:
        return 'Irregular'

df['Study Pattern'] = df.apply(classify_pattern, axis=1)

# One-hot encode Study Pattern
df = pd.get_dummies(df, columns=['Study Pattern'])

# Ensure all expected dummy columns are present
for col in ['Study Pattern_Consistent', 'Study Pattern_Crammer']:
    if col not in df.columns:
        df[col] = 0  # Add missing columns as zeros

# Define features and target
X = df[['Hours Studied', 'Previous Scores', 'Attendance', 'motivation_score',
        'Study Pattern_Consistent', 'Study Pattern_Crammer']]
y = df['Performance Index']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))

print("✅ Model trained and saved successfully!")
