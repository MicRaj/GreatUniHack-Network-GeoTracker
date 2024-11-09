CREATE TABLE cities (
    id INTEGER,
    geonameid INTEGER PRIMARY KEY,
    asciiname TEXT,
    latitude REAL,
    longitude REAL,
    countrycode TEXT
);

CREATE TABLE geoip (
    network TEXT,
    geoname_id INTEGER,
    registered_country_geoname_id INTEGER,
    represented_country_geoname_id INTEGER,
    postal_code TEXT,
    latitude REAL,
    longitude REAL,
    accuracy_radius INTEGER
);

CREATE INDEX idx_combined_