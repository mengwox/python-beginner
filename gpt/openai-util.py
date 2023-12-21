def getApiKeyFromFile(filePath: str) -> str:
	handler = open(filePath)
	content = ""
	with open(filePath, 'r', encoding='utf-8') as file:
		for line in file.readlines():
			content = content + line.strip() + "\n"
	return content


from unittest import TestCase


class GPTTest(TestCase):
	def test_get_api_key_from_file(self):
		apiKey = getApiKeyFromFile("openai_api_key.txt")
		self.assertIsNotNone(apiKey, "api key shouldn't null")
