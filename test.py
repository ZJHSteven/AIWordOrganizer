from LlmCompletion import Agent
# --- Agent 3 Definition (Root Extractor) ---
agent3_root_extractor = Agent(
    name="roots_extractor_agent",
    model="gemini/gemini-2.0-flash",
    description="从词根分解结果中提取有价值的词根，过滤常见词根，优化输出格式。",
    instruction=(
        "你将接收一个名为 {decomposed_markdown_list} 的Markdown格式字符串，其中包含了单词的词根分析结果。\\n"
        "你的任务是从这些分析中提取出值得背诵的词根，并以新的格式输出。\\n"
        "\\n"
        "请按照以下规则处理：\\n"
        "1. 如果词根与原单词差别较大，保留作为背诵词根\\n"
        "2. 删除常见英语单词作为词根的项（如foot, hand, line等）\\n"
        "3. 保留医学上有特殊意义的词根\\n"
        "\\n"
        "输出格式应为：\\n"
        "1. 原语言词根（如拉丁语或希腊语单词）\\n"
        "   释义：词根含义,来自什么语言\\n"
        "   词根：原词词根\\n"
        "2. [下一个词根]\\n"
        "   ...\\n"
        "\\n"
        "例如，从\"vertebra-\" (椎骨，来自拉丁语\"vertere\"，意思是\"转动\")中提取得到：\\n"
        "1. vertere\\n"
        "   释义：转动\\n"
        "   来自：拉丁语，椎骨\\n"
        "\\n"
        "请确保输出的是纯净的Markdown有序列表。输出不要包含任何代码块标记、前缀或后缀。\\n"
        "如果输入为空或无法提取有价值的词根，请输出\"未找到可用的词根数据。\"。"
    ),

    tools=[],
    output_key="extracted_roots"
)