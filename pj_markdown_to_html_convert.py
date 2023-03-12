"""
Markdown to html convert

[本プログラムの説明]
マークダウンを HTML に変換するプログラムです。
markdown は実行するコマンド、inputfile は .md ファイルへのパス、出力パスはプログラムを実行した後に作成される .html です。

下記、コマンドのように入力をして実行します。
例：python3 file-converter.py markdown inputfile outputfile

詳細は、各関数のコメントに記載してます。
"""

import sys


def markdown_to_html_convert(md_file):
    return None


def main(argv):
    markdown_to_html_convert(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
