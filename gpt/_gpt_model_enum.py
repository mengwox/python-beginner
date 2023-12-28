from enum import Enum


class GptModelDefines(Enum):
	GPT4_TUBRO_PREVIEW_1106 = "gpt-4-1106-preview"
	""" input: $0.01 / 1K token; output: $0.03 / 1K tokens """
	GPT4_TUBRO_VISION_PREVIEW_1106 = "gpt-4-1106-vision-preview"
	""" input: $0.01 / 1K token; output: $0.03 / 1K tokens """
	# gpt4-tubro model: end

	GPT4 = "gpt-4"
	""" input: $0.03 / 1K token; output: $0.06 / 1K tokens """
	GPT4_32K = "gpt4-32k"
	""" input: $0.06 / 1K token; output: $0.12 / 1K tokens """
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
