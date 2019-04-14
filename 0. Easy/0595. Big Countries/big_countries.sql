# selects the name, population, and area from countries with area above 3 million
# or population above 25 million
SELECT name, population, area FROM World WHERE area > 3000000 OR population > 25000000;
