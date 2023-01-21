# Remote terminal

A telegram bot to remotely interact with and monitor servers

## Features

### Commands

### Monitors

## Deployment

### 1. Fetch `docker-compose.yml` and `env.template` files

```bash
wget https://github.com/giobyte8/rterminal/raw/main/docker-compose.yml
wget https://github.com/giobyte8/rterminal/raw/main/env.template
```

### 2. Prepare your password

In order to allow only trusted users to interact with your bot
they must enter a passphare.

You'll need to pass a hashed password to **rterminal**. Use below
command to hash your own password.

```bash
docker run -it --rm                        \
    giobyte8/rterminal:1.0.2               \
    python hash_pw.py <YOUR_OWN_PASSWORD>

# This is the password you will use to authenticate
# against rterminal
```

### 3. Prepare your telegram bot

Message @BotFather on Telegram to register your bot and receive its
authentication token.

Official docs: https://core.telegram.org/bots#how-do-i-create-a-bot

### 4. Setup your own environment

Prepare your `.env` file with appropiate values corresponding to your
own env

```bash
cp env.template .env
vim .env

# Enter your own values including hashed password and telegram
# bot token
```

> Pay attention to comment in .env file about how to escape '$' signs
> in hashed password

### 5. Run rterminal

With `.env` and `docker-compose.yml` in place, run **rterminal**
with:

```bash
docker-compose up -d
```

🎉 - Now you can message your telegram bot to use **reterminal** - 🎉
