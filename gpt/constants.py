# 英文提示
SYSTEM_PROMPT_ENGLISH = ('As a computer science teacher, you are expected to provide detailed '
                         'and accurate answers in English.')
# 中文提示
SYSTEM_PROMPT_CHINESE = ('As a computer science teacher, you are expected to provide detailed '
                         'and accurate answers in Chinese.')
# Prompt格式定义
SYSTEM_PROMPT_FORMAT = """
Instructions you must follow:
- Don't use code blocks for non-coding questions. Wrap code blocks in triple backticks, 
    and denote them with the language name.
- Math formula should be displayed in katex syntax
"""

LOCAL_API_PATH = 'D:\\github\\desktop\\python-beginner\\gpt\\api_key\\'
# 官方api key
OFFICIAL_API_FILE = LOCAL_API_PATH + 'official-api-key'
# 官方API URL代理(防封, 无墙)
OFFICIAL_SAFE_URL = LOCAL_API_PATH + 'official-safe-url'
# proxy api key
PROXY_API_FILE = LOCAL_API_PATH + 'proxy-api-key'
# proxy api url
PROXY_URL = LOCAL_API_PATH + 'proxy-url'

# store prompt file
LOCAL_FILES_PATH = 'D:\\github\\desktop\\python-beginner\\gpt\\'
# user prompt
PROMPT_FILE = LOCAL_FILES_PATH + 'files\\current_prompt'
# HISTORY_PROMPT = LOCAL_FILES_PATH + 'history\\history_prompts_others.md'
HISTORY_PROMPT = LOCAL_FILES_PATH + 'history\\history_prompts.md'

UTF8 = 'utf-8'
