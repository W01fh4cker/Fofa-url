from tkinter import *#line:1
import requests #line:2
import json #line:3
import base64 #line:4
import threading #line:5
import yaml #line:6
import os #line:7
import ctypes #line:8
import time #line:9
import tkinter as tk #line:10
import ttkbootstrap as ttk #line:11
from tkinter .messagebox import *#line:12
def fofa_config_save ():#line:14
    OO00O0O0OO0O00O00 =fofa_urls_collector_config_frame_fofa_api_text .get ()#line:15
    O000O00OO0OOO000O =fofa_urls_collector_config_frame_fofa_email_text .get ()#line:16
    O0OO0O00OOOO0OO00 =fofa_urls_collector_config_frame_fofa_key_text .get ()#line:17
    OO0OOO0O00OOO0OOO ={"api":OO00O0O0OO0O00O00 ,"email":O000O00OO0OOO000O ,"key":O0OO0O00OOOO0OO00 }#line:22
    with open ("fofa_config.yaml","w",encoding ="utf-8")as OOO00OO0O00OO0000 :#line:23
        yaml .dump (OO0OOO0O00OOO0OOO ,OOO00OO0O00OO0000 ,allow_unicode =True )#line:24
    showinfo ("保存成功！","下次无需再编辑！如果需要修改，再次填写配置保存即可！")#line:25
def read_fofa_config ():#line:27
    with open ("fofa_config.yaml","r")as O0O0OO0O0OOO00000 :#line:28
        O00OOOOO000O000O0 =O0O0OO0O0OOO00000 .read ()#line:29
        OO00OOOOO0O0000OO =yaml .load (O00OOOOO000O000O0 ,Loader =yaml .FullLoader )#line:30
        return OO00OOOOO0O0000OO #line:31
def config_existence_judgement ():#line:33
    if os .path .exists ("fofa_config.yaml"):#line:34
        return True #line:35
    else :#line:36
        return False #line:37
def base64_enocde_sentence ():#line:39
    OO0O00O0O000O0O0O =encode_entry .get ().encode ("utf-8")#line:40
    OOOOOOO0O000O0OOO =OO0O00O0O000O0O0O .decode ("utf-8")#line:41
    OOOO00OO0O00O0000 =base64 .b64encode (OO0O00O0O000O0O0O )#line:42
    O0O0O00O00000OOOO =OOOO00OO0O00O0000 .decode ("GB2312")#line:43
    encode_text .insert (END ,chars =f"【{OOOOOOO0O000O0OOO}】的加密结果为{O0O0O00O00000OOOO}\n")#line:44
