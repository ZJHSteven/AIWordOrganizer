from litellm import completion

class LlmApiAgent:
    def __init__(self, model_name: str):
        self.model_name = model_name

    def execute(self, messages: list) -> str:
        """
        执行 LLM补全请求。

        参数:
            messages: litellm.completion 所需格式的消息列表。
                      示例: [{"role": "user", "content": "Hello, world!"}]

        返回:
            LLM 响应的内容。
        """
        response = completion(
            model=self.model_name,
            messages=messages
        )
        # 假设响应结构一致且至少有一个选项。
        if response and response.choices and len(response.choices) > 0:
            return response.choices[0].message.content
        else:
            # 处理响应可能为空或格式不符合预期的情况
            return "错误：LLM无响应或响应格式意外。"

# 示例用法 (如果此文件仅用于类定义，则可以删除或注释掉此部分)
if __name__ == "__main__":
    # 如何使用 LlmApiAgent 的示例
    # 请替换为您实际的模型和消息
    agent = LlmApiAgent(model_name="gemini/gemini-2.0-flash") 
    user_messages = [{"role": "user", "content": "编写代码，通过 LiteLLM 说 hi"}]
    result = agent.execute(messages=user_messages)
    print(result)