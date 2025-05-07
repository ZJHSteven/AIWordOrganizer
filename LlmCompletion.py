from litellm import completion

# 模块级别的共享状态字典
state = {}

class Agent:
    def __init__(self, name: str, model: str, description: str, instruction: str, output_key: str | None = None, tools: list = None):
        self.name = name
        self.model_name = model  # model_name is used by litellm.completion
        self.description = description
        self.instruction = instruction
        self.output_key = output_key  # Now optional, defaults to None
        self.tools = tools if tools is not None else []
        self.state = state  # 所有实例共享同一个状态字典

    def execute(self, user_provided_text: str | None = None) -> dict:
        """
        执行 LLM 补全请求，使用预定义的指令和用户提供的文本。
        指令中的占位符会从 self.state 中获取值进行替换。
        如果提供了 output_key，执行结果会以 self.output_key 为键更新到 self.state。

        参数:
            user_provided_text: 用户提供的需要处理的文本。

        返回:
            一个字典，其键为 self.output_key (如果提供的话，否则为 None)，值为 LLM 响应的内容。
        """
        processed_instruction = self.instruction
        for key, value in self.state.items():
            placeholder = f"{{{key}}}"
            processed_instruction = processed_instruction.replace(placeholder, str(value))

        messages = [
            {"role": "system", "content": processed_instruction},
            {"role": "user", "content": user_provided_text}
        ]
        
        response = completion(
            model=self.model_name,
            messages=messages
        )
        
        llm_response_content = "错误：LLM无响应或响应格式意外。"
        if response and response.choices and len(response.choices) > 0:
            message_obj = response.choices[0].message
            if message_obj and hasattr(message_obj, 'content'):
                llm_response_content = message_obj.content
        
        # 仅当 output_key 提供时才更新 state
        if self.output_key is not None:
            self.state[self.output_key] = llm_response_content
        
        return {self.output_key: llm_response_content}