def fofa_query ():#line:46
    if (config_existence_judgement ()):#line:47
        pass #line:48
    else :#line:49
        showerror ("出错啦！","请先去【fofa采集配置】界面配置fofa再来使用！")#line:50
    try :#line:51
        OO0O0O00O000O0OO0 =read_fofa_config ()#line:52
        print (OO0O0O00O000O0OO0 )#line:53
        OOOO0OOOO0O00OO00 =OO0O0O00O000O0OO0 ["api"]#line:54
        OO00O0OO0OO0000O0 =OO0O0O00O000O0OO0 ["email"]#line:55
        OO00OOO0O0O00O0OO =OO0O0O00O000O0OO0 ["key"]#line:56
        OO0OO0000OO0OOO00 =fofa_urls_collector_collection_frame_yf_text .get ()#line:57
        OOO0O0OOO00000O00 =fofa_urls_collector_collection_frame_ts_text .get ()#line:58
        OO0000OO0OO0O000O ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}#line:61
        OO0000000000OOO00 =f"{OOOO0OOOO0O00OO00}api/v1/search/all?email={OO00O0OO0OO0000O0}&key={OO00OOO0O0O00O0OO}&qbase64={OO0OO0000OO0OOO00}&size={OOO0O0OOO00000O00}".format ()#line:62
        O00OO00O00OOOOO00 =requests .get (url =OO0000000000OOO00 ,headers =OO0000OO0OO0O000O )#line:63
        if O00OO00O00OOOOO00 .status_code ==-1 :#line:64
            showerror ('出错了！','账号信息有误。请检查您的email和key是否填写正确！')#line:65
            fofa_urls_collector_collection_frame_query_text .insert (END ,chars ="【×】出错了！账号信息有误,请检查您的email和key是否填写正确！\n")#line:66
            fofa_urls_collector_collection_frame_query_text .see (END )#line:67
        elif O00OO00O00OOOOO00 .status_code ==-4 :#line:68
            showerror ('出错了！','请求参数有误')#line:69
            fofa_urls_collector_collection_frame_query_text .insert (END ,chars ="【×】出错了！请求参数有误,请检查您的查询语句和查询条数是否填写正确（尤其是后者）！\n")#line:70
            fofa_urls_collector_collection_frame_query_text .see (END )#line:71
        elif O00OO00O00OOOOO00 .status_code ==-5 :#line:72
            showerror ('出错了！','系统错误，请联系微信W01fh4cker！')#line:73
            fofa_urls_collector_collection_frame_query_text .insert (END ,chars ="【×】出错了！系统错误，请联系微信W01fh4cker！\n")#line:74
            fofa_urls_collector_collection_frame_query_text .see (END )#line:75
        else :#line:76
            O00OOOOO0O0000OOO =json .loads ((O00OO00O00OOOOO00 .content ).decode ('utf-8'))#line:77
            OOO0OOO000OO0O0OO =len (O00OOOOO0O0000OOO ["results"])#line:78
            showinfo ('开始采集','程序开始采集url，请耐心等待，不要关闭程序。')#line:79
            fofa_urls_collector_collection_frame_query_text .insert (END ,chars ="【+】开始采集！程序开始采集url，请耐心等待，不要关闭程序。\n")#line:80
            fofa_urls_collector_collection_frame_query_text .see (END )#line:81
            OO0000OO0O0OO00OO =time .strftime ("%Y_%m_%d_%H_%M_%S",time .localtime ())#line:82
            OOOO0OO00OOOOO0O0 =f"fofa_collect_{OO0000OO0O0OO00OO}.txt"#line:83
            for O0O000OO0O0O00OOO in range (OOO0OOO000OO0O0OO ):#line:84
                with open ("urls.txt","a+")as OO000OO0OOOO0O000 :#line:85
                    OO0000000000OOO00 =O00OOOOO0O0000OOO ["results"][O0O000OO0O0O00OOO ][0 ]#line:86
                    OO000OO0OOOO0O000 .write (OO0000000000OOO00 +"\n")#line:87
            for OO000O0OOO000O0O0 in range (OOO0OOO000OO0O0OO ):#line:88
                with open ("host.txt","a+")as OO000OO0OOOO0O000 :#line:89
                    O00OO000OOOO0O000 =O00OOOOO0O0000OOO ["results"][OO000O0OOO000O0O0 ][1 ]#line:90
                    OO000OO0OOOO0O000 .write (O00OO000OOOO0O000 +"\n")#line:91
            with open ("urls.txt",'r')as OO000OO0OOOO0O000 :#line:92
                OOO0O0OOOOOO00O0O =OO000OO0OOOO0O000 .readlines ()#line:93
                for OO000O0OOO000O0O0 in OOO0O0OOOOOO00O0O :#line:94
                    OO0000000000OOO00 =OO000O0OOO000O0O0 .strip ()#line:95
                    if OO0000000000OOO00 [:7 ]=='http://'or OO0000000000OOO00 [:8 ]=='https://':#line:96
                        with open (OOOO0OO00OOOOO0O0 ,'a+')as OO000OO0OOOO0O000 :#line:97
                            fofa_urls_collector_collection_frame_query_text .insert (END ,chars =OO0000000000OOO00 +"\n")#line:98
                            fofa_urls_collector_collection_frame_query_text .see (END )#line:99
                            OO000OO0OOOO0O000 .write (OO0000000000OOO00 +'\n')#line:100
                    else :#line:101
                        O0O0000O00O000OO0 ='http://'+str (OO0000000000OOO00 )#line:102
                        with open (OOOO0OO00OOOOO0O0 ,'a+')as OO000OO0OOOO0O000 :#line:103
                            fofa_urls_collector_collection_frame_query_text .insert (END ,chars =O0O0000O00O000OO0 +"\n")#line:104
                            fofa_urls_collector_collection_frame_query_text .see (END )#line:105
                            OO000OO0OOOO0O000 .write (O0O0000O00O000OO0 +'\n')#line:106
            os .remove ('urls.txt')#line:107
            os .remove ('host.txt')#line:108
            showinfo ('保存成功',f'保存位置：当前文件夹下的 {OOOO0OO00OOOOO0O0} 。')#line:109
            fofa_urls_collector_collection_frame_query_text .insert (END ,chars =f"【+】保存成功！保存位置：当前文件夹下的 {OOOO0OO00OOOOO0O0} 。\n")#line:110
            fofa_urls_collector_collection_frame_query_text .see (END )#line:111
            OO000OO0OOOO0O000 .close ()#line:112
    except Exception as OOO000O0O000OOOO0 :#line:113
        showerror ("出错了！",f"报错内容：{OOO000O0O000OOOO0}\n请检查您的base64前的语句是否正确（比如英文双引号打成了中文双引号）或是否使用了代理软件；\n若确实没问题，请立即联系微信W01fh4cker！")#line:114
        fofa_urls_collector_collection_frame_query_text .insert (END ,chars =f"【×】出错了！报错内容：{OOO000O0O000OOOO0}，请检查您的base64前的语句是否正确（比如英文双引号打成了中文双引号）或是否使用了代理软件；若确实没问题，请立即联系微信W01fh4cker！\n")#line:115
        fofa_urls_collector_collection_frame_query_text .see (END )#line:116
