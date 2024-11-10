rm -f database.db*
sqlite3 -batch database.db <<"EOF"
.read database_new.sql
.mode csv
.import combined.csv geoip
EOF