#!/usr/bin/python3

import os
import re
import subprocess
import sys

import openai
from openai import OpenAI

OS_TYPE = "MacOS"
TERMINAL_TYPE = "Bash"
API_BASE = "https://api.lingyiwanwu.com/v1"
API_KEY = "YOUR API KEY"

# Set up your OpenAI API key
client = OpenAI(
    api_key=API_KEY,
    base_url=API_BASE
)


def get_chatgpt_response(prompt):
    completion = client.chat.completions.create(
        model="yi-large-turbo",
        messages=[
            {"role": "system",
             "content": f"请根据问题回答如何使用终端命令来完成对应的工作,我的操作系统是{OS_TYPE}终端是{TERMINAL_TYPE},终端命令使用markdown code block包裹,每次仅输出一个最合适的脚本。"},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content.strip()


def extract_code_block(text):
    pattern = r"```bash\n(.*?)\n```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ? <prompt>")
        sys.exit(1)

    user_input = " ".join(sys.argv[1:])
    query = f"当前我打开了终端,我的问题是: {user_input}. 请告诉我如何使用脚本完成这个问题."

    response = get_chatgpt_response(query)
    print(response)

    shell_cmd = extract_code_block(response)
    if shell_cmd:
        # TODO 多个脚本命令不应该能够执行
        user_input = input("检测到了脚本命令. 执行(r) 或者 编辑(e) 或者 退出(q): ")
        if user_input.lower() == 'r':
            subprocess.run(shell_cmd, shell=True)
        elif user_input.lower() == 'e':
            os.system(f"echo '{shell_cmd}' | pbcopy")
            print("脚本已经复制到剪贴板.")
        else:
            print("退出.")
