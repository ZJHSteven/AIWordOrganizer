from LlmCompletion import LlmApiAgent # 从 LlmCompletion.py 导入 LlmApiAgent 类

# 创建 LlmApiAgent 实例，传入模型名称
# 您可以根据需要更改模型名称
agent = LlmApiAgent(model_name="gemini/gemini-2.0-flash")

# 定义要发送给模型的用户消息
user_messages = [{"role": "user", "content": "编写代码，通过 LiteLLM 说 hi"}]

# 执行代理并获取结果
result = agent.execute(messages=user_messages)

# 打印结果
print(result)