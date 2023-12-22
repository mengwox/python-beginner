from openai import OpenAI

from _gpt_model_enum import GptModelDefines


def getModelName(model_enum: GptModelDefines) -> str:
	return model_enum.value


client = OpenAI()

completion = client.chat.completions.create(
	model=getModelName(GptModelDefines.GPT3_5_TURBO),
	messages=[
		{"role": "system",
		 "content": "You are a teacher about computer science. and designed to output with chinese."},
		{"role": "user", "content": "请介绍一下python语言"}
	]
)

print(completion)
resp_cont = completion.choices[0].message.content
print(resp_cont)
