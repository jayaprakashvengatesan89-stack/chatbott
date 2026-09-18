# Chatbot identity
CHATBOT_TITLE = 'Carrier Assistant'
DOMAIN = 'Career Guidance'
BOT_ICON = '🧭'

# Domain rules sent to Gemini as part of the system instruction
SYSTEM_PROMPT = 'Help users explore careers, skills, resumes, interviews, job-search preparation, and professional development.'
BEHAVIOR = (
    "Be accurate, helpful, friendly, and concise. Explain clearly. "
    "Stay strictly within the configured domain. If the user asks something outside the domain, "
    "do not answer it; state that you can only help with the configured domain."
)
WELCOME_MESSAGE = 'Welcome! I’m Carrier Assistant. Ask me about careers, skills, resumes, interviews, or job preparation.'

# UI customization
UI_STYLE = 'aurora'
PRIMARY_COLOR = '#7c3aed'
ACCENT_COLOR = '#06b6d4'
BACKGROUND_COLOR = '#0f172a'
QUICK_PROMPTS = ['Suggest careers for my skills', 'Improve my resume', 'Prepare me for an interview']

# App/server configuration
PORT = 5000
SESSION_TTL_SECONDS = 60 * 60 * 6
MAX_HISTORY_MESSAGES = 20
MAX_USER_MESSAGE_CHARS = 6000

# Gemini generation settings
TEMPERATURE = 0.35
MAX_OUTPUT_TOKENS = 1200
