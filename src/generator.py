"""Data Generator"""

import pandas as pd
import numpy as np

def generate_customers(n=50000):
    """Generate mall customer data"""
    print(f"Generating {n:,} customers...")
    np.random.seed(42)
    
    segments = [
        {'income': (15, 40), 'spending': (1, 40), 'age': (18, 35)},
        {'income': (15, 40), 'spending': (60, 99), 'age': (18, 30)},
        {'income': (70, 137), 'spending': (1, 40), 'age': (35, 70)},
        {'income': (70, 137), 'spending': (60, 99), 'age': (25, 50)}
    ]
    
    data = []
    per_seg = n // len(segments)
    
    for seg_idx, seg in enumerate(segments):
        for i in range(per_seg):
            data.append({
                'CustomerID': seg_idx * per_seg + i + 1,
                'Gender': np.random.choice(['Male', 'Female']),
                'Age': np.random.randint(*seg['age']),
                'Annual_Income_k': round(np.random.uniform(*seg['income']), 2),
                'Spending_Score': round(np.random.uniform(*seg['spending']), 2)
            })
    
    df = pd.DataFrame(data).sample(frac=1, random_state=42).reset_index(drop=True)
    print(f"Generated {len(df):,} customers")
    return df