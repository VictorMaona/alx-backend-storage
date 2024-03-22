-- ranks all bands with Glam rock as their primary genre according to how long they have been around

SELECT
    band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';
