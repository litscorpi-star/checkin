
from message_send import MessageSend
from config import message_tokens, youdao_cookie,ali_refresh_token,ty_pwd,ty_user,youdao_user, redis_info
import aliyunpan, tianyiyunpan,YouDao_user_login
import notify

def run():
    content =''
    title = ""
    if youdao_user != None:
        youdao_sign=YouDao_user_login.Youdao(youdao_user, redis_info)
        content= youdao_sign.run() + '\n\n'
        title = "【有道】"
    # if ali_refresh_token != None :
    #     Aliyun=aliyunpan.Ali(ali_refresh_token, redis_info)
    #     content += Aliyun.run() + '\n\n'
    #     title += "【阿里】"
    # if ty_user != None and ty_pwd != None:
    #     content += tianyiyunpan.main(ty_user, ty_pwd)
    #     title += "【天翼】"

    send = MessageSend()
    send.send_all(message_tokens,title+'每日签到',content)
    # 另一种通知方式
    notify.send(title+'每日签到',content)

def ty_run():
    user_ty = []
    pwd_ty = []
    user_ty.extend(ty_user.split(","))
    pwd_ty.extend(ty_pwd.split(","))
    print(user_ty)
    for i in range(len(user_ty)):
        if user_ty[i] != None and pwd_ty[i] != None:
            content += tianyiyunpan.main(user_ty[i], pwd_ty[i])
            title += "【天翼】"+user_ty[i]
            notify.send(title+'每日签到',content)
        
if __name__ == "__main__":
    try_run()


    


