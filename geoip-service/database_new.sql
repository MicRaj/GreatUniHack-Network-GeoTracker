CREATE TABLE geoip(
  network TEXT PRIMARY KEY,
  post_code TEXT,
  latitude REAL,
  longitude REAL,
  accuracy_radius INT,
  registered_country TEXT,
  represented_country TEXT,
  place TEXT
);