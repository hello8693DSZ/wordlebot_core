# coding=utf-8
from os import system
import enchant # 单词拼写判断依赖pyenchant，需要提前安装


wordleword = "world" # 正确的单词
availableword = enchant.Dict("en_US")

anslist=[]
def guess_word(word,stat):
    global wordleword
    global guessnum
    global guesslist
    word = word.lower()
    if len(word) != len(wordleword):
        return "你输入单词的字母数量错了。应该是"+str(len(wordleword))+"个字母。"
    elif availableword.check(word) == False:
        return "你输入的单词不在词库中。"
    else:
        if stat==1:
            guesslist.append(word)
            guessnum+=1
        color=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        cnt=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        msg=""
        for i in range(len(word)):
            if word[i]==wordleword[i]:
                color[i]=1
            else:
                color[i]=0
                cnt[ord(wordleword[i])]+=1
        for i in range(len(word)):
            if color[i]==0:
                if cnt[ord(word[i])]!=0:
                    color[i]=-1
                    cnt[ord(word[i])]-=1
        for i in range(len(word)):
            if color[i]==1:
                msg+="绿"
            elif color[i]==0:
                msg+="灰"
            elif color[i]==-1:
                msg+="黄"
        return msg
guesslist=[]
guessnum=0
def wordlepng(word):
    global wordleword
    global guessnum
    global guesslist
    p=guess_word(word,1)
    if p[0]=="你":
        return p
    else:
        for i in range(guessnum):
            p=guess_word(guesslist[i],0)
def realguess(s):
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont
    global wordlelist
    global wordleword
    global guessnum
    global guesslist
    wordles = guess_word(s,1)
    if wordles[0] == "你":
        return wordles
    else:
        img = Image.new("RGB", (100*len(wordleword),100*guessnum), "white")
        for histnum in range(guessnum):
            draw = ImageDraw.Draw(img)
            x = 0
            y = 100*histnum
            histwordle=guess_word(guesslist[histnum],0)
            hist=guesslist[histnum]
            for i in range(len(histwordle)):
                if histwordle[i] == "绿":
                    draw.rectangle((x, y, x + 100, y + 100), fill="green")
                elif histwordle[i] == "灰":
                    draw.rectangle((x, y, x + 100, y + 100), fill="grey")
                elif histwordle[i] == "黄":
                    draw.rectangle((x, y, x + 100, y + 100), fill="yellow")
                x += 100
                # if x == 300:
                #     x = 0
                #     y += 100
            x=7/20*100
            y=5/20*100+100*histnum
            font = ImageFont.truetype('Consolas.ttf', 50)  # 依赖字体文件需要提前拷贝到同目录
            for i in range(len(histwordle)):
                if histwordle[i] == "绿":
                    draw.text((x, y), hist[i], fill="black",font=font)
                elif histwordle[i] == "灰":
                    draw.text((x, y), hist[i], fill="black",font=font)
                elif histwordle[i] == "黄":
                    draw.text((x, y), hist[i], fill="black",font=font)
                x += 100
                # if x == 300:
                #     x = 0
                #     y += 100
            
        img.save("wordle.png")
        return "wordle.png"
#realguess("你要猜的是什么")
#如果正常就会返回wordle.png，当前目录下
#否则返回一个字符串，提示错误

# Demo:
#
# wordleword=input("input:")
# while 1:
#     s=input("")
#     if s=="":
#         break
#     else:
#         m=realguess(s)
#         if m[0]=="你":
#             print(m)
#         else:
#             system("start "+m)
#         if s==wordleword:
#             print("恭喜你猜对了")
#             break
