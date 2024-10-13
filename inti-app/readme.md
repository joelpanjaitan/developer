Query to create database needed for the backend system

CREATE DATABASE api_db

USE api_db

CREATE TABLE employees (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
position VARCHAR(100) NOT NULL,
salary DECIMAL(10, 2) NOT NULL
)
