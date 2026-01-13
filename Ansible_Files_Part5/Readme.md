# 🌐 Flask Network Interface API

A Flask-based backend application that parses network interface data from a local source and exposes the results through HTTP endpoints.

This project demonstrates backend API development, data parsing, automated testing, and deployment automation using Ansible.

---

## 📌 Overview

The application reads network interface information from a text file and returns structured JSON responses through a Flask API.  
It simulates how backend services can expose system or network metadata in a controlled environment.

The project includes:
- Flask API endpoints
- Parsing logic for network interface data
- Automated tests using pytest
- Deployment and execution automation using Ansible

---

## 🚀 API Endpoints

### `GET /`
Returns a default response to verify the application is running.

**Response**

Default Home Page


---

### `GET /interfaces`
Parses network interface data and returns detected interfaces with their IPv4 addresses.

**Sample Response**
```json
{
  "ComputerInterfaces": {
    "eth0": "192.168.2.100",
    "eth1": "10.10.2.100",
    "eth2": "10.12.5.11",
    "lo": "127.0.0.1"
  }
}

🧠 Application Logic

    Extracts interface names and IPv4 addresses from raw interface output

    Filters valid interface and address pairs

    Returns data as structured JSON using Flask response objects

    Includes basic error handling to prevent application crashes

🧪 Testing

Automated tests are written using pytest to verify:

    Application startup

    Root endpoint availability

    Correct HTTP status responses

Tests use Flask’s built-in test client.
🤖 Automation with Ansible

An Ansible playbook is included to automate setup and execution tasks, including:

    Installing required system packages

    Cloning the application repository

    Installing Python dependencies

    Running the Flask application

    Verifying endpoint availability using HTTP requests

This demonstrates basic configuration management and service validation.
🛠️ Technologies Used

    Python

    Flask

    Pytest

    Ansible

    Linux

    Git

🎯 Purpose

This project was built to demonstrate:

    Backend API development with Flask

    Parsing and exposing system/network data

    Writing automated backend tests

    Automating application deployment and verification

    Understanding how backend services are deployed and validated

👤 Author

Johnny (Yoseph Gebre)
IT Graduate | Software Development
📄 License

This project is for educational and portfolio purposes.
