from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load the pre-cleaned dataset

BASE_DIR = Path(__file__).resolve().parent.parent
df = pd.read_csv(BASE_DIR / 'data' / 'processed' / 'aha_cleaned.csv')
print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.")


#----------FINANCIAl STATISTICS----------------
expenses = df[['Total Expense','Payroll Expense', 'Personnel']]

print(expenses.head())

total_expense = expenses['Total Expense'].sum()

total_payroll_expense = expenses['Payroll Expense'].sum()

operational_expense = total_expense - total_payroll_expense

df['Operational Expense'] = df['Total Expense'] - df['Payroll Expense']

print(f"Total Expense: Ghc{total_expense}.00")
print(f"Total Payroll Expense: Ghc{total_payroll_expense}.00")
print(f"Operational Expense: Ghc{operational_expense}.00")

#-------FINANCIAL SUMMARY BY STATE----------------

state_expenses = df.groupby('State')[['Total Expense','Payroll Expense']].sum().reset_index()
state_expenses['Operational Expense'] = state_expenses['Total Expense'] - state_expenses['Payroll Expense']
print(state_expenses.head())

state_summary = df.groupby('State').agg(
    Admissions=('Admissions', 'sum'),
    Total_Expense=('Total Expense', 'sum'),
    Payroll_Expense=('Payroll Expense', 'sum'),
    Operational_Expense=('Operational Expense', 'sum'),
    Personnel = ('Personnel', 'sum')
).reset_index()

state_summary['Operational_Expense'] = state_summary['Total_Expense'] - state_summary['Payroll_Expense']

print(state_summary.head(20))


#________________________DESCRIPTIVE STATISTICS________________________

#----------Pie Chart for total expenses----------------

label = ['Payroll Expense', 'Operational Expense']
values = [total_payroll_expense, operational_expense]

plt.figure(figsize=(5, 5))
plt.pie(values, labels=label, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.title('Expense Distribution')
plt.show()

#----------Bar Chart for State Expenses----------------

plt.figure(figsize=(10, 6))

plt.bar(
    state_expenses['State'],
    state_expenses['Operational Expense'],
    bottom=state_expenses['Payroll Expense'],
    color= 'green',
    label= 'Operational Expense'
)

plt.bar(
    state_expenses['State'], 
    state_expenses['Payroll Expense'],
    color= 'red',  
    label='Payroll Expense',
    )

plt.title('Total Expenses Across States')
plt.xlabel('State')
plt.xticks(rotation=45)

plt.yticks(range(0, int(state_expenses['Total Expense'].max()) + 100000, 100000))
plt.legend()

plt.tight_layout()
plt.show()

df['Operational Expense'] = df['Total Expense'] - df['Payroll Expense']

#-------------Scatter Plot for Admissions vs Operational Expenses----------------

plt.figure(figsize=(10, 6))
plt.scatter(df['Admissions'], df['Operational Expense'])
plt.title('Admissions vs Operational Expenses')
plt.xlabel('Admissions')
plt.ylabel('Operational Expenses')

plt.tight_layout()
plt.show() 

'''
plot shows a strong positive correlation between admissions and operational expenses, 
indicating that as the number of admissions increases, the operational expenses also tend to increase. 
This suggests that hospitals with higher patient volumes may incur higher operational costs.   
'''
