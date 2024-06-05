
import random

def dice():
    result = random.randint(1, 6)
    return result

def janken_hand():
    result = random.choice(["グー","チョキ","パー"]) # random.choice ← ランダムに取り出す文字
    return result
