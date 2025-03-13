from enum import Enum


class GptModelDefines(Enum):
	O1_LATEST = "o1-preview"
	O1_MINI = "o1-mini"
	# chatgpt-4o-latest
	CHATGPT_4o_LATEST = "chatgpt-4o-latest"
	GPT4_O = "gpt-4o"
	GPT4_PREVIEW = "gpt-4-0125-preview"

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
	DEFAULT = O1_LATEST


class DeepseekModel(Enum):
	"""
    DEEPSEEK AI大模型枚举类
    """
	# model='deepseek-chat' 即可调用 DeepSeek-V3
	DEFAULT = 'deepseek-chat'
	# model='deepseek-reasoner'，即可调用 DeepSeek-R1
	REASONER = 'deepseek-reasoner'
	# DeepSeek-R1, 字节部署版本
	BYTE_DANCE_R1 = 'DeepSeek-R1'
