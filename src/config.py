DATA_PATH = "data/WA_Fn-UseC_-Telco-Customer-Churn.csv" # Data path
TARGET = "Churn" # We would like to predict this variable (Yes/No)
ID_COLS = ["customerID"] # We don't use it for prediction
NUM_COLS = ["tenure", "MonthlyCharges", "TotalCharges"]
CAT_COLS = [
    "gender","SeniorCitizen","Partner","Dependents","PhoneService","MultipleLines",
    "InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport",
    "StreamingTV","StreamingMovies","Contract","PaperlessBilling","PaymentMethod"
] # Columns that we use for prediction
TEST_SIZE = 0.2 # Train-Test split ratio
RANDOM_STATE = 42 # Random seed
MODEL_PATH = "models/model.pkl" # Trained model path