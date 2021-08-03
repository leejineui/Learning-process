--- Countries table 과  Locations table 을 이용하여, 나라 코드(), 나라 이름, 나라별 오피스의 수를 출력하라.   

 SELECT country_name, c.country_id, count(c.country_id) as The_number_of_offices 
 FROM countries c, locations i
 WHERE c.country_id = i.country_id
 GROUP BY c.country_id, country_name;

COUNTRY_NAME                                                                     COUN THE_NUMBER_OF_OFFICES
-------------------------------------------------------------------------------- ---- ---------------------
Italy                                                                            IT                       2
United Kingdom                                                                   UK                       3
Japan                                                                            JP                       2
Singapore                                                                        SG                       1
Brazil                                                                           BR                       1
Canada                                                                           CA                       2
Germany                                                                          DE                       1
Netherlands                                                                      NL                       1
Australia                                                                        AU                       1
Switzerland                                                                      CH                       2
China                                                                            CN                       1
Mexico                                                                           MX                       1
India                                                                            IN                       1
United States of America                                                         US                       4
