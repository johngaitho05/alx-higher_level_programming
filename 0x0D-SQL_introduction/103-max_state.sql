-- This script displays the maximum temperature for each state
SELECT state, MAX(value) as max_temp from temperatures GROUP BY state ORDER BY state;
