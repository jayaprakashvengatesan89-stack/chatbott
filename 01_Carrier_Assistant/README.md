# Carrier Assistant

A no-login Flask chatbot restricted to the **Career Guidance** domain and powered by **Gemini 3.1 Flash-Lite**.

## Project structure

```text
app.py
config.py
.env
requirements.txt
templates/
  index.html
README.md
.gitignore
```

## Features

- No login or registration.
- Gemini model: `gemini-3.1-flash-lite`.
- API key loaded from `.env` / environment variable, with an optional fallback variable in `app.py`.
- Server-side temporary Flask session history, isolated per browser session.
- Domain-only system instruction with an out-of-domain response.
- Responsive mobile, tablet, laptop, and desktop UI.
- UI title, domain, behavior, welcome text, theme, colors, quick prompts, history limits, and port are controlled from `config.py`.
- Clear-chat endpoint removes the current session's chat history.
- Gunicorn-compatible and Render-ready.

## Run locally

1. Open a terminal in this folder.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Edit `.env` and replace `PASTE_YOUR_GEMINI_API_KEY_HERE` with your Gemini API key.
5. Change `SECRET_KEY` to a long random string.
6. Start:

```bash
python app.py
```

Then open `http://127.0.0.1:5000` (or the port configured in `.env` / `config.py`).

## Configure the chatbot

Edit `config.py`:

- `CHATBOT_TITLE`
- `DOMAIN`
- `SYSTEM_PROMPT`
- `BEHAVIOR`
- `WELCOME_MESSAGE`
- `BOT_ICON`
- `UI_STYLE`
- `PRIMARY_COLOR`
- `ACCENT_COLOR`
- `BACKGROUND_COLOR`
- `PORT`
- generation and history limits

The API key can also be pasted into `APP_GEMINI_API_KEY` in `app.py`, but environment variables are safer.

## Deploy on Render

Create a **Web Service** from this project/repository.

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Environment variable: `GEMINI_API_KEY=your_real_key`
- Environment variable: `SECRET_KEY=your_long_random_secret`
- Recommended: `COOKIE_SECURE=true`

Render provides a `PORT` environment variable. `app.py` uses that value first and falls back to `PORT` in `config.py`.

## Session/privacy notes

Chat history is stored server-side in a temporary filesystem-backed Flask session cache, while the browser only receives a signed session cookie. Different browser sessions do not share chat histories through the application.

On ephemeral hosting such as Render, filesystem session data can disappear when an instance restarts or is replaced. This is intentional for this temporary-history example. For a larger multi-instance production service, replace the filesystem cache with a shared server-side session store such as Redis.

## Important

No AI prompt can mathematically guarantee perfect domain restriction. This project applies a strict system instruction, refuses out-of-domain requests, limits retained history, and does not expose other sessions through any route. Add application-specific validation or moderation if your production use case needs stronger guarantees.
