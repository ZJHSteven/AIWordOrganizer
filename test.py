import re
import pandas as pd
import os

sample_state = {
    'decomposed_markdown_list': '1. Humerus\n   释义：肱骨\n   词根：“humer-” (肩，臂，来自拉丁语“humerus”)\n   后缀：“-us” (名词后缀)\n2. Ankle\n   释义：踝\n   词源：日耳曼语词根，与弯曲相关，中古英语"ankel"\n3. Vertebrae\n   释义：椎骨\n   词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n   后缀：“-ae” (名词复数后缀)\n4. vertebral body\n   释义：椎体\n   词根：“vertebra-” (椎骨， 来自拉丁语“vertere”，表示转动)\n   后缀：“-al” (形容词后缀)\n   词：“body” (身体)\n5. vertebral foramen\n   释义：椎孔\n   词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n   后缀：“-al” (形容词后缀)\n   词根：“foramen-” (孔，来自拉丁语“forare”，表示钻孔)\n6. vertebral canal\n   释义：椎管\n   词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n   后缀：“-al” (形容词后缀)\n   词：“canal” (管道)\n7. vertebral arch\n   释义：椎弓\n   词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n   后缀：“-al” (形容词后缀)\n   词：“arch” (弓形)\n8. pedicle of vertebral arch\n   释义：椎弓根\n   词根：“ped-” (脚，足，茎，来自拉丁语“pes”)\n   后缀：“-icle” (小词后缀)\n   介词：“of”\n   词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n   后缀：“-al” (形容词后缀)\n   词：“arch” (弓形)\n9. superior vertebral notch\n   释义：椎上切迹\n   词根：“super-” (之上，超过，来自拉丁语“super”)\n    后缀：“-ior” (形容词比较级后缀)\n   词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n   后缀 ：“-al” (形容词后缀)\n   词：“notch” (切口)\n10. inferior vertebral notch\n    释义：椎下切迹\n    词根：“infer-” (之下，低于，来自拉丁语“inferus”)\n    后缀：“-ior” (形容词比较级后缀)\n    词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n    后缀：“-al” (形容词后缀)\n    词：“notch” (切口)\n11. inter vertebral foramina\n    释义：椎间孔\n    词根：“inter-” (之间，在……之间，来自拉丁语“inter”)\n    词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n    后缀：“-al” (形容词后缀)\n    词根 ：“foramen-” (孔，来自拉丁语“forare”，表示钻孔)\n    后缀："-a" (复数)\n12. spinous process\n    释义：棘突\n    词根：“spin-” (刺，棘，来自拉丁语“spina”)\n    后缀：“-ous” (形容词后缀)\n    词：“process” (突起)\n13. transverse process\n    释义：横突\n    词根：“trans-” (横跨，穿过，来自拉丁语“trans”)\n    词根：“verse-” (转动，来自拉丁语“vertere”)\n    后缀：“-al” (形容词后缀)\n    词：“process” (突起)\n14. articular process\n    释义：关节突\n    词根：“articul-” (关节，来自拉丁语“articulus”)\n    后缀：“-ar” (形容词后缀)\n    词：“process” (突起)\n15. cervical vertebrae\n    释义：颈椎\n    词根：“cervic-” (颈，来自拉丁语“cervix”)\n    后缀：“-al” (形容词后缀)\n    词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n    后缀：“-ae” (名词复数后缀)\n16. uncus of vertebral body\n    释义：椎体钩\n    词根：“unc-” (钩，弯曲，来自拉丁语“uncus”)\n    介词：“of”\n    词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n    后缀：“-al” (形容词后缀)\n    词：“body” (身体)\n\n17. uncovertebral joint\n    释义：钩椎关节\n    词根：“unc-” (钩，弯曲，来自拉丁语“uncus”)\n    词根：“vertebra-” ( 椎骨，来自拉丁语“vertere”，表示转动)\n    后缀：“-al” (形容词后缀)\n    词：“joint” (关节)\n\n18. transverse foramen\n    释义：横突孔\n    词根：“trans-” (横跨，穿过，来自拉丁语“trans”)\n    词根：“verse-” (转动，来自拉丁语“vertere”)\n    后缀：“-al” (形容词后缀)\n    词根：“foramen-” (孔，来自拉丁语“forare”，表示钻孔)\n\n19. tubercle\n    释义：颈动脉结节\n    词根: “tuber-” (肿块，隆起，来自拉丁语“tuber”)\n    后缀: “-cle” (小词后缀，表示小肿块)\n\n20. atlas\n    释义：寰椎\n    来源：希腊神话中的擎天神阿特拉斯(Atlas)，因寰椎支撑头部，故名。\n\n21. axis\n    释义：枢椎\n    词根：“axi-” (轴，来自拉丁语“axis”)\n\n22. vertebra prominens\n    释义：隆椎\n    词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n    词根：“promin-” (突出，来自拉丁语“prominere”)\n    后缀：“-ens” (现在分词后缀)\n\n23. thoracic vertebrae\n    释义：胸椎\n    词根：“thorac-” (胸，来自希腊语“thorax”)\n    后缀：“-ic” (形容词后缀)\n    词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n    后缀：“-ae” (名词复数后缀)\n\n24. lumbar vertebrae\n    释义：腰椎\n    词根：“lumb-” (腰，来自拉丁语“lumbus”)\n    后缀：“-ar” (形容词后缀)\n    词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n    后缀：“-ae” ( 名词复数后缀)\n\n25. sacrum, sacral bone\n    释义：骶骨\n    词根：“sacr-” (神圣的，来自拉丁语“sacer”，在解剖学中指骨盆下部的骨头)\n    后缀：“-um” (名词后缀) or "-al"(形容词)\n    词: "bone" (骨头)\n\n26. promontory\n    释义：岬\n    词根：“promont-” (突出，延伸，来自拉丁语“promontorium”)\n    后缀 ：“-ory” (表示地点或事物的后缀)\n\n27. sacral hiatus\n    释义：骶管裂孔\n    词根：“sacr-” (神圣的，来自拉丁语“sacer”，在解剖学中指骨盆下部的骨头)\n    后缀：“-al” (形容词后缀)\n    词根：“hiat-” (张开，裂开，来自拉丁语“hiatus”)\n\n28. sacral cornu\n    释义：骶角\n    词根：“sacr-” (神圣的，来自拉丁 语“sacer”，在解剖学中指骨盆下部的骨头)\n    后缀：“-al” (形容词后缀)\n    词根：“corn-” (角，来自拉丁语“cornu”)\n    后缀：“-u” (拉丁语名词单数第四格后缀)\n\n29. coccyx\n    释义：尾骨\n    词根：“coccy-” (布谷鸟的喙，来自希腊语“kokkyx”，因形状相似而得名)\n\n30. sternum\n    释义：胸骨\n    词根：“stern-” (胸，胸骨，来自希腊语“sternon”)\n\n31. manubrium sterni\n    释义：胸骨柄\n    词根：“manubri-” (柄，把手，来自拉丁语“manubrium”)\n    介词：“sterni” (胸骨的所有格)\n\n32. jugular notch\n    释义： 颈静脉切迹\n    词根：“jugul-” (颈，喉咙，来自拉丁语“jugulum”)\n    后缀：“-ar” (形容词后缀)\n    词 ：“notch” (切口)\n\n33. sternal angle\n    释义：胸骨角\n    词根：“stern-” (胸，胸骨，来自希腊语“sternon”)\n    后缀：“-al” (形容词后缀)\n    词：“angle” (角)\n\n34. body of sternum\n    释义：胸骨体\n    词：“body” (身体)\n    介词：“of”\n    词根：“stern-” (胸，胸骨，来自希腊语“sternon”)\n\n35. xiphoid process\n    释义：剑突\n    词根：“xiph-” (剑，来自希腊语“xiphos”)\n    后缀：“-oid” (像……的)\n    词：“process” (突起)\n\n36. rib\n    释义：肋\n    词源：古英语"rib"，表示构成胸腔的弯曲骨头。\n\n37. costal arch\n    释义：肋弓\n    词根：“cost-” (肋，来自拉丁语“costa”)\n    后缀：“-al” (形容词后缀)\n    词：“arch” (弓形)\n\n38. costal bone\n    释义：肋骨\n    词根：“cost-” (肋，来自拉丁语“costa”)\n    后缀：“-al” (形容词后缀)\n    词：“bone” (骨头)\n\n39. costal head\n    释义：肋头\n    词根：“cost-” (肋，来自拉丁语“costa”)\n    后缀：“-al” (形容词后缀)\n    词：“head” (头)\n\n40. costal neck\n    释义：肋颈\n    词根：“cost-” (肋，来自拉丁语“costa”)\n    后缀：“-al” (形容词后缀)\n    词：“neck” (颈)\n\n41. costal tubercle\n    释义：肋结节\n    词根：“cost-” (肋，来自拉丁语“costa”)\n    后缀：“-al” (形容词后缀)\n    词根: “tuber-” (肿块，隆起，来自拉丁语“tuber”)\n    后缀: “-cle” (小词 后缀，表示小肿块)\n\n42. shaft of rib\n    释义：肋体\n    词: “shaft” (柄，杆)\n    介词：“of”\n    词：“rib” (肋)\n\n43. costal groove\n    释义：肋沟\n    词根：“cost-” (肋，来自拉丁语“costa”)\n     后缀：“-al” (形容词后缀)\n    词：“groove” (沟槽)\n\n44. costal angle\n    释义：肋角\n    词根：“cost-” (肋，来自拉丁语“costa”)\n    后缀：“-al” (形容词后缀)\n    词：“angle” (角)\n\n45. costal cartilage\n    释义：肋软骨\n    词根：“cost-” (肋，来自拉丁语“costa”)\n    后缀：“-al” (形容词后缀)\n    词根：“cartilag-” (软骨，来自拉丁语“cartilago”)\n    后缀：“-e” (名词后缀)\n\n46. skull\n    释义：颅\n    词源：古诺斯语 "skalli"，表示头盖骨。\n\n47. calvaria\n    释义：颅盖\n    词根：“calvar-” (秃头 ，头盖骨，来自拉丁语“calvaria”)\n    后缀：“-ia” (名词后缀)\n\n48. frontal bone\n    释义：额骨\n    词根：“front-” (前，额头，来自拉丁语“frons”)\n    后缀：“-al” (形容词后缀)\n    词：“bone” (骨头)\n\n49. ethmoid bone\n    释义：筛骨\n    词根：“ethmo-” (筛子，来自希腊语“ethmos”)\n    后缀：“-oid” (像……的)\n    词：“bone” (骨头)\n\n50. sphenoid bone\n    释义：蝶骨\n    词根：“sphen-” (楔子，来自希腊语“sphen”)\n    后缀：“-oid” (像……的)\n    词：“bone” (骨头)\n\n51. vertebral column\n    释义：脊柱\n    词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n    后缀：“-al” (形容词后缀)\n    词：“column” (柱)\n\n52. intervertebral disc\n    释义：椎间盘\n    词根：“inter-” (之间，在……之间，来自拉丁语“inter”)\n    词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n    后缀：“-al” (形容词后 缀)\n    词：“disc” (盘)\n\n53. nucleus pulposus\n    释义：髓核\n    词根：“nucle-” (核，核心，来自 拉丁语“nucleus”)\n    后缀：“-us” (名词后缀)\n    词根：“pulpos-” (髓，果肉，来自拉丁语“pulpa”)\n    后缀：“-us” (形容词后缀)\n\n54. anulus fibrosus\n    释义：纤维环\n    词根：“anul-” (环，来自拉丁语“anulus”)\n    后缀：“-us” (名词后缀)\n    词根：“fibros-” (纤维的，来自拉丁语“fibra”)\n    后缀：“-us” (形容词后缀)\n\n55. anterior longitudinal ligament\n    释义：前纵韧带\n    词根：“anter-” (前，来 自拉丁语“ante”)\n    后缀：“-ior” (形容词比较级后缀)\n    词根：“longitud-” (长度，来自拉丁语“longitudo”)\n    后缀：“-al” (形容词后缀)\n    词：“ligament” (韧带)\n\n56. posterior longitudinal ligament\n    释义：后纵韧带\n    词根：“poster-” (后，来自拉丁语“posterior”)\n    后缀：“-ior” (形容词比较级 后缀)\n    词根：“longitud-” (长度，来自拉丁语“longitudo”)\n    后缀：“-al” (形容词后缀)\n    词：“ligament” (韧带)\n\n57. ligamenta flava\n    释义：黄韧带\n     词根：“ligament-” (韧带，来自拉丁语“ligamentum”)\n     后缀：“-a” (复数形式)\n     词根：“flav-” (黄色，来自拉丁语“flavus”)\n     后缀：“-a” (复数形式)\n\n58. interspinal ligament\n    释义：棘间韧带\n    词根：“inter-” (之间，在……之间，来自拉丁语“inter”)\n    词根：“spin-” (刺，棘，来自拉丁语“spina”)\n    后缀：“-al” (形容词后缀)\n    词：“ligament” (韧带)\n\n59. supraspinal ligament\n    释义：棘上韧带\n    词根：“supra-” (之上，超过，来自拉丁语“supra”)\n    词根：“spin-” (刺，棘，来自拉丁语“spina”)\n    后缀：“-al” (形容词后缀)\n    词：“ligament” (韧带)\n\n60. ligamentum nuchae\n    释义：项韧带\n    词根：“ligament-” (韧带，来自拉丁语“ligamentum”)\n    后缀：“-um” (名词后缀)\n    词：“nuchae” (拉丁语，项部的)\n\n61. intertransverse ligament\n    释义：横突间韧带\n    词根：“inter-” (之间，在……之间，来自拉丁语“inter”)\n    词根：“trans-” (横跨，穿过，来自拉丁语“trans”)\n    词根：“verse-” (转动，来自拉丁语“vertere”)\n    后缀：“-al” (形容词后缀)\n    词：“ligament” (韧带)\n\n62. zygapophysial joint\n    释义：关节突关节\n    词根：“zygo-” (连接，结合，来自希腊语“zygon”)\n    词根：“apophys-” (突起，来自希腊语“apophysis”)\n    后缀：“-ial” (形容词后缀)\n    词：“joint” (关节)\n\n63. atlantooccipital joint\n    释义：寰枕关节\n    词：“atlanto-” (寰椎的，连接词)\n    词根：“occipit-” (后脑勺，来自拉丁语“occiput”)\n    后缀：“-al” (形容词后缀)\n    词：“joint” (关节)\n\n64. atlantoaxial joint\n    释义：寰枢关节\n    词：“atlanto-” (寰椎的，连接词)\n    词：“axial” (枢椎的)\n    词：“joint” (关节)\n\n65. costovertebral joint\n    释义：肋椎关节\n    词根：“costo-” (肋的，连接词)\n    词根：“vertebra-” (椎骨，来自拉丁语“vertere”，表示转动)\n    后缀：“-al” (形容词后缀)\n    词：“joint” (关节)\n\n66. joint of costal head\n     释义：肋头关节\n    词：“joint” (关节)\n    介词：“of”\n    词根：“cost-” (肋，来自拉丁语“costa”)\n    后缀：“-al” (形容词后缀)\n    词：“head” (头)\n\n67. costotransverse joint\n    释义：肋横突关节\n    词根：“costo-” (肋的，连接词)\n    词根：“trans-” (横跨，穿过，来自拉丁语“trans”)\n    词根：“verse-” (转动，来自拉丁语“vertere”)\n    后缀：“-al” (形容词后缀)\n    词：“joint” (关节)\n\n68. sternocostal joint\n    释义：胸肋关节\n    词根：“sterno-” (胸骨的，连接词)\n    词根：“cost-” (肋，来自拉丁语“costa”)\n    后缀：“-al” (形容词后缀)\n    词：“joint” (关节)\n\n69. thorax\n    释义：胸廓\n     词根：“thorax-” (胸，来自希腊语“thorax”)\n\n70. temporomandibular joint\n    释义：颞下颌关节\n    词根：“temporo-” (颞的, 来自拉丁语“tempus”)\n    词根：“mandibul-” (下颌骨的, 来自拉丁语“mandibula”)\n    后缀：“-ar” (形容词后缀)\n    词：“joint” (关节)'
}

