
# 練習プログラム3 コマンドライン引数で指定したファイルを開く (1.5点)

"""
- コマンドライン引数で指定されたファイルパスからファイルを読み込んで出力するプログラム作成しましょう。
"""

import sys
arglist = sys.argv    # コマンドライン引数を受け取る
print(arglist)    # そのまま出力する

file_path = arglist[1]  # "./data/asitaka.txt" 等を指定する
with open(file_path, "r", encoding="utf_8") as fileobj: # ファイルオブジェクトを作る
    while True:
        line = fileobj.readline()    # 1行ずつ読み込む
        aline = line.rstrip()    # 改行を取り除く
        if aline :    # 文字列があれば出力する
            print(aline) 
        else:
            break    # 読み込みを終了する