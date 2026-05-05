#  DevOps Project – Flask App with Docker, CI/CD & AWS Deployment

## Project Overview

This project demonstrates a complete DevOps lifecycle by building, containerizing, and deploying a Flask-based web application using Docker, CI/CD pipeline, and AWS EC2.

---

##  Tech Stack

* Python (Flask)
* Docker & Docker Compose
* GitHub Actions (CI/CD)
* AWS EC2 (Amazon Linux)
* MongoDB

---

##  Features

* REST API using Flask
* Multi-container setup (Flask + MongoDB)
* CI/CD pipeline for automated build & testing
* Cloud deployment on AWS EC2
* Health check endpoint

---

##  Project Structure

devops-project/
│── app.py
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── .github/workflows/ci-cd.yml

---

##  Docker Setup

### Build & Run

```bash
docker-compose up --build -d
```

---

##  CI/CD Pipeline

Implemented using GitHub Actions:

* Automatically builds Docker image
* Runs container test
* Verifies application health endpoint

---

## ☁️ AWS Deployment

Steps:

1. Launch EC2 instance (Amazon Linux)
2. Install Docker & Docker Compose
3. Clone repository
4. Run docker-compose
5. Configure Security Group (port 5000)

---

## Live Application

Access the app:
http://16.171.162.19:5000

Health Check:
http://16.171.162.19:5000/health

---

##  API Endpoints

| Method | Endpoint  | Description  |
| ------ | --------- | ------------ |
| GET    | /         | Home route   |
| GET    | /health   | Health check |
| POST   | /add_user | Add user     |
| GET    | /users    | Get users    |

---

## 📈 Future Improvements

* Add Nginx & HTTPS
* Kubernetes deployment
* Monitoring (Prometheus/Grafana)
* Auto deployment (CD)

---

##  Key Learnings

- Docker containerization and image creation  
- Managing multi-container applications using Docker Compose  
- Implementing CI/CD pipelines using GitHub Actions  
- Deploying applications on AWS EC2 (Amazon Linux)  
- Configuring Security Groups for public access  
- Debugging real-world deployment issues  

##  Author

Karthik Varma
