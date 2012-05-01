# coding: utf-8

import android
import hashlib
import urllib2 as ul2
import json as j
import time as t

app = android.Android()

app.vibrate()

login = app.dialogGetInput(u'Пользователь', u'myshows.ru').result
if not login:
    exit()

password = app.dialogGetInput(u'Пароль', u'не сохраняется').result
if not password:
    exit()
    
list_len = 5

app.dialogCreateSpinnerProgress(u'Загрузка', u'пожалуйста подождите...')
app.dialogShow()

password = hashlib.md5(password).hexdigest()

try:
    a = ul2.urlopen('http://api.myshows.ru/profile/login?login=%s&password=%s' %(login, password))
    cookie = unicode(a.headers['Set-Cookie'], 'cp1251')

    req = ul2.Request('http://api.myshows.ru/profile/episodes/next/')
    req.add_header("Cookie", cookie)
    f = ul2.urlopen(req)
    next = j.loads(f.read())

    req = ul2.Request('http://api.myshows.ru/profile/shows/')
    req.add_header("Cookie", cookie)
    f = ul2.urlopen(req).read()
    shows = j.loads(f)
except:
    app.dialogCreateAlert(u'Ошибка', u'нет соединения с интернетом или неправильное имя или пароль')
    app.dialogSetPositiveButtonText(u'Закрыть')
    app.dialogShow() 
    exit()

app.dialogDismiss()

eps = []

for i in next:
    mon_s = int(next[i][u'airDate'][3:5]) #episode month
    mon_c = t.localtime().tm_mon          #current month
    if mon_s == mon_c:
        eps.append([next[i][u'airDate'],                          #adding current show air date to episodes list
                    shows[unicode(next[i][u'showId'])][u'title'], #adding current show title to episodes list
                    next[i][u'seasonNumber'],                     #adding current show season num to episodes list
                    next[i][u'episodeNumber']])                   #adding current show episode num to episodes list

eps.sort() #sorting episodes list by date

res = '\n'.join('%s %s %sx%s' %(x[0], x[1], x[2], x[3]) for x in eps[:list_len])

app.dialogCreateAlert(u"Следующие эпизоды:")
app.dialogSetItems([res])
app.dialogSetPositiveButtonText(u'OK')
app.dialogShow()
