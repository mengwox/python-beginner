from .constants import OFFICIAL_API_FILE, PROXY_API_FILE, UTF8


def get_api_key(file_path: str) -> str:
	"""
	根据文件路径, 读取文件内容, 去除首尾空后返回
	:param file_path: path of file, stored api key
	:return: api key
	"""
	with open(file_path, 'r', encoding=UTF8) as file:
		content = file.read()
	return content.strip()


def official_api_key() -> str:
	return get_api_key(OFFICIAL_API_FILE)


def proxy_api_key() -> str:
	return get_api_key(PROXY_API_FILE)
