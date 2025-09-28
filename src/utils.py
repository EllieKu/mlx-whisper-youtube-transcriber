import re

def clean_filename(filename: str) -> str:
    """清理檔名，移除不合法字符和 emoji

    Args:
        filename: 原始檔名

    Returns:
        str: 清理後的檔名
    """
    # 移除不合法的檔名字符
    filename = re.sub(r'[<>:"/\\|?*｜]', '', filename)
    # 移除 emoji（Unicode 範圍）
    filename = re.sub(
        r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF'
        r'\U0001F1E0-\U0001F1FF\U00002600-\U000027BF\U0001F900-\U0001F9FF'
        r'\U0001F018-\U0001F270]',
        '',
        filename
    )
    filename = filename.strip()
    return filename
