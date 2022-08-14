import pandas as pd
import numpy as np

# Generate some random increasing data
data = pd.DataFrame(
    {'A': [np.random.uniform(0.1*i, 0.1*i + 1) for i in range(100)],
     'B': [np.random.uniform(0.1*i, 0.1*i + 1) for i in range(100)]}
)
# Create a Pandas Excel writer using XlsxWriter
excel_file = 'output.xlsx'
sheet_name = 'Data set'
writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
data.to_excel(writer, sheet_name=sheet_name)
# Access the XlsxWriter workbook and worksheet objects from the dataframe.
workbook = writer.book
worksheet = writer.sheets[sheet_name]
# Create a scatter chart object.
chart = workbook.add_chart({'type': 'scatter'})
# Get the number of rows and column index
max_row = len(data)
col_x = data.columns.get_loc('A') + 1
col_y = data.columns.get_loc('B') + 1
# Create the scatter plot, use a trendline to fit it
chart.add_series({
    'name':       "Samples",
    'categories': [sheet_name, 1, col_x, max_row, col_x],
    'values':     [sheet_name, 1, col_y, max_row, col_y],
    'marker':     {'type': 'circle', 'size': 4},
    'trendline': {'type': 'linear'},
})
# Set name on axis
chart.set_x_axis({'name': 'Concentration'})
chart.set_y_axis({'name': 'Measured',
                  'major_gridlines': {'visible': False}})
# Insert the chart into the worksheet in field D2
worksheet.insert_chart('D2', chart)
# Close and save the Excel file
writer.save()
