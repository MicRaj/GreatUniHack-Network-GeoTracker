CREATE TABLE
combined
AS
SELECT
  geoip.network as network,
  geoip.postal_code as post_code,
  geoip.latitude as latitude,
  geoip.longitude as longitude,
  geoip.accuracy_radius as accuracy_radius,
  COALESCE(c1.asciiname, NULL) AS registered_country,
  COALESCE(c2.asciiname, NULL) AS represented_country,
  COALESCE(c3.asciiname, NULL) AS place
FROM
  geoip
LEFT JOIN
  cities c1 ON COALESCE(geoip.registered_country_geoname_id, -1) = c1.geonameid
LEFT JOIN
  cities c2 ON COALESCE(geoip.represented_country_geoname_id, -1) = c2.geonameid
LEFT JOIN
  cities c3 ON COALESCE(geoip.geoname_id, -1) = c3.geonameid
;