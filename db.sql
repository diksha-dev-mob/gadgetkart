CREATE DATABASE IF NOT EXISTS gadgetkart;

-- Switch to your database
USE gadgetkart;

-- Create a users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Insert a sample user
INSERT INTO users (email, password) VALUES ('test@example.com', 'password123');

-- Creates a contacts table
CREATE TABLE IF NOT EXISTS contacts (
id INT AUTO_INCREMENT PRIMARY KEY,
fullname VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL,
phone VARCHAR(15),
message TEXT NOT NULL);