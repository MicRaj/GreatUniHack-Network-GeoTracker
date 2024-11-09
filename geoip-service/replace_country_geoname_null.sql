SELECT
  geoip.network,
  geoip.geoname_id,
  geoip.postal_code,
  geoip.latitude,
  geoip.longitude,
  geoip.accuracy_radius,
  geoip.represented_country_geoname_id,
  COALESCE(c1.asciiname, NULL) AS registered_country,
  COALESCE(c2.asciiname, NULL) AS represented_country
FROM
  geoip
LEFT JOIN
  cities c1 ON COALESCE(geoip.registered_country_geoname_id, -1) = c1.geonameid
LEFT JOIN
  cities c2 ON COALESCE(geoip.represented_country_geoname_id, -1) = c2.geonameid
LIMIT
  10
;