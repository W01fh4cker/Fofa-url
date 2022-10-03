from tkinter import *
import requests
import json
import base64
import threading
import yaml
import os
import ctypes
import time
import tkinter as tk
import ttkbootstrap as ttk
from tkinter.messagebox import *

def fofa_config_save():
    api = fofa_urls_collector_config_frame_fofa_api_text.get()
    email = fofa_urls_collector_config_frame_fofa_email_text.get()
    key = fofa_urls_collector_config_frame_fofa_key_text.get()
    fofa_config = {
        "api": api,
        "email": email,
        "key": key
    }
    with open("fofa_config.yaml", "w", encoding="utf-8") as f:
        yaml.dump(fofa_config, f, allow_unicode=True)
    showinfo("保存成功！","下次无需再编辑！如果需要修改，再次填写配置保存即可！")

def read_fofa_config():
    with open("fofa_config.yaml","r") as h:
        data = h.read()
        config = yaml.load(data, Loader=yaml.FullLoader)
        return config

def config_existence_judgement():
    if os.path.exists("fofa_config.yaml"):
        return True
    else:
        return False

def base64_enocde_sentence():
    str = encode_entry.get().encode("utf-8")
    str_r = str.decode("utf-8")
    encodestr = base64.b64encode(str)
    str_base64 = encodestr.decode("GB2312")
    encode_text.insert(END, chars=f"【{str_r}】的加密结果为{str_base64}\n")

def fofa_query():
    if(config_existence_judgement()):
        pass
    else:
        showerror("出错啦！", "请先去【fofa采集配置】界面配置fofa再来使用！")
    try:
        fofaConfig = read_fofa_config()
        print(fofaConfig)
        api = fofaConfig["api"]
        email = fofaConfig["email"]
        key = fofaConfig["key"]
        fofa_yf = fofa_urls_collector_collection_frame_yf_text.get()
        fofa_ts = fofa_urls_collector_collection_frame_ts_text.get()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
        }
        url = f"{api}api/v1/search/all?email={email}&key={key}&qbase64={fofa_yf}&size={fofa_ts}".format()
        resp = requests.get(url=url, headers=headers)
        if resp.status_code == -1:
            showerror('出错了！', '账号信息有误。请检查您的email和key是否填写正确！')
            fofa_urls_collector_collection_frame_query_text.insert(END, chars="【×】出错了！账号信息有误,请检查您的email和key是否填写正确！\n")
            fofa_urls_collector_collection_frame_query_text.see(END)
        elif resp.status_code == -4:
            showerror('出错了！', '请求参数有误')
            fofa_urls_collector_collection_frame_query_text.insert(END, chars="【×】出错了！请求参数有误,请检查您的查询语句和查询条数是否填写正确（尤其是后者）！\n")
            fofa_urls_collector_collection_frame_query_text.see(END)
        elif resp.status_code == -5:
            showerror('出错了！', '系统错误，请联系微信W01fh4cker！')
            fofa_urls_collector_collection_frame_query_text.insert(END, chars="【×】出错了！系统错误，请联系微信W01fh4cker！\n")
            fofa_urls_collector_collection_frame_query_text.see(END)
        else:
            res = json.loads((resp.content).decode('utf-8'))
            xlen = len(res["results"])
            showinfo('开始采集', '程序开始采集url，请耐心等待，不要关闭程序。')
            fofa_urls_collector_collection_frame_query_text.insert(END, chars="【+】开始采集！程序开始采集url，请耐心等待，不要关闭程序。\n")
            fofa_urls_collector_collection_frame_query_text.see(END)
            make_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
            file_name = f"fofa_collect_{make_time}.txt"
            for i in range(xlen):
                with open("urls.txt", "a+") as f:
                    url = res["results"][i][0]
                    f.write(url + "\n")
            for j in range(xlen):
                with open("host.txt", "a+") as f:
                    host = res["results"][j][1]
                    f.write(host + "\n")
            with open("urls.txt", 'r') as f:
                ln = f.readlines()
                for j in ln:
                    url = j.strip()
                    if url[:7] == 'http://' or url[:8] == 'https://':
                        with open(file_name, 'a+') as f:
                            fofa_urls_collector_collection_frame_query_text.insert(END, chars=url + "\n")
                            fofa_urls_collector_collection_frame_query_text.see(END)
                            f.write(url + '\n')
                    else:
                        newurl = 'http://' + str(url)
                        with open(file_name, 'a+') as f:
                            fofa_urls_collector_collection_frame_query_text.insert(END, chars=newurl + "\n")
                            fofa_urls_collector_collection_frame_query_text.see(END)
                            f.write(newurl + '\n')
            os.remove('urls.txt')
            os.remove('host.txt')
            showinfo('保存成功', f'保存位置：当前文件夹下的 {file_name} 。')
            fofa_urls_collector_collection_frame_query_text.insert(END, chars=f"【+】保存成功！保存位置：当前文件夹下的 {file_name} 。\n")
            fofa_urls_collector_collection_frame_query_text.see(END)
            f.close()
    except Exception as error:
        showerror("出错了！", f"报错内容：{error}\n请检查您的base64前的语句是否正确（比如英文双引号打成了中文双引号）或是否使用了代理软件；\n若确实没问题，请立即联系微信W01fh4cker！")
        fofa_urls_collector_collection_frame_query_text.insert(END, chars=f"【×】出错了！报错内容：{error}，请检查您的base64前的语句是否正确（比如英文双引号打成了中文双引号）或是否使用了代理软件；若确实没问题，请立即联系微信W01fh4cker！\n")
        fofa_urls_collector_collection_frame_query_text.see(END)

def thread_fofa():
    t = threading.Thread(target=fofa_query)
    t.setDaemon(True)
    t.start()

