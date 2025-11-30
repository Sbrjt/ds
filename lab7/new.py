import pandas as pd
import statsmodels.api as sm

# Example dataset
data = {
    "hours": [2, 3, 5, 7, 1],
    "iq": [100, 110, 120, 130, 90],
    "attendance": [0.8, 0.9, 0.95, 1.0, 0.7],
    "score": [50, 60, 80, 90, 40],
}
df = pd.DataFrame(data)

# 1. Define predictors and response
X = df[["hours", "iq", "attendance"]]
y = df["score"]

# 2. Add constant for intercept
X = sm.add_constant(X)

# 3. Fit the model
model = sm.OLS(y, X).fit()

# 4. View summary
print(model.summary())

# ---- Predict for a new student ----
new_student = [5, 115, 0.9]  # order: hours, iq, attendance

# 5. Create DataFrame for new student with same column names (without 'const')
X_new = pd.DataFrame([new_student], columns=["hours", "iq", "attendance"])

# 6. Add constant (intercept)
X_new = sm.add_constant(X_new, has_constant='add')  # ensures 'const' is added

# 7. Make prediction
predicted_score = model.predict(X_new)
print("Predicted score:", predicted_score.iloc[0])
