from LlmCompletion import Agent # 从 LlmCompletion.py 导入 LlmApiAgent 类

# 创建 LlmApiAgent 实例，传入模型名称
# 您可以根据需要更改模型名称

agent1_extractor = Agent(
    name="english_chinese_pair_extractor_agent",
    model="gemini/gemini-2.0-flash",
    description="从系统解剖学文本中提取英文术语和对应的中文含义，并以 Markdown 有序列表格式输出。",
    instruction=(
        "你的任务是从用户提供的【系统解剖学】相关文本中，提取出成对的中文术语及其对应的英文单词。 "
        "文本的格式可能多样，例如 '中文术语 English Word'，或者混合在段落中。 "
        "请仔细阅读文本，找出所有这样的配对。 "
        "最终，你必须只输出一个 Markdown 格式的有序列表，其中每一项都是中文术语和括号括起来的英文单词。 "
        "绝对不要包含任何额外的解释性文字、Markdown 代码块标记（例如 \\`\\`\\`）或其他任何前缀或后缀。 "
        "输出格式范例如下：\\n"
        "1. 肱骨 (Humerus)\\n"
        "2. 踝 (Ankle)\\n"
        "如果找不到任何配对，请输出一个空字符串或提示信息，例如“未找到可提取的术语。”。"
    ),
    tools=[],
    output_key="extracted_pairs"
)


# --- Agent 2 Definition (Decomposer) ---
agent2_decomposer = Agent(
    name="word_decomposer_agent",
    model="gemini/gemini-2.0-flash",
    description="接收英汉词对字典，对英文单词进行词根拆解，并以 Markdown 有序列表格式化输出。",
    instruction=(
        "你将接收一个名为 {extracted_pairs} 的 Python 字典作为输入，其中键是英文单词，值是对应的中文释义。\\n"
        "你的任务是：对于字典中的每一个英文单词，进行详细的词根、词缀分析，并结合其原始的中文释义。\\n"
        "最终，你必须只输出一个 Markdown 格式的有序列表。列表中的每一项代表一个单词的分析结果。\\n"
        "每一项的格式如下，请严格遵守（注意换行和缩进）：\\n"
        "1. EnglishWord\\n"
        "   释义：中文意思\\n"
        "   词根：“root1-” (来源和含义)\\n"
        "   词根：“root2-” (来源和含义)\\n"
        "   后缀：“-suffix” (来源和含义)\\n"
        "\\n"
        "输出格式范例如下，假设输入为 `{\\'pilosebaceous\\': \\'毛囊皮脂腺的\\', \\'cardiopathy\\': \\'心脏病\\'}`：\\n"
        "1. pilosebaceous\\n"
        "   释义：毛囊皮脂腺的\\n"
        "   词根：“pilo-” (毛发，来自拉丁语“pilus”)\\n"
        "   词根：“sebace-” (皮脂的，来自拉丁语“sebaceus”)\\n"
        "   后缀：“-ous” (形容词后缀，表示“具有……的”)\\n"
        "2. cardiopathy\\n"
        "   释义：心脏病\\n"
        "   词根：“cardio-” (心脏，来自希腊语“kardia”)\\n"
        "   词根：“-pathy” (疾病，来自希腊语“pathos”)\\n"
        "\\n"
        "请确保输出的是纯净的 Markdown 有序列表，绝对不要包含任何额外的解释性文字、Markdown 代码块标记（例如 \\`\\`\\`）或其他任何前缀或后缀。\\n"
        "如果输入的字典为空，请输出一个空字符串或提示信息，例如“没有可供分析的单词。”。"
    ),
    tools=[],
    output_key="decomposed_markdown_list"  # Updated output_key
)

# 执行代理并获取结果
result1 = agent1_extractor.execute(user_provided_text=input("请输入文本："))
print(result1)
result2 = agent2_decomposer.execute(user_provided_text=input("请输入文本："))

# 打印结果
print(result2)
