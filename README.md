# 🧩 Dynamic Load Balancer for CI/CD Workers

A lightweight **CI/CD Load Balancer** simulation built using **Python, Flask, and Docker Compose**.  
It demonstrates how jobs can be dynamically distributed across multiple workers — without using heavy tools like Jenkins or Kubernetes.

---

## 🚀 Features
- Dynamic job assignment to the least-loaded worker  
- Scalable design using **Docker Compose**  
- Two worker nodes simulated in isolated containers  
- Fast setup with **Flask microservices**  
- Great for learning **DevOps concepts** like load balancing and container orchestration  

---

## 🏗️ Project Structure
devops-project/
├── docker-compose.yml
├── balancer/
│ ├── app.py
│ └── Dockerfile
└── worker/
├── worker.py
└── Dockerfile

---

## ⚙️ How to Run

### 1️⃣ Start Docker
Make sure **Docker Desktop** is running.

### 2️⃣ Launch the containers
docker-compose up

### 3️⃣ Test the Load Balancer
curl -X POST http://localhost:8000/job -H "Content-Type: application/json" -d '{"task": "Build A"}'
curl -X POST http://localhost:8000/job -H "Content-Type: application/json" -d '{"task": "Build B"}'

curl -X POST http://localhost:8000/job -H "Content-Type: application/json" -d '{"task": "Build A"}'
curl -X POST http://localhost:8000/job -H "Content-Type: application/json" -d '{"task": "Build B"}'

🧠 Concepts Covered

Flask microservices

Containerization with Docker

Docker Compose networking

Load distribution and scaling

💡 Future Enhancements

Add web UI to monitor worker loads

Integrate with GitHub Actions for real CI/CD pipelines

Add a persistent database for job tracking