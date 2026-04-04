-- UPSERT
DROP PROCEDURE IF EXISTS upsert_contact(VARCHAR, VARCHAR, VARCHAR, VARCHAR);

CREATE OR REPLACE PROCEDURE upsert_contact(
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_phone VARCHAR,
    p_email VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM contacts 
        WHERE first_name = p_first_name AND last_name = p_last_name
    ) THEN
        UPDATE contacts
        SET phone = p_phone,
            email = p_email
        WHERE first_name = p_first_name AND last_name = p_last_name;
    ELSE
        INSERT INTO contacts(first_name, last_name, phone, email)
        VALUES(p_first_name, p_last_name, p_phone, p_email);
    END IF;
END;
$$;


-- BULK INSERT
DROP PROCEDURE IF EXISTS insert_many_contacts(TEXT[], TEXT[], TEXT[], TEXT[]);

CREATE OR REPLACE PROCEDURE insert_many_contacts(
    first_names TEXT[],
    last_names TEXT[],
    phones TEXT[],
    emails TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(first_names, 1) LOOP
        IF phones[i] ~ '^[0-9]{10,}$' THEN
            INSERT INTO contacts(first_name, last_name, phone, email)
            VALUES (first_names[i], last_names[i], phones[i], emails[i]);
        ELSE
            RAISE NOTICE 'Invalid phone: %', phones[i];
        END IF;
    END LOOP;
END;
$$;


-- DELETE
DROP PROCEDURE IF EXISTS delete_contact(VARCHAR);

CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE first_name = p_value 
       OR last_name = p_value
       OR phone = p_value
       OR email = p_value;
END;
$$;