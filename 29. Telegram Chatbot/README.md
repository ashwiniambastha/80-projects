# How to Create Virtual Environment and Install Dependencies

conda create -n telebot python=3.8 -y

conda activate telebot

pip install -r requirements.txt


## Telegram setup:

1. search for botfather
2. /newbot
   - chatgpt88
   - chatgpt88_bot

   Now click on the url


### AIogram docs


4. Create a `.env` file in the root directory and add your OpenAI API key and Telegram BOT TOKEN as follows:

```ini
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TELEGRAM_BOT_TOKEN=xxxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```



# Docker Buid command:

docker build -t telegram-telebot .


# Run the Docker container with the following command, replacing the API key and bot token with your actual values:

docker run --rm -e OPENAI_API_KEY=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 -e TELEGRAM_BOT_TOKEN=8589138992:AAHeLLTlavt6UnOdJJKL9OpAI-wg3hCZ5t0 telegram-telebot