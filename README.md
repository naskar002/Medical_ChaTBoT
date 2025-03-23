# 🚀 End-to-End Medical Chatbot with Generative AI  

An AI-powered chatbot designed for **medical assistance**, built using **Flask, LangChain, Pinecone, and OpenAI GPT**.  
This project provides **real-time medical insights** and is **deployed on AWS with CI/CD using GitHub Actions**.

---

## 📌 Features  
✅ **AI-Powered Medical Chatbot** – Uses **GPT models** for generating responses.  
✅ **Retrieval-Augmented Generation (RAG)** – Fetches **relevant medical data** from Pinecone.  
✅ **Secure API Integration** – Uses **OpenAI API** for enhanced chatbot responses.  
✅ **AWS CI/CD Deployment** – Fully **automated deployment** using **GitHub Actions & AWS EC2**.  
✅ **Dockerized Application** – Runs inside **Docker containers** for **portability & scalability**.  

---

# 🛠️ Tech Stack  

| Technology  | Description |
|-------------|------------|
| **Python**  | Core programming language |
| **Flask**   | Backend framework |
| **LangChain** | Manages **AI prompt engineering** |
| **Pinecone** | Stores embeddings for **fast retrieval** |
| **GPT (OpenAI)** | Generates human-like responses |
| **Docker** | Containerization for easy deployment |
| **AWS EC2** | Cloud hosting |
| **AWS ECR** | Stores Docker images |
| **GitHub Actions** | Automates CI/CD pipeline |

---

# 🚀 How to Run Locally  
Follow these steps to **set up and run the chatbot on your local machine**.

### 🛠️ Step 1: Clone the Repository  
```bash
git clone https://github.com/YOUR-USERNAME/End-to-end-Medical-Chatbot-Generative-AI.git
cd End-to-end-Medical-Chatbot-Generative-AI
```

### 🏗️ Step 2: Set Up a Virtual Environment  
```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

### 📦 Step 3: Install Dependencies  
```bash
pip install -r requirements.txt
```

### 🔑 Step 4: Add API Keys  
Create a **.env** file in the project root and add your **Pinecone & OpenAI credentials**:  
```ini
PINECONE_API_KEY = "your_pinecone_api_key"
OPENAI_API_KEY = "your_openai_api_key"
```

### 📚 Step 5: Store Embeddings in Pinecone  
Run the following command to **store indexed embeddings** in Pinecone:  
```bash
python store_index.py
```

### 🚀 Step 6: Run the Chatbot  
```bash
python app.py
```

Now, open your browser and visit:  
```
http://localhost:5000
```

---

# 🌍 Deploying on AWS with CI/CD  

This project is **deployed on AWS** using **GitHub Actions** for **continuous deployment**.

## 🏗️ Step 1: Create an IAM User  
Create an **IAM user** with the following permissions:  
✅ **AmazonEC2FullAccess**  
✅ **AmazonEC2ContainerRegistryFullAccess**  

## 🏗️ Step 2: Create an AWS ECR Repository  
Create an **AWS Elastic Container Registry (ECR)** repository to store the Docker image.  
💾 **Save the ECR URI** (e.g., `970547337635.dkr.ecr.ap-south-1.amazonaws.com/medicalchatbot`).

## 🏗️ Step 3: Launch an EC2 Instance  
1. **Open AWS EC2 Console** → Click **Launch Instance**.  
2. Choose **Ubuntu 20.04** as the OS.  
3. Select an **instance type** (e.g., `t2.medium`).  
4. Configure security group to allow inbound **port 5000** (for Flask).  
5. Launch the instance and **connect via SSH**.

### 🐳 Step 4: Install Docker on EC2  
Connect to EC2 and install Docker:  
```bash
sudo apt-get update -y
sudo apt-get install -y docker.io
sudo usermod -aG docker ubuntu
newgrp docker
```

### 🔗 Step 5: Configure GitHub Secrets  
Go to **GitHub Repository → Settings → Secrets** and add:  
- `AWS_ACCESS_KEY_ID`  
- `AWS_SECRET_ACCESS_KEY`  
- `AWS_DEFAULT_REGION`  
- `ECR_REPO` (your ECR URI)  
- `PINECONE_API_KEY`  
- `OPENAI_API_KEY`  

### 🚀 Step 6: Push Docker Image to ECR  
Run the following command:  
```bash
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <ECR_URI>
docker build -t medicalchatbot .
docker tag medicalchatbot:latest <ECR_URI>:latest
docker push <ECR_URI>:latest
```

### 🚀 Step 7: Deploy on EC2  
SSH into EC2 and pull the Docker image:  
```bash
docker pull <ECR_URI>:latest
docker run -d -p 5000:5000 <ECR_URI>:latest
```

### ✅ Done! Your chatbot is now live on EC2! 🎉  

---

# 📜 Contribution Guide  
Want to contribute? Follow these steps:  

1. **Fork the repository**  
2. **Create a new branch** (`feature-xyz`)  
3. **Commit your changes** (`git commit -m "Added feature XYZ"`)  
4. **Push to GitHub** (`git push origin feature-xyz`)  
5. **Create a Pull Request** 🎉  


## ⭐ Don't forget to **star** this repo if you like it! ⭐  
