-- This sql script queries the metal_bands table and lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (IFNULL(split, '2020') - formed) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', IFNULL(style, ''))
ORDER BY lifespan DESC;
