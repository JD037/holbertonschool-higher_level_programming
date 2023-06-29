-- 4-never_empty.sql

-- Script to create the table id_not_null with specific columns and default value constraints

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
