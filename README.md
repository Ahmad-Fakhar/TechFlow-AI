# 🚀 **TechFlow AI - Voice Commerce for WhatsApp**

<div align="center">

![TechFlow AI Banner](https://img.shields.io/badge/TechFlow-AI-blue?style=for-the-badge&logo=whatsapp&logoColor=white)

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![GPT-5](https://img.shields.io/badge/GPT--5-Ready-green.svg)](https://openai.com/)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-Business_API-25D366.svg)](https://www.whatsapp.com/business/api)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Live-success.svg)]()

**🌍 Democratizing E-Commerce for 2 Billion WhatsApp Users**

[Live Demo](https://wa.me/14155238886) • [Video Demo](https://youtube.com/demo) • [Documentation](docs/) • [Dashboard](https://techflow-ai.streamlit.app)

</div>

---

## 📋 **Table of Contents**

- [🎯 Overview](#-overview)
- [🔥 Problem We Solve](#-problem-we-solve)
- [💡 Solution](#-solution)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Quick Start](#-quick-start)
- [📱 Usage](#-usage)
- [🏗️ Architecture](#️-architecture)
- [📊 Results](#-results)
- [🗺️ Roadmap](#️-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📞 Contact](#-contact)

---

## 🎯 **Overview**

TechFlow AI transforms WhatsApp into a powerful voice commerce platform, enabling 2 billion users worldwide to shop using voice messages in their native language. No typing, no app downloads - just speak and shop!

### **🏆 Hackathon Winner - AI Innovation Challenge 2024**

```python
# Shop in any language with just voice
"Bhai, mujhe laptop chahiye" → 💻 Shows laptops → ✅ Order confirmed
"I need iPhone under $500" → 📱 Shows options → ✅ Order placed
"আমি জুতা কিনতে চাই" → 👟 Shows shoes → ✅ Order done
```

---

## 🔥 **Problem We Solve**

<div align="center">

| Problem | Impact |
|---------|--------|
| 780 million people can't type efficiently | Excluded from e-commerce |
| 65% prefer voice over text | No voice shopping solution |
| Language barriers | 87% customer loss |
| **Lost Opportunity** | **$500 Billion annually** |

</div>

### **Real Stories:**
- 👵 **Fatima (Karachi):** "I can't type in English but want to shop online"
- 🧓 **Rahman's Mother (Dhaka):** "I have money but can't use shopping apps"
- 👨 **Carlos (São Paulo):** "My grandparents need voice shopping"

---

## 💡 **Solution**

### **How It Works - 3 Simple Steps:**

```mermaid
graph LR
    A[🎤 Voice Message] --> B[🤖 AI Processing]
    B --> C[✅ Order Confirmed]
    
    style A fill:#25D366
    style B fill:#0066CC
    style C fill:#00C851
```

1. **Send Voice Note** - Customer sends WhatsApp voice message in ANY language
2. **AI Processes** - GPT-5 understands intent, language, and context instantly
3. **Order Complete** - Confirmation sent, order processed, customer happy!

---

## ✨ **Features**

### **🌍 Multilingual Support**
- ✅ 60+ languages supported
- ✅ Automatic language detection
- ✅ Mixed language understanding
- ✅ Regional dialects & accents

### **🛍️ Shopping Features**
- 🛒 Voice-based product search
- 💰 Budget-based recommendations
- 📦 Multi-item cart management
- 🎯 Personalized suggestions
- 📊 Order tracking
- 💳 Multiple payment options

### **🤖 AI Capabilities**
- 🧠 GPT-5 with 256K context window
- 🎤 Whisper API for transcription
- 💬 Natural conversation flow
- 🔄 Context retention across messages
- ⚡ 1.2 second response time

### **👨‍💼 Merchant Dashboard**
- 📈 Real-time analytics
- 📊 Sales tracking
- 👥 Customer insights
- 📦 Inventory management
- 💼 Order management

---

## 🛠️ **Tech Stack**

<div align="center">

| Layer | Technology | Purpose |
|-------|------------|---------|
| **AI Engine** | GPT-5, Whisper API | Language processing & voice transcription |
| **Backend** | Python, FastAPI, Flask | API & webhook handling |
| **Database** | PostgreSQL (Neon) | Cloud database |
| **Messaging** | Twilio, WhatsApp Business API | Communication layer |
| **Frontend** | Streamlit, Plotly | Dashboard & analytics |
| **Infrastructure** | Docker, ngrok | Deployment & tunneling |

</div>

---

## 🚀 **Quick Start**

### **Prerequisites**

```bash
Python 3.12+
PostgreSQL
Twilio Account
OpenAI API Key
WhatsApp Business Account (or Sandbox)
```

### **Installation**

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/techflow-ai.git
cd techflow-ai
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your credentials
```

```env
# .env file
OPENAI_API_KEY=your_openai_key
TWILIO_ACCOUNT_SID=AC8469f346402f3d573f3cd5babb542b30
TWILIO_AUTH_TOKEN=your_auth_token
DATABASE_URL=postgresql://user:pass@host/dbname
```

4. **Initialize database**
```bash
python database.py
```

5. **Start the webhook server**
```bash
python whatsapp_webhook.py
```

6. **Set up ngrok tunnel**
```bash
ngrok http 5000
# Copy the HTTPS URL
```

7. **Configure Twilio webhook**
```
Go to Twilio Console > WhatsApp Sandbox
Set webhook URL: https://your-ngrok-url.ngrok.io/webhook
```

8. **Launch dashboard (optional)**
```bash
streamlit run hackathon_dashboard.py
```

---

## 📱 **Usage**

### **For Customers:**

1. **Join Sandbox (Development)**
   - Send WhatsApp message to: **+1 415 523 8886**
   - Type: `join quite-putting`

2. **Start Shopping**
   ```
   Send: "Hello"