# Multi-Agent-Support-System
An AI-powered Multi-Agent Support System designed to handle customer queries efficiently by simulating real-world support workflows. This project demonstrates how multiple intelligent agents can coordinate to understand user queries, generate appropriate responses, and escalate critical issues when necessary.

Project: Intelligent Multi-Agent Customer Support System

An AI-powered project demonstrating coordinated agent behaviour for real-world support tasks.

An AI-powered, coordinated multi-agent system that classifies customer queries, generates responses, and decides escalation using an orchestrator-based architecture.

⭐ 1. Overview

This project implements a Multi-Agent Customer Support System using Python.
It uses four main agents:

Intent Agent – Understands customer intent

Reply Agent – Generates professional responses

Escalation Agent – Decides if ticket needs human support

Orchestrator – Coordinates all agents and produces final output

This project is built for Google AI Agent Builder Capstone Project and showcases real-world agent collaboration.

🚀 2. Features

🔍 Automatic intent detection

💬 Human-like response generation

⚠️ Escalation prediction

🔗 Multi-agent coordination

📦 End-to-end executable Python script

🧠 Lightweight design for enterprise workflows

🏗️ 3. Architecture
User Query

     ↓
     
Intent Agent → Reply Agent → Escalation Agent

     ↓                ↓               ↓
     
               Orchestrator
               
     ↓
     
Final Response + Escalation Status

🔧 4. How It Works

1️⃣ User sends query
2️⃣ Orchestrator sends message to Intent Agent
3️⃣ Based on intent → Reply Agent generates answer
4️⃣ Escalation Agent decides if human help is needed
5️⃣ Final combined response returned

🧩 5. Project Structure

/multi-agent-support-system

│── orchestrator.py

│── agents/

│      ├── intent_agent.py

│      ├── reply_agent.py

│      ├── escalation_agent.py

│── main.py

│── README.md

🖥️ 6. How To Run
pip install -r requirements.txt
python main.py

🧪 7. Example Output
User: My refund is still not processed.
Intent: Refund Issue
Reply: "Your refund is under process. Please wait 2–3 business days."
Escalation: Yes → Human support required

📸 8. Project Images (for Capstone)

Architecture Diagram

How It Works Diagram

Features Image

Project Statement Image

Ending Slide Image
(You can upload inside a /images folder)

🧑‍💻 9. Full Python Code

Add your full working Python script here (we already created earlier; I can add again if you want).

🏅 10. Credits

Made by Megha Sahu

For Google AI Agent Capstone Project
