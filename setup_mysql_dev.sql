-- Create the database
CREATE DATABASE IF NOT EXISTS youandI;

-- Create the user and set the password
CREATE USER IF NOT EXISTS 'youandI_user'@'localhost' IDENTIFIED BY 'abdelmaliksalma';

-- Grant privileges to the user for the database
GRANT ALL PRIVILEGES ON `youandI`.* TO 'youandI_user'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

