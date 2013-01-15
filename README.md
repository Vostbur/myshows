Android-клиент сервиса слежения за выходом новых эпизодов сериалов.
===================================================================

**Приложение информирует о ближайших пяти новых эпизодов сериалов на которые вы подписаны на сайте [myshows.ru]**

![ALT Screenshoot](http://1.bp.blogspot.com/-CLIq9lIdYjU/T52p_lNbYJI/AAAAAAAALRQ/oYOnfkgTQuc/s1600/ArrRP3gCAAAN5U-.png)

Требования:
-----------
- [Android SDK]
- [SL4A]
- [Python for Android]

Для Windows:
------------
- После установки Andriod SDK в Windows XP в папку по умолчанию копированием перенес каталог android-sdk в корень C:\, затем создал системную переменную ANDROID_SDK_HOME со значением C:\, SDK и эмулятор андроида не работают с путями содержащими пробелы и символы отличные от латиницы.
- Вызов скрипта adb: *C:\android-sdk>platform-tools\adb.exe push myshows.py /sdcard/sl4a/scripts*

Будут полезны:
--------------
- [Разработка приложения для Anroid на Python]

[myshows.ru]: http://myshows.ru/
[Android SDK]: http://lexpr.ru/python_for_android
[SL4A]: http://code.google.com/p/android-scripting/
[Python for Android]: http://code.google.com/p/android-scripting/downloads/detail?name=PythonForAndroid_r4.apk
 [Разработка приложения для Anroid на Python]: http://lexpr.ru/python_for_android
