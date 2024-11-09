    SELECT
    geoip.network,
    geoip.geoname_id,
    geoip.postal_code,
    geoip.latitude,
    geoip.longitude,
    geoip.accuracy_radius,
    geoip.represented_country_geoname_id,
    c1.asciiname as registered_country,
    c2.asciiname as represented_country
FROM
    geoip
    INNER JOIN cities c1 on geoip.registered_country_geoname_id = c1.geonameid
    INNER JOIN cities c2 on geoip.represented_country_geoname_id = c2.geonameid
LIMIT
    1
    ;