# 1. 提取 Markdown 字符串
markdown_text = sample_state.get('decomposed_markdown_list', '')

# 如果存在 Markdown 代码块标记，则移除
if markdown_text.startswith("```markdown\n"):
    markdown_text = markdown_text[len("```markdown\n"):]
if markdown_text.endswith("\n```"):
    markdown_text = markdown_text[:-len("\n```")]
markdown_text = markdown_text.strip() # 移除首尾可能存在的空白

# 2. 定义正则表达式
# 匹配 "数字. 单词\n" 和随后的 "   释义：... (直到下一个 "数字." 或字符串末尾)"
# (?s) 使 . 可以匹配换行符
# (\d+\.\s+.*?)\n  匹配 "数字. 单词" 这一行，捕获单词
# (\s{3}释义：.*?)(?=\n\d+\.\s+|\Z) 匹配 "   释义：" 开始的详细内容，直到下一个条目或字符串末尾
regex = r"(\d+\.\s*(.*?)\n)(\s{3}释义：.*?)(?=\n\d+\.\s*|\Z)"

parsed_data = []
if markdown_text:
    matches = re.finditer(regex, markdown_text, re.DOTALL)
    for match in matches:
        english_word = match.group(2).strip()
        # 移除开头的 "   " 和 "释义："，并去除首尾空格
        chinese_definition_and_roots = match.group(3).strip()
        if chinese_definition_and_roots.startswith("释义："):
             chinese_definition_and_roots = chinese_definition_and_roots[len("释义："):].strip()
        else: # 兼容可能没有严格 "   释义：" 开头的情况，直接取捕获组内容
            chinese_definition_and_roots = match.group(3).replace("释义：", "", 1).strip()

        parsed_data.append({
            "英文": english_word,
            "中文": chinese_definition_and_roots
        })

