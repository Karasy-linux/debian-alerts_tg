Debian Telegram Notifier

A lightweight Python-based utility designed to send instant notifications to a Telegram chat. This tool is particularly useful for Linux users who want to receive alerts when long-running terminal processes (like system updates or script executions) are completed.
🚀 Features

    Instant Alerts: Sends text messages via the Telegram Bot API.

    CLI Integration: Can be easily chained with other bash/fish commands using &&.

    Secure Configuration: Uses a separated configuration system to keep sensitive API tokens safe.

    Lightweight: Minimal dependencies, focused on speed and simplicity.

🛠 Installation

    Clone the repository:
    Bash

git clone git@github.com:FAnterrr/debian-alerts_tg.git
cd debian-alerts_tg

Set up a virtual environment:
Bash

python3 -m venv .venv
source .venv/bin/activate  # for bash
# or source .venv/bin/activate.fish for fish shell

Install dependencies:
Bash

    pip install requests

⚙️ Configuration

Create a config.py file in the root directory (this file is ignored by git for security):
Python

# config.py
BOT_TOKEN = "your_bot_token_here"
CHAT_ID = 123456789  # your chat id as an integer

📖 Usage

Run the script directly from the terminal:
Bash

python3 send_tg.py "Your message here"

Pro Tip for Debian/Linux users:

Chain it with system updates to get notified on your phone when they finish:
Bash

sudo apt update && sudo apt upgrade -y && python3 ~/path/to/send_tg.py "System update complete!"

🛡 License

This project is open-source and available under the MIT License.
