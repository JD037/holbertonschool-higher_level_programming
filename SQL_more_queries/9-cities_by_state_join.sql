-- 9-cities_by_state_join.sql

-- Script to list all the cities along with their states

SELECT cities.id, cities.name, states.name 
FROM cities 
INNER JOIN states ON cities.state_id = states.id 
ORDER BY cities.id ASC;
