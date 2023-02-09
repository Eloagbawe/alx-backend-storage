-- This sql script queries the metal_bands table and lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, IF(ISNULL(split), 2020 - formed, split - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
