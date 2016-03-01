# -*- coding: utf-8 -*-
# The Consumer Complaint csv file comes from the data.gov website listed here:
# https://catalog.data.gov/dataset/consumer-complaint-database

import pandas as pd

# Reads in the dataset.
complaints=pd.read_csv('../Consumer_Complaints.csv',index_col='Date received',parse_dates=['Date received'])

# Turns string values(Company and Product) into numberical values.
company_complaints=complaints['Company'].value_counts()
product_complaints=complaints['Product'].value_counts()

# Show top 10 companies and products with complaints.
company_complaints[:10]
product_complaints[:10]

# Shows values with mortgage complaints.
mortgage=complaints['Product'] == "Mortgage"
mortgage_complaints=complaints[mortgage]

# Shows top 10 companies with mortgage complaints.
mortgage_complaints['Company'].value_counts()[:10]

# Shows bar graph of types of mortgages with complaints in descending order.
mortgage_complaints['Sub-product'].value_counts().plot(kind='bar')