import pandas as pd

def load_data_into_df(filepath):
  df = pd.read_csv(filepath)
  return df
  
def rename_columns(df):
  df.rename(columns = {'S Code': 's_code','Level of Service (single App)': 'service_level', 'Gender':'gender','Race / Ethnicity':'race_or_ethnicity', 'Number of Children':'num_of_children', 'Education Level When Released':'education_level_when_released' }, inplace = True)
  return df

def drop_nonpped_users(df):
  
  pass

def create_recidivism_column(df):
  y = df['total_recidivism_events'] > 0
  return y

