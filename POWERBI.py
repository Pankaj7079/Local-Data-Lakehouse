import pandas as pd

print("="*60)
print("EXPORTING DATA LAKE FOR POWER BI")
print("="*60)

# Read from Data Lake output
df = pd.read_csv('data/customers_clustered.csv')
print(f"\n Loaded {len(df):,} customers from Spark Data Lake")

# Add analytics columns
df['Income_Category'] = pd.cut(df['Annual_Income_k'], 
                                bins=[0, 40, 80, 150],
                                labels=['Low', 'Medium', 'High'])

df['Spending_Category'] = pd.cut(df['Spending_Score'],
                                   bins=[0, 33, 66, 100],
                                   labels=['Low', 'Medium', 'High'])

df['Age_Group'] = pd.cut(df['Age'],
                          bins=[0, 25, 40, 60, 100],
                          labels=['Young', 'Adult', 'Middle-aged', 'Senior'])

df['Customer_Value'] = (df['Annual_Income_k'] * 0.5 + 
                        df['Spending_Score'] * 0.5)

print(" Added analytics columns")

# Export for Power BI
df.to_csv('data/powerbi_data.csv', index=False)
print("\n Saved: data/powerbi_data.csv")

print("\n" + "="*60)
print(" READY FOR POWER BI!")
print("="*60)
print("\nNext Steps:")
print("1. Open Power BI Desktop")
print("2. Get Data → Text/CSV")
print("3. Select: data/powerbi_data.csv")
print("4. Click Load")
print("5. Create dashboard!")