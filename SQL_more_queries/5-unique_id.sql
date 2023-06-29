-- 5-unique_id.sql

-- Script to create the table unique_id with specific columns and constraints

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
