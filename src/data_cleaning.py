import pandas as pd

def load_data_into_df(filepath):
  df = pd.read_csv(filepath)
  return df
  
def rename_columns(df):
  pass

def drop_nonpped_users(df):
  
  pass

def create_recidivism_column(df):
  y = df['total_recidivism_events'] > 0
  return y

