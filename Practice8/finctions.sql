-- SEARCH FUNCTION
DROP FUNCTION IF EXISTS search_contacts(TEXT);

CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(
    first_name VARCHAR,
    last_name VARCHAR,
    phone VARCHAR,
    email VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT c.first_name, c.last_name, c.phone, c.email
    FROM contacts c
    WHERE c.first_name ILIKE '%' || pattern || '%'
       OR c.last_name ILIKE '%' || pattern || '%'
       OR c.phone ILIKE '%' || pattern || '%'
       OR c.email ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- PAGINATION FUNCTION
DROP FUNCTION IF EXISTS get_contacts_paginated(INTEGER, INTEGER);

CREATE OR REPLACE FUNCTION get_contacts_paginated(limit_val INT, offset_val INT)
RETURNS TABLE(
    id INT,
    first_name VARCHAR,
    last_name VARCHAR,
    phone VARCHAR,
    email VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.first_name, c.last_name, c.phone, c.email
    FROM contacts c
    ORDER BY c.id
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;