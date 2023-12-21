from enum import Enum


class GptModelDefines(Enum):
	class Gpt4Tubro:
		""" Gpt-4-Tubro
		最大支持128K的上下文, 功能比Gpt-4更强大
		"""

		preview_1106 = "gpt-4-1106-preview"
		""" input: $0.01 / 1K token; output: $0.03 / 1K tokens """
		vision_preview_1106 = "gpt-4-1106-vision-preview"
		""" input: $0.01 / 1K token; output: $0.03 / 1K tokens """

	class Gpt4:
		""" Gpt-4
		不如Gpt-4-Tubro, 不推荐使用
		"""

		gpt4 = "gpt-4"
		""" input: $0.03 / 1K token; output: $0.06 / 1K tokens """
		gpt4Large = "gpt4-32k"
		""" input: $0.06 / 1K token; output: $0.12 / 1K tokens """

	class Gpt3Point5Tubro:
		gpt = "gpt-3.5-turbo-1106"
		""" 最大支持16K上下文 
		input: $0.0010 / 1K token; output: $0.002 / 1K tokens """

		gpt4Large = "gpt-3.5-turbo-instruct"
		""" 最大支持4K上下文, 模型已较为过时
		input: $0.0015 / 1K token; output: $0.002 / 1K tokens """

# Assistants API 助手API
# Fine-tuning models 自定义微调模型
# Embedding models 嵌入模型
# Base models 基础模型
# Other Models:
# Image models
# Audio models
# 纯语音: Whisper	$0.006 / minute (rounded to the nearest second)
# 文本转语音: TTS	$0.015 / 1K characters
# 文件转语音(高清): TTS HD	$0.030 / 1K characters
