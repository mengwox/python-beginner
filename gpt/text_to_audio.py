from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
	model="tts-1",
	voice="shimmer",
	input="Hello world! This is a streaming test.",
)

print(response)
response.stream_to_file("output.aac")
