from openai import OpenAI

from _gpt_model_enum import GptModelDefines
from constants import ROLE_DEFINE


def getModelName(model_enum: GptModelDefines) -> str:
	return model_enum.value


def getOfficialClient():
	return OpenAI()


def getProxyClient():
	return OpenAI(
		api_key='sk-XkrWCMiNpFLHkCnx68A119834534453aBe1f92Ea54405d83',
		base_url='https://orisound.cn/v1'
	)


client = getOfficialClient()
completion = client.chat.completions.create(
	model=getModelName(GptModelDefines.GPT4_TUBRO_PREVIEW_1106),
	messages=[
		{"role": "system", "content": ROLE_DEFINE},
		{"role": "user", "content": "springframework.validation是怎么实现入参校验的?"}
	]
)

print(completion)
resp_cont = completion.choices[0].message.content
print(resp_cont)