# 3. 准备 Excel 文件路径和表头
excel_file_name = "test_output.xlsx"  # 测试文件名
# target_excel_path = "d:\Workspace\Stable\Python\ReWordOrganizer\词根整理.xlsx" # 实际文件路径（注释掉供测试）
excel_column_english = "英文"
excel_column_chinese = "中文"
excel_column_tag = "标签"

# 4. 读取现有 Excel (如果存在) 并进行去重
existing_df = pd.DataFrame(columns=[excel_column_english, excel_column_chinese, excel_column_tag])
if os.path.exists(excel_file_name):
    try:
        existing_df = pd.read_excel(excel_file_name)
        # 确保列名是字符串类型，以防读取的是数字等
        existing_df.columns = existing_df.columns.astype(str)
    except Exception as e:
        print(f"读取 Excel 文件 '{excel_file_name}' 失败: {e}")
        # 如果读取失败，当作空 DataFrame 处理，避免后续操作出错

# 获取已存在的英文单词列表（转换为小写以便不区分大小写比较）
existing_english_words = set()
if excel_column_english in existing_df.columns:
    existing_english_words = set(existing_df[excel_column_english].astype(str).str.lower())

# 5. 筛选需要添加的新数据 (去重)
new_data_to_add = []
for item in parsed_data:
    if item["英文"].lower() not in existing_english_words:
        new_data_to_add.append(item)
        existing_english_words.add(item["英文"].lower()) # 将新添加的词也加入，防止本次解析内容内部重复

