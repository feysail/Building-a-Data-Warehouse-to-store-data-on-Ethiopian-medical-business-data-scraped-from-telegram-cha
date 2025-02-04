import pandas as pd
import os
import re

def add_headers_to_csv(csv_file_path, column_names):
    """
    Adds column headers to an existing CSV file.

    Parameters:
    - csv_file_path: str - The path to the existing CSV file.
    - column_names: list - A list of column names to add.

    Returns:
    - None
    """
    if not os.path.isfile(csv_file_path):
        raise FileNotFoundError(f"The file {csv_file_path} does not exist.")
    data = pd.read_csv(csv_file_path, header=None)  # Read without headers

    data.columns = column_names
    data.to_csv(csv_file_path, index=False)

    print("Column names added successfully.")

    
def remove_emoji(df):
    df['Message'] = df['Message'].str.replace(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F900-\U0001F9FF\U00002700-\U000027BF\U00002600-\U000026FF]+', '', regex=True)


def create_emoji_column(df):
    df['Emoji'] = df['Message'].str.extract(r'([\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F900-\U0001F9FF\U00002700-\U000027BF\U00002600-\U000026FF]+)', expand=False)
    



def remove_links(df):
    url_pattern = r'(http[s]?://\S+)'
    df['Message']=df['Message'].str.replace(url_pattern,'',regex=True)
    
def add_link(df):
    url_pattern = r'http[s]?://\S+'
    df['Link']=df['Message'].str.extract(f'({url_pattern})',expand=False)