def thread_fofa ():#line:118
    O0O00O0000O000O00 =threading .Thread (target =fofa_query )#line:119
    O0O00O0000O000O00 .setDaemon (True )#line:120
    O0O00O0000O000O00 .start ()#line:121
def fofa_urls_collector_gui ():#line:123
    global fofa_urls_collector_config_frame_fofa_api_text ,fofa_urls_collector_config_frame_fofa_email_text ,fofa_urls_collector_config_frame_fofa_key_text ,encode_entry ,encode_text ,fofa_urls_collector_collection_frame_yf_text ,fofa_urls_collector_collection_frame_ts_text ,fofa_urls_collector_collection_frame_query_text #line:124
    OOO00OOOOO0OOO00O =tk .Tk ()#line:126
    OOO00OOOOO0OOO00O .title ("fofa采集工具 | 只采集url   By: W01fh4cker  Blog: https://W01fh4cker.github.io")#line:127
    OOO00OOOOO0OOO00O .geometry ("800x600")#line:128
    OOO00OOOOO0OOO00O .resizable (0 ,0 )#line:129
    OO00O0O00OOO0OO0O ="fofa_urls_collector.1.0"#line:130
    ctypes .windll .shell32 .SetCurrentProcessExplicitAppUserModelID (OO00O0O00OOO0OO0O )#line:131
    OOO00OOOOO0OOO00O .wm_iconbitmap ('logo.ico')#line:132
    O00O0OOO000O0000O =ttk .Notebook (OOO00OOOOO0OOO00O ,bootstyle ="success")#line:135
    OOOOO00OOOO0OOO0O =ttk .Frame ()#line:138
    OO000OO0O0O00OOO0 =ttk .Frame ()#line:139
    OOOOO0O00OO00O00O =ttk .LabelFrame (OOOOO00OOOO0OOO0O ,text ="参数配置",bootstyle ="info")#line:140
    OOOOO0O00OO00O00O .grid (row =0 ,column =0 ,padx =10 ,pady =10 )#line:141
    O000O0OO00OOO0O0O =tk .StringVar (OOOOO0O00OO00O00O ,value ="填写api头，如https://fofa.info/或者https://g.fofa.info/")#line:144
    fofa_urls_collector_config_frame_fofa_api_text =ttk .Entry (OOOOO0O00OO00O00O ,bootstyle ="success",width =104 ,textvariable =O000O0OO00OOO0O0O )#line:145
    fofa_urls_collector_config_frame_fofa_api_text .grid (row =0 ,column =0 ,padx =5 ,pady =5 )#line:146
    O0000000OO0OO0000 =tk .StringVar (OOOOO0O00OO00O00O ,value ="填写fofa账户的邮箱")#line:148
    fofa_urls_collector_config_frame_fofa_email_text =ttk .Entry (OOOOO0O00OO00O00O ,bootstyle ="success",width =104 ,textvariable =O0000000OO0OO0000 )#line:149
    fofa_urls_collector_config_frame_fofa_email_text .grid (row =1 ,column =0 ,padx =5 ,pady =5 )#line:150
    O0OOOO0OOO00O000O =tk .StringVar (OOOOO0O00OO00O00O ,value ="填写fofa 账户的key")#line:152
    fofa_urls_collector_config_frame_fofa_key_text =ttk .Entry (OOOOO0O00OO00O00O ,bootstyle ="success",width =104 ,textvariable =O0OOOO0OOO00O000O )#line:153
    fofa_urls_collector_config_frame_fofa_key_text .grid (row =2 ,column =0 ,padx =5 ,pady =5 )#line:154
    OO0OO00OO0OO000OO =ttk .Button (OOOOO0O00OO00O00O ,text ="点击保存配置",command =fofa_config_save ,width =104 ,bootstyle ="info")#line:156
    OO0OO00OO0OO000OO .grid (row =3 ,column =0 ,padx =5 ,pady =5 )#line:157
    OOO00O0O0O000O0O0 =ttk .LabelFrame (OOOOO00OOOO0OOO0O ,text ="base64加密需要查询的语法",bootstyle ="info")#line:159
    OOO00O0O0O000O0O0 .grid (row =1 ,column =0 ,padx =10 ,pady =10 )#line:160
    O0O0OOO000OOOO00O =tk .StringVar (OOO00O0O0O000O0O0 ,value ="填写您要加密的语法")#line:161
    encode_entry =ttk .Entry (OOO00O0O0O000O0O0 ,bootstyle ="success",width =75 ,textvariable =O0O0OOO000OOOO00O )#line:162
    encode_entry .grid (row =0 ,column =0 ,padx =5 ,pady =5 )#line:163
    OO000O0O0000O0OO0 =ttk .Button (OOO00O0O0O000O0O0 ,text ="点击加密",command =base64_enocde_sentence ,width =26 )#line:165
    OO000O0O0000O0OO0 .grid (row =0 ,column =1 ,padx =5 ,pady =5 )#line:166
    encode_text =tk .scrolledtext .ScrolledText (OOO00O0O0O000O0O0 ,width =104 ,height =14 )#line:168
    encode_text .grid (row =1 ,column =0 ,columnspan =2 ,padx =5 ,pady =5 )#line:169
    O00O0OOO000O0000O .add (OOOOO00OOOO0OOO0O ,text ="fofa采集配置")#line:171
    O00O0OOO000O0000O .add (OO000OO0O0O00OOO0 ,text ="fofa url采集")#line:172
    OO0OO0O0OOOO00O00 =tk .StringVar (value ="填写base64后的fofa语法")#line:173
    fofa_urls_collector_collection_frame_yf_text =ttk .Entry (OO000OO0O0O00OOO0 ,bootstyle ="success",width =50 ,textvariable =OO0OO0O0OOOO00O00 )#line:174
    fofa_urls_collector_collection_frame_yf_text .grid (row =0 ,column =0 ,padx =5 ,pady =5 )#line:175
    O0O0O0000O0OO000O =tk .StringVar (value ="填写查询条数(根据自己的会员情况填写)")#line:176
    fofa_urls_collector_collection_frame_ts_text =ttk .Entry (OO000OO0O0O00OOO0 ,bootstyle ="success",width =35 ,textvariable =O0O0O0000O0OO000O )#line:177
    fofa_urls_collector_collection_frame_ts_text .grid (row =0 ,column =1 ,padx =5 ,pady =5 )#line:178
    O00O0OOO000O0000O .grid (padx =10 ,pady =10 )#line:179
    O00O0OOO0OOO00O0O =ttk .Button (OO000OO0O0O00OOO0 ,text ="点击查询",command =thread_fofa ,width =15 ,bootstyle ="info")#line:180
    O00O0OOO0OOO00O0O .grid (row =0 ,column =2 ,padx =5 ,pady =5 )#line:181
    fofa_urls_collector_collection_frame_query_text =tk .scrolledtext .ScrolledText (OO000OO0O0O00OOO0 ,width =106 ,height =28 )#line:182
    fofa_urls_collector_collection_frame_query_text .grid (row =1 ,columnspan =3 ,padx =5 ,pady =5 )#line:183
    OOO00OOOOO0OOO00O .mainloop ()#line:184
if __name__ =="__main__":#line:186
    fofa_urls_collector_gui ()