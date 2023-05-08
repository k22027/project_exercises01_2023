import os
import re

directory = './img'  # ファイルを変換したいディレクトリのパス
old_pattern = '5_'  # 変換前の文字列を正規表現で指定
new_string = '1_'  # 変換後の文字列

# ディレクトリ内のファイルを列挙し、変換を行う
for filename in os.listdir(directory):
    new_filename = re.sub(old_pattern, new_string, filename)
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))



