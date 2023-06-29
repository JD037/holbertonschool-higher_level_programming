-- 3-force_name.sql

-- Script to create the table force_name with specific columns and constraints

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
