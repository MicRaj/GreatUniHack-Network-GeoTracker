"""
# GeoLite2
network,geoname_id,registered_country_geoname_id,represented_country_geoname_id,is_anonymous_proxy,is_satellite_provider,postal_code,latitude,longitude,accuracy_radius,is_anycast
1.0.0.0/24,,2077456,,0,0,,,,,
1.0.1.0/24,1814991,1814991,,0,0,,34.7732,113.7220,1000,
1.0.2.0/23,1814991,1814991,,0,0,,34.7732,113.7220,1000,
1.0.4.0/22,2077456,2077456,,0,0,,-33.4940,143.2104,1000,
1.0.8.0/21,1814991,1814991,,0,0,,34.7732,113.7220,1000,
1.0.16.0/20,1861060,1861060,,0,0,,35.6897,139.6895,500,
1.0.32.0/19,1814991,1814991,,0,0,,34.7732,113.7220,1000,
1.0.64.0/20,1862415,1861060,,0,0,730-0851,34.3927,132.4501,10,
1.0.80.0/20,1857550,1861060,,0,0,690-0871,35.4785,133.0489,100,
"""

"""
# allCountries.txt
2994701	Roc Meler	Roc Meler	Roc Mele,Roc Meler,Roc Mélé	42.58765	1.7418	T	PK	AD	AD,FR	02				0	2811	2348	Europe/Andorra	2023-10-03
3017832	Pic de les Abelletes	Pic de les Abelletes	Pic de la Font-Negre,Pic de la Font-Nègre,Pic de les Abelletes	42.52535	1.73343	T	PK	AD	FR	A9	66	663	66146	0		2411	Europe/Andorra	2014-11-05
3017833	Estany de les Abelletes	Estany de les Abelletes	Estany de les Abelletes,Etang de Font-Negre,Étang de Font-Nègre	42.52915	1.73362	H	LK	AD	FR	A9				0		2260	Europe/Andorra	2014-11-05
3023203	Port Vieux de la Coume d’Ose	Port Vieux de la Coume d'Ose	Port Vieux de Coume d'Ose,Port Vieux de Coume d’Ose,Port Vieux de la Coume d'Ose,Port Vieux de la Coume d’Ose	42.62568	1.61823	T	PASS	AD		00				0		2687	Europe/Andorra	2014-11-05
3029315	Port de la Cabanette	Port de la Cabanette	Port de la Cabanette,Porteille de la Cabanette	42.6	1.73333	T	PASS	AD	AD,FR	B3	09	091	09139	0		2379	Europe/Andorra	2014-11-05
3034945	Roc de Port Dret	Roc de Port Dret		42.60288	1.45736	T	PK	AD	AD,FR	04				0	2735	2650	Europe/Andorra	2023-12-24
3038814	Costa de Xurius	Costa de Xurius		42.50692	1.47569	T	SLP	AD		07				0		1839	Europe/Andorra	2015-03-08
3038815	Font de la Xona	Font de la Xona		42.55003	1.44986	H	SPNG	AD		04				0		1976	Europe/Andorra	2010-01-11
3038816	Xixerella	Xixerella		42.55327	1.48736	P	PPL	AD		04				0		1417	Europe/Andorra	2009-04-24
3038818	Riu Xic	Riu Xic		42.57165	1.67554	H	STM	AD		02				0		1851	Europe/Andorra	2014-12-03
"""

"""
The main 'geoname' table has the following fields :
---------------------------------------------------
geonameid         : integer id of record in geonames database
name              : name of geographical point (utf8) varchar(200)
asciiname         : name of geographical point in plain ascii characters, varchar(200)
alternatenames    : alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table, varchar(10000)
latitude          : latitude in decimal degrees (wgs84)
longitude         : longitude in decimal degrees (wgs84)
feature class     : see http://www.geonames.org/export/codes.html, char(1)
feature code      : see http://www.geonames.org/export/codes.html, varchar(10)
country code      : ISO-3166 2-letter country code, 2 characters
cc2               : alternate country codes, comma separated, ISO-3166 2-letter country code, 200 characters
admin1 code       : fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; varchar(20)
admin2 code       : code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80) 
admin3 code       : code for third level administrative division, varchar(20)
admin4 code       : code for fourth level administrative division, varchar(20)
population        : bigint (8 byte int) 
elevation         : in meters, integer
dem               : digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
timezone          : the iana timezone id (see file timeZone.txt) varchar(40)
modification date : date of last modification in yyyy-MM-dd format
"""

