import traceback
from typing import List

from openai import OpenAI

from .constants import OFFICIAL_API_FILE, PROXY_API_FILE, PROXY_URL, UTF8
from .gpt_model_enum import GptModelDefines


def get_file_content(file_path: str) -> str:
	"""
	根据文件路径, 读取文件内容, 去除首尾空后返回
	:param file_path: path of file, stored api key
	:return: api key
	"""
	try:
		with open(file_path, 'r', encoding=UTF8) as file:
			content = file.read()
		return content.strip()
	except FileNotFoundError:
		traceback.print_exc()
		print("文件未找到，请检查文件路径是否正确。")


def official_api_key() -> str:
	return get_file_content(OFFICIAL_API_FILE)


def proxy_api_key() -> str:
	return get_file_content(PROXY_API_FILE)


def get_model_name(model_enum: GptModelDefines) -> str:
	return model_enum.value


def official_client():
	return OpenAI(api_key=official_api_key())


def proxy_client():
	return OpenAI(
		api_key=get_file_content(PROXY_API_FILE),
		base_url=get_file_content(PROXY_URL)
	)


def get_model_list() -> List[str]:
	client = official_client()
	models = client.models.list()
	model_names = list()
	for model in models:
		model_names.append(model.id)
	model_names.sort()
	return model_names