def fofa_urls_collector_gui():
    global fofa_urls_collector_config_frame_fofa_api_text, fofa_urls_collector_config_frame_fofa_email_text, fofa_urls_collector_config_frame_fofa_key_text, encode_entry, encode_text,  fofa_urls_collector_collection_frame_yf_text, fofa_urls_collector_collection_frame_ts_text, fofa_urls_collector_collection_frame_query_text

    fofa_urls_collector = tk.Tk()
    fofa_urls_collector.title("fofa采集工具 | 只采集url   By: W01fh4cker  Blog: https://W01fh4cker.github.io")
    fofa_urls_collector.geometry("800x600")
    fofa_urls_collector.resizable(0,0)
    myappid = "fofa_urls_collector.1.0"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    fofa_urls_collector.wm_iconbitmap('logo.ico')


    fofa_urls_collector_notebook = ttk.Notebook(fofa_urls_collector, bootstyle="success")


    fofa_urls_collector_config_frame = ttk.Frame()
    fofa_urls_collector_collection_frame = ttk.Frame()
    fofa_urls_collector_config_frame_group_one = ttk.LabelFrame(fofa_urls_collector_config_frame, text="参数配置", bootstyle="info")
    fofa_urls_collector_config_frame_group_one.grid(row=0, column=0, padx=10, pady=10)

    # 填写fofa api头的文本框
    fofa_api = tk.StringVar(fofa_urls_collector_config_frame_group_one,value="填写api头，如https://fofa.info/或者https://g.fofa.info/")
    fofa_urls_collector_config_frame_fofa_api_text = ttk.Entry(fofa_urls_collector_config_frame_group_one, bootstyle="success", width=104, textvariable=fofa_api)
    fofa_urls_collector_config_frame_fofa_api_text.grid(row=0, column=0, padx=5, pady=5)
    # 填写fofa email的文本框
    fofa_email = tk.StringVar(fofa_urls_collector_config_frame_group_one,value="填写fofa账户的邮箱")
    fofa_urls_collector_config_frame_fofa_email_text = ttk.Entry(fofa_urls_collector_config_frame_group_one,bootstyle="success", width=104, textvariable=fofa_email)
    fofa_urls_collector_config_frame_fofa_email_text.grid(row=1, column=0, padx=5, pady=5)
    # 填写fofa key的文本框
    fofa_key = tk.StringVar(fofa_urls_collector_config_frame_group_one,value="填写fofa 账户的key")
    fofa_urls_collector_config_frame_fofa_key_text = ttk.Entry(fofa_urls_collector_config_frame_group_one,bootstyle="success", width=104, textvariable=fofa_key)
    fofa_urls_collector_config_frame_fofa_key_text.grid(row=2, column=0, padx=5, pady=5)
    # 保存配置的按钮
    fofa_urls_collector_config_save_button = ttk.Button(fofa_urls_collector_config_frame_group_one, text="点击保存配置", command=fofa_config_save, width=104, bootstyle="info")
    fofa_urls_collector_config_save_button.grid(row=3, column=0, padx=5, pady=5)

    fofa_urls_collector_config_frame_group_two = ttk.LabelFrame(fofa_urls_collector_config_frame, text="base64加密需要查询的语法", bootstyle="info")
    fofa_urls_collector_config_frame_group_two.grid(row=1, column=0, padx=10, pady=10)
    sentence = tk.StringVar(fofa_urls_collector_config_frame_group_two, value="填写您要加密的语法")
    encode_entry = ttk.Entry(fofa_urls_collector_config_frame_group_two, bootstyle="success", width=75, textvariable=sentence)
    encode_entry.grid(row=0, column=0, padx=5, pady=5)

    encode_button = ttk.Button(fofa_urls_collector_config_frame_group_two, text="点击加密", command=base64_enocde_sentence,width=26)
    encode_button.grid(row=0, column=1, padx=5, pady=5)

    encode_text = tk.scrolledtext.ScrolledText(fofa_urls_collector_config_frame_group_two, width=104, height=14)
    encode_text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    fofa_urls_collector_notebook.add(fofa_urls_collector_config_frame, text="fofa采集配置")
    fofa_urls_collector_notebook.add(fofa_urls_collector_collection_frame, text="fofa url采集")
    fofa_yf = tk.StringVar(value="填写base64后的fofa语法")
    fofa_urls_collector_collection_frame_yf_text = ttk.Entry(fofa_urls_collector_collection_frame, bootstyle="success", width=50, textvariable=fofa_yf)
    fofa_urls_collector_collection_frame_yf_text.grid(row=0, column=0, padx=5, pady=5)
    fofa_ts = tk.StringVar(value="填写查询条数(根据自己的会员情况填写)")
    fofa_urls_collector_collection_frame_ts_text = ttk.Entry(fofa_urls_collector_collection_frame, bootstyle="success", width=35, textvariable=fofa_ts)
    fofa_urls_collector_collection_frame_ts_text.grid(row=0, column=1, padx=5, pady=5)
    fofa_urls_collector_notebook.grid(padx=10, pady=10)
    fofa_urls_collector_collection_frame_query_button = ttk.Button(fofa_urls_collector_collection_frame, text="点击查询", command=thread_fofa, width=15, bootstyle="info")
    fofa_urls_collector_collection_frame_query_button.grid(row=0, column=2, padx=5, pady=5)
    fofa_urls_collector_collection_frame_query_text = tk.scrolledtext.ScrolledText(fofa_urls_collector_collection_frame, width=106, height=28)
    fofa_urls_collector_collection_frame_query_text.grid(row=1, columnspan=3, padx=5, pady=5)
    fofa_urls_collector.mainloop()

if __name__ == "__main__":
    fofa_urls_collector_gui()
