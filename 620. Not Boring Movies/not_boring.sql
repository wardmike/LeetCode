# selects all info with an odd id and description that doesn't contain "boring"; orders by rating
SELECT * FROM cinema WHERE id % 2 = 1 AND description <> "boring" ORDER BY rating DESC;
