-- SQL script that lists all bands with Glam rock as main style ranked by longevity

SELECT band_name, (ifnull(split, 2023) - formed) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
