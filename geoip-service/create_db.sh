#!/bin/bash
rm -f database.db*
sqlite3 -batch database.db <<"EOF"
.read database.sql
.mode csv
.import geodata.csv geoip
.import countries.csv cities
EOF