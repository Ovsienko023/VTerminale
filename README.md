#  VTerminale__version 2.0 

Api консольного чата для обмена сообщениями по локальной сети с использованием  Mongodb + клиентская часть.

# Для начала работы, необходимо:


1. Установить все зависимости $ pip install -r requirements.txt
2. Запустить сервер базы данных - Mongodb.
3. В файле config.txt записать параметры забуска БД и сервера:

        {
            "server":{"host": "Хост сервера", 
                      "port": "Порт Сервера"}, 
         "Data_Base":{"host":"Хост сервера"
                      "port": "Порт сервера"}
        }


4. Выполнить в терминале команды:
   
        $ make build
        ok
        $ make test
        ok
        $ make run


# Клиентская часть ಠ_ಠ


* Реализация на QT:
  
  В корне проекта, запустить файл: Application-VT/client/QT_GUI/Vterminale.exe

  Сборка файла Vterminale.exe осуществляется с помощью библиотеки pyinstaller, командой: ` pyinstaller .\net_client.py --onefile --noconsole` обзор приложения:

  
  
* Реализация в терминале(консоле): 
  
  В корне проекта, запустить файл: Application-VT/client/net_client.py и следовать инструкциям.