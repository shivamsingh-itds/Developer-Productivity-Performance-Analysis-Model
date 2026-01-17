# Import data Manipulation library 
import pandas as pd 
import numpy as np 

# Import Scikit learn library
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler


# Data Ingestion
filepath = 'https://raw.githubusercontent.com/shivamsingh-itds/Developer-Productivity-Performance-Analysis-Model/refs/heads/main/Data/raw/Ai_Developer.csv'
def data_ingestion():
    return pd.read_csv(filepath)

# Data Preprocessing
def data_preprocessing(df):

    # Spliting data in X and y 
    X = df.drop(columns='Task_Success_Rate', axis= 1)
    y = df['Task_Success_Rate']
    
    # train test split
    X_train ,X_test , y_train ,y_test = train_test_split(X ,y , test_size= 0.3 , random_state= 42)

    # Scaling
    
    sc = MinMaxScaler()
    X_train = sc.fit_transform(X_train)
    X_test =sc.transform(X_test)

    return X_train ,X_test , y_train ,y_test

# Model Building
def model_building(X_train ,X_test , y_train ,y_test):
    model = RandomForestRegressor(n_estimators=200)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    return r2, rmse




# Function calling

df = data_ingestion()
X_train ,X_test , y_train ,y_test = data_preprocessing(df)
r2, rmse = model_building(X_train, X_test, y_train, y_test)


print("Random Forest Model Performance")
print("-------------------------------")
print(f"R2 Score : {r2:.4f}")
print(f"RMSE     : {rmse:.4f}")
