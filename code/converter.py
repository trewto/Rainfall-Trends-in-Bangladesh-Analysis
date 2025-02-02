import pandas as pd

# Read the Excel file
df = pd.read_excel('mk_18Nov_Citywise .xlsx', sheet_name='mk_18Nov')

stations = []

# Iterate over each pair of Zmk and Q rows
for i in range(0, len(df), 2):
    zmk_row = df.iloc[i]
    q_row = df.iloc[i + 1]
    
    # Extract station name by removing 'Zmk_' prefix
    station_name = zmk_row['index'].replace('Zmk_', '')
    
    # Prepare the row data with station name
    row_data = {'Station': station_name}
    
    # Process each month from 1 to 12
    for month in range(1, 13):
        zmk_val = zmk_row[month]
        q_val = q_row[month]
        
        # Check if Zmk is outside the threshold
        if abs(zmk_val) > 1.96:
            row_data[month] = q_val
        else:
            row_data[month] = 0.0  # Ensure it's a float for consistency
    
    stations.append(row_data)

# Convert to DataFrame and reorder columns
result_df = pd.DataFrame(stations)
columns_order = ['Station'] + list(range(1, 13))
result_df = result_df[columns_order]

# Save to CSV
result_df.to_csv('rainfall_trend_results.csv', index=False, float_format='%.5f')