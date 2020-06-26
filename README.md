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

## Окно аутентификации: 
Вход уже зарегистрированных пользователей и регистарция при нажатии на `Check in`

![Authentication](https://github.com/Ovsienko023/VTerminale/blob/master/Application-VT/client/QT_GUI/Screen/authentication.png)

## Окно регистрации: 
Регистрация новых пользователей

![Web_registration](https://github.com/Ovsienko023/VTerminale/blob/master/Application-VT/client/QT_GUI/Screen/web_registration.png)

## Окно отправки и просмотра сообщений: 
Для отправки сообщения необходимо: написать сообщение, выбрать адресата в окне `Friends` и нажать кнопку `Send`. ( если окно пусто, перейти во вкладку `Find friends` и добавить в друзья адресата сообщения )

![Send_message](https://github.com/Ovsienko023/VTerminale/blob/master/Application-VT/client/QT_GUI/Screen/Send_message.png)
  

## Окно поиска пользователей: 
Для поиска пользователя нужно ввести его логин в форму `Enter login` нажать кнопку `Find` если пользователь найден в форме `Status` отобразится: `User (name user), found! Add as Friend?`, нажмите `Add friend`
(В случае если пользователя с таким логином нет, в форме `Status` отобразится: `User (name user), not found! Enter the correct login.`)

![Find_friends](https://github.com/Ovsienko023/VTerminale/blob/master/Application-VT/client/QT_GUI/Screen/Find_friends.png)


## Профиль пользователя : 
(находится в доработке) Отражение информации о пользователе.

![My_profile](https://github.com/Ovsienko023/VTerminale/blob/master/Application-VT/client/QT_GUI/Screen/My_profile.png)
 

* Реализация в терминале(консоле): 
  
  В корне проекта, запустить файл: Application-VT/client/net_client.py и следовать инструкциям.