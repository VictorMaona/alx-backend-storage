-- script lists nations of origin of bands in order
-- by number of (non-unique) fans
SELECT origin, SUM(fans) as nb_fans from metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
