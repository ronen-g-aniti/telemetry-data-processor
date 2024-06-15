import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('telemetry_data.db')

# Query telemetry data
df = pd.read_sql_query('SELECT * FROM telemetry', conn)

# close the connection
conn.close()

# Data processing
df['timestamp'] = pd.to_datetime(df['timestamp']) # Convert timestamp to datetime object
df.set_index('timestamp', inplace=True) # Set timestamp as index (inplace=True modifies the DataFrame in place)
# The reason for setting the timestamp as the index is to make it easier to plot the data

# Visualize
plt.figure(figsize=(10,6))

# Plot Latitude and Longitude
plt.subplot(2,2,1) # 2 rows, 2 columns, 1st subplot
plt.plot(df.index, df['latitude'], label='Latitude')
plt.plot(df.index, df['longitude'], label='Longitude')
plt.title('Latitude and Longitude Over Time')
plt.xlabel('Time')
plt.ylabel('Degrees')
plt.legend()

# Plot Altitude
plt.subplot(2,2,2) # 2 rows, 2 columns, 2nd subplot
plt.plot(df.index, df['altitude'], color='green')
plt.title('Altitude Over Time')
plt.xlabel('Time')
plt.ylabel('Altitude (meters)')
plt.legend()

# Plot Speed
plt.subplot(2,2,3) # 2 rows, 2 columns, 3rd subplot
plt.plot(df.index, df['speed'], color='red')
plt.title('Speed Over Time')
plt.xlabel('Time')
plt.ylabel('Speed (m/s)')
plt.legend()

# Plot Battery Level
plt.subplot(2,2,4) # 2 rows, 2 columns, 4th subplot
plt.plot(df.index, df['battery_level'], color='purple')
plt.title('Battery Level Over Time')
plt.xlabel('Time')
plt.ylabel('Battery Level (%)')
plt.legend()

plt.tight_layout() # Adjust subplots to fit into the figure area
plt.show()




