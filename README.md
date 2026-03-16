# 🇮🇳 Indian Legal AI Portal

A Flask-based web application that helps citizens understand Indian laws, file complaints, and ask legal questions.

## Features

- 👤 Citizen Registration and Login
- ⚖ AI Legal Question Chat
- 📄 Complaint Submission System
- 📚 Indian Constitution Articles
- 🗄 MySQL Database Integration
- 🎨 Government Theme UI

## Technologies Used

- Python (Flask)
- HTML
- CSS
- JavaScript
- MySQL

## Project Structure

project/
│
app.py
README.md

## Database Setup

CREATE DATABASE juris_ai_portal;

USE juris_ai_portal;

CREATE TABLE users(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100),
password VARCHAR(100)
);

CREATE TABLE complaints(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
complaint TEXT
);

## Run the Project

Install libraries:

pip install flask flask-mysqldb

Run application:

python app.py

Open in browser:

http://127.0.0.1:5000
