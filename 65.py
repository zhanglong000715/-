import time

def talk(text):
    print(f"""
          ╭{'─' * (len(text) + 2)}╮
          ┃  {text}  ┃
          ╰{'─' * (len(text) + 2)}╯
        ／⌒ヽ
      （｡•ᴗ•｡）
       /　　 \
    """)

# 模拟对话
while True:
    talk(input('：'))
    time.sleep(1)