# 6. 如果有新数据，则创建 DataFrame 并添加标签列
if new_data_to_add:
    new_df = pd.DataFrame(new_data_to_add)
    new_df[excel_column_tag] = "系统解剖学"  # 添加标签

    # 7. 合并新旧数据并写入 Excel
    # combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    # 为了确保列的顺序和存在性，我们基于预期的列来构建最终的 DataFrame
    # 首先，确保 existing_df 包含所有必要的列
    for col in [excel_column_english, excel_column_chinese, excel_column_tag]:
        if col not in existing_df.columns:
            existing_df[col] = None # 或者 pd.NA
    
    # 合并时，如果 new_df 也有这些列，它们会被正确对齐
    # 如果 existing_df 为空，concat 的结果就是 new_df (带有正确的列)
    if not existing_df.empty:
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    else: # 如果 existing_df 是空的 (比如文件不存在或读取失败或文件本身为空)
        combined_df = new_df
    
    # 重新排序列，确保 "英文", "中文", "标签" 的顺序
    final_columns = [excel_column_english, excel_column_chinese, excel_column_tag]
    # 添加 existing_df 中可能存在的其他列，以防丢失
    for col in existing_df.columns:
        if col not in final_columns:
            final_columns.append(col)
    combined_df = combined_df.reindex(columns=final_columns)

    try:
        combined_df.to_excel(excel_file_name, index=False)
        print(f"数据已成功写入/追加到 '{excel_file_name}'")
        if new_data_to_add:
            print("新添加的单词：")
            for item in new_data_to_add:
                print(f"- {item['英文']}")
        else:
            print("没有新的不重复单词需要添加。")
    except Exception as e:
        print(f"写入 Excel 文件 '{excel_file_name}' 失败: {e}")
elif parsed_data: # 有解析到的数据，但都是重复的
    print("所有解析到的单词已存在于 Excel 文件中，无需添加。")
else: # 没有解析到任何数据
    print("从 Markdown 文本中没有解析到任何数据。")

