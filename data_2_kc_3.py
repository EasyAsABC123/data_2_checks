import enum
import os
import pandas as pd

# I'm using an enum to store column names.
class ColumnName(enum.Enum):
    COUNTRY = 'Country'
    DEVELOPER_INCOME = 'Average Developer Income in USD ($)'
    OVERALL_INCOME = 'Income per Capita in USD ($)'

# Import data from income per capita report from World Bank:
# https://data.worldbank.org/indicator/NY.ADJ.NNTY.PC.CD
wb_df = pd.read_csv(os.path.join('data', 'API_NY.ADJ.NNTY.PC.CD_DS2_en_csv_v2_4261468.csv'), usecols=('Country Name', '2021'))

# Rename columns:
wb_df.rename(columns={
    'Country Name': ColumnName.COUNTRY.value,
    '2021': ColumnName.OVERALL_INCOME.value
}, inplace=True)

print(wb_df.sample(30))

# Drop rows with null values:
wb_df.dropna(inplace=True)

# Import data from 2021 Stack Overflow developer survey:
# https://insights.stackoverflow.com/survey
so_df = pd.read_csv(os.path.join('data', 'survey_results_public.csv'), usecols=('Country', 'ConvertedCompYearly'))

# Rename columns:
so_df.rename(columns={
    'ConvertedCompYearly': ColumnName.DEVELOPER_INCOME.value
}, inplace=True)

# Drop rows with null values:
so_df.dropna(inplace=True)

# Group by country and get average income:
so_df.groupby(ColumnName.COUNTRY.value)[ColumnName.DEVELOPER_INCOME.value].mean()

# Merge dataframes
merged_df = wb_df.merge(so_df, on=ColumnName.COUNTRY.value)

print(merged_df.sample(30))