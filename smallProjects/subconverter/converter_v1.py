import re

def vtt_to_srt(vtt_file, srt_file):
    with open(vtt_file, 'r', encoding='utf-8') as vtt, open(srt_file, 'w', encoding='utf-8') as srt:
        content = vtt.read()

        # 使用正则表达式将时间标记格式从00:00:00.000 转换为 00:00:00,000
        content = re.sub(r'(\d{2}:\d{2}:\d{2})\.(\d{3})', r'\1,\2', content)

        # 使用正则表达式删除VTT格式中的标签
        content = re.sub(r'Kind:.*\n', '', content)
        content = re.sub(r'Language:.*\n', '', content)

        # 分割字幕条目
        entries = content.split('\n\n')

        # 写入SRT文件
        for index, entry in enumerate(entries, start=1):
            srt.write(f"{index}\n")
            # 两行合并成一行，并添加空格
            entry = re.sub(r'(.*\n.*)\n(.*)', r'\1 \2', entry)
            srt.write(entry + '\n')

if __name__ == '__main__':
    vtt_file = 'Andrew Ng： Opportunities in AI - 2023.vtt'  # 替换为输入VTT文件的文件名
    srt_file = 'output.srt'  # 替换为输出SRT文件的文件名

    vtt_to_srt(vtt_file, srt_file)
    print(f"VTT文件 '{vtt_file}' 已成功转换为SRT文件 '{srt_file}'")
