# Copyright 2018-2024 Business Cyber Guardian a Reliable Energy Analytics LLC Compant
# Provided under MIT Licensing Terms
# This code snippet shows how to read a CISA Software Assurance Guide spreadsheet and display the Governance tab Conrols with producer answers 
import pandas as pd
df = pd.read_excel("https://www.cisa.gov/sites/default/files/2024-08/PDM24064%20Software%20Acquisition%20Guide%20for%20Government%20Enterprise%20Consumers%20Final-%2020240710_v19.xlsx", sheet_name="Governance", usecols="A,B, C", skiprows=11)
# df = pd.read_excel("SAG-SPREADSHEET-SAG-PM_V2_1_1.xls", sheet_name="Governance", usecols="A,B, C", skiprows=11) 
for row in df.itertuples():
    if isinstance(row[1], str):
        print(row[1], " Response: ", row[3], "\n", "\t", row[2], "\n")

