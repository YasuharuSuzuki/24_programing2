
# 17. Pythonモジュールの作成(0.5点)

"""
- 沖縄県のワクチン接種データを扱うPythonモジュール「okinawa_vaccination.py」を作成してください。
- 作成するPythonモジュールには、日付を複数指定したら沖縄県のワクチン接種数の合計を返すユーザー定義関数を作成してください。
  - 関数名はgetTotalVaccinationsForDates()としてください
"""

# 定数定義
OKINAWA_VACCINATION_PATH = "./data/okinawa_vaccination.txt"

def getTotalVaccinationsForDates(dates):
    total_count = 0
    with open(OKINAWA_VACCINATION_PATH, mode="r", encoding="utf_8") as f:
        okinawa_vaccinations = f.readlines()
        for okinawa_vaccination1 in okinawa_vaccinations:
            date, count = okinawa_vaccination1.split()
            if date in dates:
              total_count += int(count)
    
    return total_count
