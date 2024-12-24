from enum import Enum


class GptModelDefines(Enum):
	# chatgpt-4o-latest
	CHATGPT_4o_LATEST = "chatgpt-4o-latest"
	GPT4_O = "gpt-4o"

	GPT4_PREVIEW = "gpt-4-0125-preview"

	GPT4_VISION_PREVIEW = "gpt-4-vision-preview"
	""" input: $0.01 / 1K token; output: $0.03 / 1K tokens """

	GPT4_TUBRO_PREVIEW = "gpt-4-turbo-preview"
	""" input: $0.01 / 1K token; output: $0.03 / 1K tokens """

	GPT4 = "gpt-4"
	""" input: $0.03 / 1K token; output: $0.06 / 1K tokens """

	UNAVAILABLE_GPT4_32K = "gpt-4-32k"
	""" 
		input: $0.06 / 1K token; output: $0.12 / 1K tokens 
		目前不可用
	"""
	# gpt4 model: end

	GPT3_5_TURBO = "gpt-3.5-turbo"
	""" 最大支持16K上下文 
	input: $0.0010 / 1K token; output: $0.002 / 1K tokens """
	GPT_3_5_TUBO_INSTRUCT = "gpt-3.5-turbo-instruct"
	""" 最大支持4K上下文, 模型已较为过时
	input: $0.0015 / 1K token; output: $0.002 / 1K tokens """
	# gpt3.5-tubro model: end

	TTS = 'tts-1'
	""" 文本转语音: TTS	$0.015 / 1K characters """
	TTS_HD = 'tts-1-hd'
	""" 文件转语音(高清): TTS HD	$0.030 / 1K characters """
	# text to audio model: end

	WHISPER = 'whisper-1'
	""" $0.006 / minute (四舍五入, 精确到秒) """
	# audio to text model: end

	# Assistants API 助手API
	# Fine-tuning models 自定义微调模型
	# Embedding models 嵌入模型
	# Base models 基础模型
	# Other Models:
	# Image models
	DEFAULT = GPT3_5_TURBO
