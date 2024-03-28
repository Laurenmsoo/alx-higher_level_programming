-- Lists all cities found in California

SELECT cities.id, cities.name
FROM cities
WHERE state_id = (
    SELECT states.id
    FROM states
    WHERE states.name = 'California'
    );
