from constants import SYSTEM_PROMPT
from gpt_utils import *

client = official_client()
completion = client.chat.completions.create(
	model=get_model_name(GptModelDefines.GPT4_TUBRO_PREVIEW_1106),
	messages=[
		{"role": "system", "content": SYSTEM_PROMPT},
		{"role": "user", "content": "springframework.validation是怎么实现入参校验的?"}
	]
)

print(completion)
resp_cont = completion.choices[0].message.content
print(resp_cont)
