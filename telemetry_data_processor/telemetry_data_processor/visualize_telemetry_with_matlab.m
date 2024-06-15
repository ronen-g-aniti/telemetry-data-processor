% Visualize telemetry data from SQLite database

% Define the database connection
dbfile = "C:\Users\Ronen\Desktop\drone-algorithms\telemetry_data_processor\telemetry_data_processor\telemetry_data_processor\telemetry_data.db";
conn = sqlite(dbfile, 'readonly');

% Define the query
query = 'SELECT * FROM telemetry';

% Execute the query and fetch the data
data = fetch(conn, query);

% Close the database connection
close(conn);

% Extract the timestamp from each entry
timesteps = table2array(data(:, 1));

% Extract latitude
latitudes = table2array(data(:, 3));

% Extract longitude
longitudes = table2array(data(:, 4));

% Extract altitude
altitudes = table2array(data(:, 5));

% Extract speed
speeds = table2array(data(:, 6));

% Extract battery level
batteryLevels = table2array(data(:, 7));

% Plot 1: Geodetic Position
figure;
geoplot(latitudes, longitudes, '.-');
geobasemap satellite
title("Drone Path")

% Plot 2: Altitude
figure; 
plot(timesteps, altitudes);
xlabel("Timestep");
ylabel("Altitude"); 

% Plot 2: Speed
figure; 
plot(timesteps, speeds);
xlabel("Timestep");
ylabel("Speed (m/s)"); 

% Plot 2: Battery Level
figure; 
plot(timesteps, altitudes);
xlabel("Timestep");
ylabel("Battery Level");






