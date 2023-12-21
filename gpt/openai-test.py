from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
	model="gpt-3.5",
	# model="gpt-4",
	messages=[
		{"role": "system",
		 "content": "You are a teacher about computer science. and designed to output with chinese."},
		{"role": "user", "content": "请介绍一下python语言"}
	]
)

print(completion)
resp_cont = completion.choices[0].message.content
print(resp_cont)
