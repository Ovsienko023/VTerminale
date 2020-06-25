## Kонвертация QT в .py

  1. pip install pyqt5
  2. Создание формы в QT 
  3. Сохранить как file_name.ui
  4. pyuic5 -x file_name.ui -o file_name.py
## In .exe
  pyinstaller .\net_client.py --onefile --noconsole
