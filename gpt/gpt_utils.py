import os
import time
import traceback
from datetime import datetime
from typing import List

import httpx
import pytz
from openai import OpenAI
from openai.types.chat import ChatCompletion

from .constants import *
from .gpt_model_enum import *


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"函数 {func.__name__} 的调用耗时 {elapsed_time} 秒。")
        return result

    return wrapper


def completion_top_append_file(
        current_content: str,
        file_path: str | None = HISTORY_PROMPT):
    if not os.path.exists(file_path):
        file = open(file_path, 'w', encoding=UTF8)
        file.write(current_content + '\n')
    else:
        # 将字符串写入文件的最顶端
        file = open(file_path, 'r+', encoding=UTF8)
        original_content = file.read()
        file.seek(0, 0)
        file.write(current_content + '\n' + original_content)


def get_current_time() -> str:
    """
    :return: 获取UTC8的当前系统时间(年-月-日 时:分:秒)
    """
    return datetime.now(pytz.timezone('Asia/Shanghai')) \
        .strftime('%Y-%m-%d %H:%M:%S')


@timing_decorator
def get_deepseek_completion(prompt: str,
                            client: OpenAI | None = None,
                            gpt_model_define: DeepseekModel | None = DeepseekModel.REASONER) \
        -> ChatCompletion:
    """
    invoke openai o1-preview model:
    response longer than 'gpt 4o' and response more correctly may.
    """
    if client is None:
        client = official_client()
    # o1 API使用方式, o1暂只支持role为user/assistant
    completion = client.chat.completions.create(
        model=get_model_name(gpt_model_define),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT_CHINESE},
            {"role": "system", "content": SYSTEM_PROMPT_FORMAT},
            {"role": "user", "content": prompt}
        ]
    )
    return completion

@timing_decorator
def get_o1_chat_completion(prompt: str,
                           client: OpenAI | None = None,
                           gpt_model_define: GptModelDefines | None = GptModelDefines.O1_LATEST) \
        -> ChatCompletion:
    """
    invoke openai o1-preview model:
    response longer than 'gpt 4o' and response more correctly may.
    """
    if client is None:
        client = official_client()
    # o1 API使用方式, o1暂只支持role为user/assistant
    completion = client.chat.completions.create(
        model=get_model_name(gpt_model_define),
        messages=[
            {"role": "assistant", "content": SYSTEM_PROMPT_CHINESE},
            {"role": "assistant", "content": SYSTEM_PROMPT_FORMAT},
            {"role": "user", "content": prompt}
        ]
    )
    return completion


@timing_decorator
def get_chat_completion(prompt: str,
                        client: OpenAI | None = None,
                        gpt_model_define: GptModelDefines | None = GptModelDefines.GPT4_O) \
        -> ChatCompletion:
    """
    get GPT Response Chat Completion
    :param prompt: user prompt; Required
    :param client: OpenAI;
        Optional, Default is Official Client
    :param gpt_model_define:
        GptModelDefines Enum; Optional,	Default is 'gpt-4-turbo'
    :return: `openai.resources.chat.Completions`
    """
    if client is None:
        client = official_client()
    # gpt 4o相关使用方式
    completion = client.chat.completions.create(
        model=get_model_name(gpt_model_define),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT_CHINESE},
            {"role": "system", "content": SYSTEM_PROMPT_FORMAT},
            {"role": "user", "content": prompt}
        ]
    )
    return completion


def get_file_content(file_path: str) -> str:
    """
    Read the file's content and strip it based on the provided file path.

    :param file_path: path of file, stored
    :return: api key
    """
    try:
        with open(file_path, 'r', encoding=UTF8) as file:
            content = file.read()
        return content.strip()
    except FileNotFoundError:
        traceback.print_exc()
        print("file not found!please check file path: %s" % file_path)


def official_api_key() -> str:
    return get_file_content(OFFICIAL_API_FILE)


def proxy_api_key() -> str:
    return get_file_content(PROXY_API_FILE)


def get_model_name(model_enum) -> str:
    return model_enum.value


def timeout_config() -> httpx.Timeout:
    return httpx.Timeout(600, connect=120)


def official_client():
    return OpenAI(
        timeout=timeout_config(),
        max_retries=0,
        api_key=official_api_key())


def client_deepseek():
    """
    Deepseek API使用
    """
    return OpenAI(
        base_url='https://api.deepseek.com/v1',
        timeout=timeout_config(),
        max_retries=0,
        api_key=get_file_content(Deepseek_API_FILE))


def official_safe_client():
    return OpenAI(
        timeout=timeout_config(),
        max_retries=0,
        base_url=get_file_content(OFFICIAL_SAFE_URL) + '/v1',
        api_key=official_api_key())


def proxy_client():
    """使用Aihubmix代理,访问各AI大模型"""
    return OpenAI(
        timeout=timeout_config(),
        max_retries=0,
        api_key=get_file_content(PROXY_API_FILE),
        base_url=get_file_content(PROXY_URL) + '/v1')


def get_model_list() -> List[str]:
    """
    :return: list of model names
    """
    client = official_client()
    models = client.models.list()
    model_names = list()
    for model in models:
        model_names.append(model.id)
    model_names.sort()
    return model_names
