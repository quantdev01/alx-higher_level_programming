-- Reading the user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- creating the user
CREATE USER 'user_0d_2' IDENTIFIED BY 'hbtn_0d_2';

-- Giving Select privileges
GRANT SELECT
ON hbtn_0d_2
TO user_0d_2@localhost;
