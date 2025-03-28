from gpt.gpt_utils import *


def gpt_completion():
    # 提示词
    prompt = get_file_content(PROMPT_FILE)
    # 客户端
    # client = proxy_client()
    client = official_client()
    # client = client_deepseek()
    # client = official_safe_client()
    # 所用模型
    model = GptModelDefines.O1_LATEST

    # 获取gpt api completion, 打印内容并写入文件
    completion = get_o1_chat_completion(prompt, client, model)
    resp_cont = completion.choices[0].message.content
    current_time = get_current_time()
    usage_count = completion.usage
    # 构建要写入文件的字符串
    formatted_string = f"""
{current_time}

***Me :***

# {prompt}

***ChatGpt {completion.model}:***

{resp_cont}

total tokens: {usage_count.total_tokens}, input tokens: {usage_count.prompt_tokens}, 
output tokens: {usage_count.completion_tokens}

---
"""
    print('\n' + formatted_string)
    # 对话写入文件
    completion_top_append_file(formatted_string)


if __name__ == '__main__':
    gpt_completion()
