Flask Network Interfaces API (Assignment 4)

A Flask-based REST API that parses Linux network interface output from a file and exposes the data as JSON. This project demonstrates backend API development, file parsing, containerization with Docker, and basic API testing using pytest.

🚀 Project Overview

This application reads network interface data from a text file (interfaces.txt), extracts interface names and IPv4 addresses, and serves them through a REST endpoint.

The project includes:

A Flask web server

File parsing logic for Linux network interfaces

Docker configuration

Automated unit testing with pytest

⚙️ Application Endpoints
GET /

Returns a default welcome message.

Response

Default Home Page

GET /iproutes

Placeholder endpoint for IP routing functionality.

Response

ip routes

GET /interfaces

Reads interfaces.txt, extracts interface names and IPv4 addresses, and returns them as JSON.

Example Response

{
  "ComputerInterfaces": {
    "eth0": "192.168.2.100",
    "eth1": "10.10.2.100",
    "eth2": "10.12.5.11",
    "lo": "127.0.0.1"
  }
}

🧠 Key Functions
getInetAddress(line)

Extracts the IPv4 address from a line containing inet addr:.

getInetName(line)

Extracts the network interface name from a line containing Link.

🐳 Docker Setup

The project includes a Dockerfile to containerize the Flask application.

Dockerfile Highlights

Uses Ubuntu base image

Installs Python and pip

Exposes port 5000

Copies application files into /home/assignment4

Build the Docker Image
docker build -t flask-interfaces-app .

Run the Container
docker run -p 5000:5000 flask-interfaces-app


The API will be accessible at:

http://localhost:5000

🧪 Testing

Unit tests are written using pytest and Flask’s test client.

Test Coverage

Verifies / endpoint returns status 200

Confirms correct response content

Run Tests
pytest

📦 Dependencies
Flask==2.0.2
pytest


Install manually with:

pip install Flask==2.0.2 pytest

🎯 Learning Objectives Demonstrated

REST API development with Flask

Parsing structured system output

JSON response handling

Docker containerization

Backend testing with pytest

✅ Notes

Interface data is read from a static file for portability and testing

Designed for Linux-style ifconfig output

Basic error handling included to prevent crashes
