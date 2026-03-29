# Matrix Vault Bot

A Python bot for Matrix chat that securely retrieves credentials from Vault using `.env`. This project demonstrates secure handling of secrets and asynchronous chat automation.

---

## Features

- Connects to a Matrix server and listens to messages in real time  
- Responds to commands, e.g., `"hello"` → `"goodbye"`  
- Securely fetches username and password from Vault using `.env`  
- Asynchronous architecture using `nio` for efficient message handling  
- Easy setup for local development and testing

---

## Tech Stack

- Python 3.11+  
- [matrix-nio](https://github.com/poljar/matrix-nio) for Matrix client  
- [hvac](https://github.com/hvac/hvac) for Vault integration  
- `.env` for local secret management  

---

## Setup

1. Clone the repository:

```bash
git clone git@github.com:Jordenproject/matrix-vault-bot.git
cd matrix-vault-bot

Install dependencies:
pip install -r requirements.txt

Create a .env file in the project root:
VAULT_TOKEN=your_vault_token_here

Run the bot:
python main.py

Notes
.env is included in .gitignore — never commit your secrets
Ensure your Vault token has proper permissions to read secrets
Long-term, SSH keys are used for GitHub authentication instead of HTTPS tokens
The bot is designed for educational and development purposes

License
MIT License
---

 


