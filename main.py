# import time, asyncio
import discord
from ydl import *
from game import *
from user import *
from chat import *
from shop import *
from discord.ext import commands

bot = commands.Bot(command_prefix=".")
token = open("token.txt", "r").readline()
mls = []


dic = {
1101	:'	권용하	',
1102	:'	김선웅	',
1103	:'	김영준	',
1104	:'	남승우	',
1105	:'	박준형	',
1106	:'	배현서	',
1107	:'	변지예	',
1108	:'	이다연	',
1109	:'	이원재A	',
1110	:'	임설호	',
1111	:'	전지민	',
1112	:'	정유찬B	',
1113	:'	조연우	',
1114	:'	조영인	',
1115	:'	한승우	',
1116	:'	허재학	',
1201	:'	고민준	',
1202	:'	김성현	',
1203	:'	김현준	',
1204	:'	박성빈	',
1205	:'	박재영	',
1206	:'	심이센	',
1207	:'	유지훈	',
1208	:'	이상기	',
1209	:'	이서준	',
1210	:'	이승환	',
1211	:'	임세준	',
1212	:'	임재현	',
1213	:'	임지언	',
1214	:'	정준호	',
1215	:'	주성운	',
1216	:'	최재훈	',
1301	:'	권성안	',
1302	:'	김도균	',
1303	:'	김동원	',
1304	:'	김산	',
1305	:'	노이헌	',
1306	:'	박승비	',
1307	:'	박준상	',
1308	:'	박탐	',
1309	:'	박현민	',
1310	:'	이관우	',
1311	:'	이범석	',
1312	:'	이원재B	',
1313	:'	이지후A	',
1314	:'	이현진	',
1315	:'	전승주	',
1316	:'	최민종	',
1401	:'	김시호	',
1402	:'	류태상	',
1403	:'	박세진	',
1404	:'	박시형	',
1405	:'	박준혁	',
1406	:'	방지현	',
1407	:'	서세준	',
1408	:'	신유범	',
1409	:'	윤동섭	',
1410	:'	윤성현	',
1411	:'	이준서	',
1412	:'	이지후B	',
1413	:'	정유찬A	',
1414	:'	최정윤	',
1415	:'	한승헌	',
1501	:'	김규민	',
1502	:'	김영훈	',
1503	:'	김주영	',
1504	:'	류재민	',
1505	:'	박도영	',
1506	:'	박준원	',
1507	:'	반지호	',
1508	:'	서규민	',
1509	:'	서채원	',
1510	:'	성이루	',
1511	:'	윤원준	',
1512	:'	이윤수	',
1513	:'	이주협	',
1514	:'	정다온	',
1515	:'	최홍우	',
1516	:'	한은혜	',
1601	:'	김범준	',
1602	:'	김희재	',
1603	:'	박진원	',
1604	:'	방유찬	',
1605	:'	배준휘	',
1606	:'	양준혁	',
1607	:'	이승현	',
1608	:'	이현채	',
1609	:'	이형석	',
1610	:'	이형주	',
1611	:'	이화인	',
1612	:'	장준성	',
1613	:'	정우찬	',
1614	:'	정채원	',
1615	:'	조명기	',
1616	:'	차이경	',
1701	:'	권지이	',
1702	:'	김수빈	',
1703	:'	설곽 기여미 진모 >_<	',
1704	:'	김진하	',
1705	:'	문새결	',
1706	:'	박상훈	',
1707	:'	박해성	',
1708	:'	백종현	',
1709	:'	엄휘식	',
1710	:'	이민혁	',
1711	:'	장민기	',
1712	:'	장희찬	',
1713	:'	정해찬	',
1714	:'	정현우	',
1715	:'	조민상	',
1716	:'	허정	',
1801	:'	고윤석	',
1802	:'	김선우	',
1803	:'	김예성	',
1804	:'	김유현	',
1805	:'	박주형	',
1806	:'	손훈일	',
1807	:'	이규동	',
1808	:'	이동훈	',
1809	:'	이승원	',
1810	:'	이예준	',
1811	:'	이정진	',
1812	:'	정재원	',
1813	:'	조윤재	',
1814	:'	조준우	',
1815	:'	최우진	',
2101	:'	강동우	',
2102	:'	고영린	',
2103	:'	김동현A	',
2104	:'	김민준A	',
2105	:'	김재우	',
2106	:'	남우현	',
2107	:'	노세현	',
2108	:'	박경원	',
2109	:'	반딧불	',
2110	:'	손형우	',
2111	:'	이윤서	',
2112	:'	이준서	',
2113	:'	이한주	',
2114	:'	임상우	',
2115	:'	조성길	',
2116	:'	조성호	',
2117	:'	최원서	',
2201	:'	고건	',
2202	:'	김남진	',
2203	:'	김대순	',
2204	:'	김동환	',
2205	:'	김석환	',
2206	:'	문준원	',
2207	:'	박지형	',
2208	:'	서지민	',
2209	:'	송경민	',
2210	:'	양준혁	',
2211	:'	오태인	',
2212	:'	유지민	',
2213	:'	육민수	',
2214	:'	이재용	',
2215	:'	이현서	',
2216	:'	조원준	',
2301	:'	권보민	',
2302	:'	김성헌	',
2303	:'	김종우	',
2304	:'	박지연	',
2305	:'	박진수	',
2306	:'	박찬우	',
2307	:'	송재한	',
2308	:'	여현준	',
2309	:'	유현우	',
2310	:'	윤동규	',
2311	:'	이재효	',
2312	:'	이호준	',
2313	:'	정우진	',
2314	:'	한정우	',
2315	:'	홍경찬	',
2316	:'	황인환	',
2401	:'	고도영	',
2402	:'	김선호	',
2403	:'	김성혁	',
2404	:'	김세헌	',
2405	:'	김수민	',
2406	:'	문성빈	',
2407	:'	문승현	',
2408	:'	배서연	',
2409	:'	송우석	',
2410	:'	신명진	',
2411	:'	안도현	',
2412	:'	안현태	',
2413	:'	안호중	',
2414	:'	이준혁B	',
2415	:'	정정훈	',
2416	:'	최민준	',
2417	:'	함주현	',
2501	:'	권재욱	',
2502	:'	김민준B	',
2503	:'	김찬우	',
2504	:'	김해정	',
2505	:'	문수혁	',
2506	:'	박제하	',
2507	:'	심준선	',
2508	:'	이성민	',
2509	:'	이주한	',
2510	:'	이채운	',
2511	:'	정시우	',
2512	:'	정재원	',
2513	:'	정진교	',
2514	:'	조석희	',
2515	:'	최건	',
2516	:'	최성민	',
2517	:'	홍재영	',
2601	:'	김동규	',
2602	:'	김동현B	',
2603	:'	김용재	',
2604	:'	류호원	',
2605	:'	민규철	',
2606	:'	민정호	',
2607	:'	박정우	',
2608	:'	박지호	',
2609	:'	송민혁	',
2610	:'	유연주	',
2611	:'	이동재	',
2612	:'	이서준	',
2613	:'	임재아	',
2614	:'	장윤성	',
2615	:'	차원재	',
2616	:'	한서준	',
2617	:'	황수영	',
2701	:'	구현모	',
2702	:'	길아성	',
2703	:'	김성준	',
2704	:'	김영준	',
2705	:'	김지환	',
2706	:'	김현준	',
2707	:'	나윤호	',
2708	:'	변형준	',
2709	:'	이경민	',
2710	:'	이동건	',
2711	:'	이주원	',
2712	:'	이준우	',
2713	:'	이준혁A	',
2714	:'	이지후	',
2715	:'	최원형	',
2716	:'	설곽최고 기여미 옹겸	',
2801	:'	강현후	',
2802	:'	김영서	',
2803	:'	김재영	',
2804	:'	서한결	',
2805	:'	손지훈	',
2806	:'	송현욱	',
2807	:'	신다윤	',
2808	:'	임서윤	',
2809	:'	장현서	',
2810	:'	정선	',
2811	:'	정찬우	',
2812	:'	한상우	',
2813	:'	홍휘택	',
2814	:'	황아현	',
2815	:'	황태훈	',
2816	:'	오유찬	',
3101	:'	강두의	',
3102	:'	김동우	',
3103	:'	김준현	',
3104	:'	김태윤B	',
3105	:'	서민석	',
3106	:'	송석원	',
3107	:'	심재진	',
3108	:'	양지민	',
3109	:'	이대준	',
3110	:'	이선우	',
3111	:'	이수민	',
3112	:'	이우진	',
3113	:'	진재범	',
3114	:'	최혁	',
3115	:'	현영우	',
3201	:'	김민서	',
3202	:'	김범준	',
3203	:'	김선우	',
3204	:'	김태민	',
3205	:'	김태윤C	',
3206	:'	박상연	',
3207	:'	박성준	',
3208	:'	박수현	',
3209	:'	변재환	',
3210	:'	유동주	',
3211	:'	윤소영	',
3212	:'	이준혁	',
3213	:'	이찬	',
3214	:'	이형진	',
3215	:'	황보현	',
3216	:'	황성빈	',
3301	:'	강현	',
3302	:'	김정현	',
3303	:'	김지호	',
3304	:'	김태윤A	',
3305	:'	민지홍	',
3306	:'	박범희	',
3307	:'	백우준	',
3308	:'	백인규	',
3309	:'	서유완	',
3310	:'	손현준	',
3311	:'	유정인	',
3312	:'	윤민식	',
3313	:'	이은재	',
3314	:'	이진환	',
3315	:'	전상욱	',
3401	:'	강태연	',
3402	:'	구홍진	',
3403	:'	기현민	',
3404	:'	김종은	',
3405	:'	김지민	',
3406	:'	김형운	',
3407	:'	송치영	',
3408	:'	신원호	',
3409	:'	신재욱	',
3410	:'	심규성	',
3411	:'	위현복	',
3412	:'	이남욱	',
3413	:'	이호준	',
3414	:'	최원준	',
3415	:'	최재현	',
3501	:'	곽재석	',
3502	:'	김민재	',
3503	:'	김원일	',
3504	:'	김태윤D	',
3505	:'	김형환	',
3506	:'	김호준	',
3507	:'	변수현	',
3508	:'	변준섭	',
3509	:'	우상엽	',
3510	:'	이기석	',
3511	:'	이승우	',
3512	:'	장근영	',
3513	:'	조용성	',
3514	:'	차지명	',
3515	:'	한승범	',
3601	:'	권혁	',
3602	:'	김경민	',
3603	:'	김민성	',
3604	:'	김민순	',
3605	:'	박재훈	',
3606	:'	신희제	',
3607	:'	오유준	',
3608	:'	오태현	',
3609	:'	이재정	',
3610	:'	장유진	',
3611	:'	조민범	',
3612	:'	조민재	',
3613	:'	천승준	',
3614	:'	최준서	',
3615	:'	한지훈	',
3616	:'	허은수	',
3701	:'	구민재	',
3702	:'	김준서	',
3703	:'	문권희	',
3704	:'	문재현	',
3705	:'	박지우	',
3706	:'	박태원	',
3707	:'	안서영	',
3708	:'	오재석	',
3709	:'	이기민	',
3710	:'	전혁주	',
3711	:'	조경아	',
3712	:'	최민규	',
3713	:'	최우진	',
3714	:'	한정민	',
3715	:'	황혜준	',
3801	:'	김승엽	',
3802	:'	김신건	',
3803	:'	김유건	',
3804	:'	김현우	',
3805	:'	박래오	',
3806	:'	박병모	',
3807	:'	손선빈	',
3808	:'	신해인	',
3809	:'	윤예람	',
3810	:'	이준상	',
3811	:'	정승민	',
3812	:'	조민성	',
3813	:'	조상렬	',
3814	:'	최동민	',
3815	:'	최서현	',
3816	:'	황두환	'
}

@bot.event
async def on_ready():
    print("I have logged in as {0.user}\n".format(bot))


# =============================== CHAT =======================================


@bot.command()
async def hello(ctx):
    await ctx.send("hello")


@bot.command()
async def chat(ctx, _de):
    print()


# =============================== SSHS BOT =======================================


@bot.command()
async def check(ctx, arg):
    embed = discord.Embed(title=dic[int(arg)], color=0xAAFFFF)
    embed.set_footer(text="SSHS DISCORD BOT")
    await ctx.send(embed=embed)


@bot.command()
async def sshs(ctx):
    embed = discord.Embed(title="SSHS DISCORD BOT", description="IS NOW DEVELOPING", color=0x6E17E3)
    embed.add_field(name=bot.command_prefix + "sshs", value="도움말을 보여줍니다.", inline=False)
    embed.add_field(name=bot.command_prefix + "rand", value="봇과의 주사위 게임", inline=False)
    embed.add_field(name=bot.command_prefix + "register", value="SSHS봇 회원가입", inline=False)
    embed.add_field(name=bot.command_prefix + "info", value="개인 정보를 봅니다.", inline=False)
    embed.add_field(name=bot.command_prefix + "pinfo [Target]", value="[Target]의 정보를 봅니다.", inline=False)
    embed.add_field(name=bot.command_prefix + "send [Target] [Money]", value="[Target]에게 [Money]를 줍니다.", inline=False)
    embed.add_field(name=bot.command_prefix + "bet [Money]", value="[Money]만큼의 도박을 합니다.", inline=False)
    embed.add_field(name=bot.command_prefix + "bank [(in/out)] [Money]", value="[Money]를 개인은행에 저장합니다.", inline=False)
    await ctx.send(embed=embed)


# =============================== DICE GAME =======================================


@bot.command()
async def rand(ctx):
    result, _color, bot1, bot2, user1, user2, a, b = dice()
    embed = discord.Embed(title="주사위 게임 결과", description=None, color=_color)
    embed.add_field(name="SSHS BOT의 숫자 " + bot1 + "+" + bot2, value=":game_die: " + a, inline=False)
    embed.add_field(name=ctx.author.name + "의 숫자 " + user1 + "+" + user2, value=":game_die: " + b, inline=False)
    embed.set_footer(text="결과: " + result)
    await ctx.send(embed=embed)


# =============================== GAMBLING =======================================


@bot.command()
async def bet(ctx, money):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    win = gamble()
    result = ""
    betting = 0
    _color = 0x000000
    if userExistance:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        cur_money = getMoney(ctx.author.name, userRow)
        if money == "allin":
            if getMoney(ctx.author.name, userRow) < 500000:
                await ctx.send('500000이상의 자산이 있어야 allin하실 수 있습니다.')
                return
            betting = cur_money
            if win:
                result = "성공"
                _color = 0x00ff56
                print(result)

                modifyMoney(ctx.author.name, userRow, int(2 * betting))

            else:
                result = "실패"
                _color = 0xFF0000
                print(result)

                modifyMoney(ctx.author.name, userRow, -int(betting))
                addLoss(ctx.author.name, userRow, int(betting))

            embed = discord.Embed(title="{} 도박 결과".format(ctx.author.name), description=result, color=_color)
            embed.add_field(name="배팅금액", value=betting, inline=False)
            embed.add_field(name="현재 자산", value=getMoney(ctx.author.name, userRow), inline=False)

            await ctx.send(embed=embed)

        elif int(money) >= 1000:
            if cur_money >= int(money):
                betting = int(money)
                print("배팅금액: ", betting)
                print("")

                if win:
                    result = "성공"
                    _color = 0x00ff56
                    print(result)

                    modifyMoney(ctx.author.name, userRow, int(1 * betting))

                else:
                    result = "실패"
                    _color = 0xFF0000
                    print(result)

                    modifyMoney(ctx.author.name, userRow, -int(betting))
                    addLoss(ctx.author.name, userRow, int(betting))

                embed = discord.Embed(title="{} 도박 결과".format(ctx.author), description=result, color=_color)
                embed.add_field(name="배팅금액", value=str(betting), inline=False)
                embed.add_field(name="현재 자산", value=getMoney(ctx.author.name, userRow), inline=False)
                await ctx.send(embed=embed)
            else:
                print("돈이 부족합니다.")
                print("배팅금액: ", money, " | 현재자산: ", cur_money)
                await ctx.send("돈이 부족합니다. 현재자산: " + str(cur_money))
        else:
            print("배팅금액", money, "가 10보다 작습니다.")
            await ctx.send("1000원 이상만 배팅 가능합니다.")
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        await ctx.send("도박은 회원가입 후 이용 가능합니다.")
    print("------------------------------\n")


@bot.command()
async def rank(ctx):
    rank = ranking()
    embed = discord.Embed(title="Level Ranking", description=None, color=0x4A44FF)

    for i in range(0, len(rank)):
        if i % 2 == 0:
            name = rank[i]
            lvl = rank[i + 1]
            embed.add_field(name=str(int(i / 2 + 1)) + "위 " + name, value="Level: " + str(lvl), inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def cashrank(ctx):
    cashrank = cashranking()
    embed = discord.Embed(title="Cash Ranking", description=None, color=0x4A44FF)
    for i in range(0, len(cashrank)):
        if i % 2 == 0:
            name = cashrank[i]
            cash = cashrank[i + 1]
            embed.add_field(name=str(int(i / 2 + 1)) + "위 " + name, value="Cash: " + str(cash), inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def register(ctx):
    print("회원가입이 가능한지 확인합니다.")
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    if userExistance:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        print("------------------------------\n")
        await ctx.send("이미 가입하셨습니다.")
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("")

        Signup(ctx.author.name, ctx.author.id)

        print("회원가입이 완료되었습니다.")
        print("------------------------------\n")
        await ctx.send("회원가입이 완료되었습니다.")


@bot.command()
async def info(ctx):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    if not userExistance:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send("회원가입 후 자신의 정보를 확인할 수 있습니다.")
    else:
        level, exp, money, bank, loss = userInfo(userRow)
        rank = getRank(userRow)
        userNum = checkUserNum()
        expToUP = level * level + 6 * level
        boxes = int(exp / expToUP * 20)
        print("------------------------------\n")
        embed = discord.Embed(title="유저 정보", description=ctx.author.name, color=0x62D0F6)
        embed.add_field(name="레벨", value=level)
        embed.add_field(name="순위", value=str(rank) + "/" + str(userNum))
        embed.add_field(name="XP: " + str(exp) + "/" + str(expToUP),
                        value=boxes * ":blue_square:" + (20 - boxes) * ":white_large_square:", inline=False)
        embed.add_field(name="보유 자산", value=money, inline=False)
        embed.add_field(name="은행 자산", value=bank, inline=False)
        embed.add_field(name="도박으로 날린 돈", value=loss, inline=False)

        await ctx.send(embed=embed)


@bot.command()
async def pinfo(ctx, user: discord.User):
    userExistance, userRow = checkUser(user.name, user.id)

    if not userExistance:
        print("DB에서 ", user.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send(user.name + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        level, exp, money, bank, loss = userInfo(userRow)
        rank = getRank(userRow)
        userNum = checkUserNum()
        print("------------------------------\n")
        embed = discord.Embed(title="유저 정보", description=user.name, color=0x62D0F6)
        embed.add_field(name="레벨", value=level)
        embed.add_field(name="경험치", value=str(exp) + "/" + str(level * level + 6 * level))
        embed.add_field(name="순위", value=str(rank) + "/" + str(userNum))
        embed.add_field(name="보유 자산", value=money, inline=False)
        embed.add_field(name="은행 자산", value=bank, inline=False)
        embed.add_field(name="도박으로 날린 돈", value=loss, inline=False)
        await ctx.send(embed=embed)


@bot.command()
async def bankinfo(ctx):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    if not userExistance:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send(ctx.author.name + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        await ctx.send('현재 은행 자산: ' + str(getbankMoney(ctx.author.name, userRow)))


@bot.command()
async def bank(ctx, inout, money):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    if not userExistance:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send(ctx.author.name + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        if inout == 'in':
            if money == 'all':
                money = str(getMoney(ctx.author.name, userRow))
                print("all -> in")
            if in_bank(ctx.author.name, userRow, money):
                embed = discord.Embed(title="입금 완료", description="입금된 돈: " + money, color=0x0066FF)
                embed.add_field(name="보낸 사람 " + ctx.author.name, value="현재 자산: " + str(getMoney(ctx.author.name, userRow)))
                embed.add_field(name="→", value=":moneybag:")
                embed.add_field(name="은행: " + ctx.author.name, value="남은 자산: " + str(getbankMoney(ctx.author.name, userRow)))
                await ctx.send(embed=embed)
            else:
                await ctx.send('입금량을 다시 확인하세요.')
        elif inout == 'out':
            if money == 'all':
                money = str(getbankMoney(ctx.author.name, userRow))
                print("all -> in")
            if out_bank(ctx.author.name, userRow, money):
                embed = discord.Embed(title="출금 완료", description="출금된 돈: " + money, color=0x0066FF)
                embed.add_field(name="은행", value="남은 자산: " + str(getbankMoney(ctx.author.name, userRow)))
                embed.add_field(name="→", value=":moneybag:")
                embed.add_field(name="받은 사람: " + ctx.author.name, value="현재 자산: " + str(getMoney(ctx.author.name, userRow)))
                await ctx.send(embed=embed)
            else:
                await ctx.send('출금량을 다시 확인하세요.')
        else:
            await ctx.send('in 또는 out을 입력하세요.')


@bot.command()
async def init(ctx):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    if getMoney(ctx.author.name, userRow) != 0 or getbankMoney(ctx.author.name, userRow) != 0:
        await ctx.send("파산상태에서만 가능합니다.")
        return
    if not userExistance:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send(ctx.author.name + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        if getref(userRow):
            iinit(ctx.author.name, userRow)
            await ctx.send("1000000 기본금이 지급되었습니다.")
        else:
            await ctx.send("충전 횟수를 전부 사용하였습니다.")


@bot.command()
async def send(ctx, user: discord.User, money):
    print("송금이 가능한지 확인합니다.")
    senderExistance, senderRow = checkUser(ctx.author.name, ctx.author.id)
    receiverExistance, receiverRow = checkUser(user.name, user.id)
    if money == 'all':
        money = str(getMoney(ctx.author.name, senderRow))
        print("all -> in")
    if int(money) < 100000:
        await ctx.send("100000부터 송금 가능합니다.")
        return
    if not senderExistance:
        print("DB에서", ctx.author.name, "을 찾을수 없습니다")
        print("------------------------------\n")
        await ctx.send("회원가입 후 송금이 가능합니다.")
    elif not receiverExistance:
        print("DB에서 ", user.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send(user.name + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        print("송금하려는 돈: ", money)

        s_money = getMoney(ctx.author.name, senderRow)
        r_money = getMoney(user.name, receiverRow)

        if s_money >= int(money) and int(money) != 0:
            print("돈이 충분하므로 송금을 진행합니다.")
            print("")

            remit(ctx.author.name, senderRow, user.name, receiverRow, money)

            print("송금이 완료되었습니다. 결과를 전송합니다.")

            embed = discord.Embed(title="송금 완료", description="송금된 돈: " + money, color=0xFFFF00)
            embed.add_field(name="보낸 사람: " + ctx.author.name,
                            value="현재 자산: " + str(getMoney(ctx.author.name, senderRow)))
            embed.add_field(name="→", value=":moneybag:")
            embed.add_field(name="받은 사람: " + user.name, value="현재 자산: " + str(getMoney(user.name, receiverRow)))

            await ctx.send(embed=embed)
        elif int(money) == 0:
            await ctx.send("0원을 보낼 필요는 없죠")
        else:
            print("돈이 충분하지 않습니다.")
            print("송금하려는 돈: ", money)
            print("현재 자산: ", s_money)
            await ctx.send("돈이 충분하지 않습니다. 현재 자산: " + str(s_money))

        print("------------------------------\n")


@bot.command()
async def shop(ctx, _cmd, _value):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    if userExistance:
        if _cmd == 'buy':
            # _item = finditem(_value)
            if getMoney(ctx.author.name, userRow) >= 1000000:
                modifyMoney(ctx.author.name, userRow, -1000000)
                addExp(userRow, 20)
                await ctx.send('결제가 완료되었습니다. 경험치가 20오릅니다.')
            else:
                await ctx.send('돈이 충분하지 않습니다.')
    else:
        await ctx.send('회원가입해주세요.')


# =============================== DEV CMD =======================================


@bot.command()
@commands.is_owner()
async def cmd(ctx, _cmd, user: discord.User, _value):
    if _cmd == 'money':
        user, row = checkUser(user.name, user.id)
        addMoney(row, int(_value))
        print("money")
    elif _cmd == 'refill':
        user, row = checkUser(user.name, user.id)
        setrefill(row, int(_value))
        print("refill")
    elif _cmd == 'loss':
        user, row = checkUser(user.name, user.id)
        setloss(row, int(_value))
        print("loss")
    elif _cmd == 'exp':
        user, row = checkUser(user.name, user.id)
        addExp(row, int(_value))
        print("exp")
    elif _cmd == 'level':
        user, row = checkUser(user.name, user.id)
        adjustlvl(row, int(_value))
        print("lvl")
    elif _cmd == 'account':
        if int(_value) == 0:
            print("탈퇴가 가능한지 확인합니다.")
            userExistance, userRow = checkUser(user.name, user.id)
            if userExistance:
                DeleteAccount(userRow)
                print("탈퇴가 완료되었습니다.")
                print("------------------------------\n")
                await ctx.send(user.name + " 탈퇴가 완료되었습니다.")
            else:
                print("DB에서 ", user.name, "을 찾을 수 없습니다")
                print("------------------------------\n")

                await ctx.send("등록되지 않은 사용자입니다.")
        elif int(_value) == 1:
            print("회원가입이 가능한지 확인합니다.")
            userExistance, userRow = checkUser(user.name, user.id)
            if userExistance:
                print("DB에서 ", user.name, "을 찾았습니다.")
                print("------------------------------\n")
                await ctx.send("이미 가입하셨습니다.")
            else:
                print("DB에서 ", user.name, "을 찾을 수 없습니다")
                print("")

                Signup(user.name, user.id)

                print("회원가입이 완료되었습니다.")
                print("------------------------------\n")
                await ctx.send(user.name + " 회원가입이 완료되었습니다.")
        else:
            await ctx.send('_value 값에 0(탈퇴), 1(가입)을 입력하세요')
    else:
        await ctx.send('등록되지 않은 명령어(cmd)')
    await ctx.send('완료되었습니다(cmd/' + _cmd + ')')


@bot.command()
@commands.is_owner()
async def reset(ctx):
    resetData()


# =============================== MUSIC =======================================


@bot.command()
async def leave(ctx):
    await bot.voice_clients[0].disconnect()
    await ctx.send("연결을 종료하였습니다.")


@bot.command()
async def pause(ctx):
    if not bot.voice_clients[0].is_paused():
        bot.voice_clients[0].pause()
    else:
        await ctx.send("플레이 중이 아닙니다.")


@bot.command()
async def resume(ctx):
    if bot.voice_clients[0].is_paused():
        bot.voice_clients[0].resume()
    else:
        await ctx.send("이미 재생중이거나 플레이 중이 아닙니다.")


@bot.command()
async def stop(ctx):
    if bot.voice_clients[0].is_playing():
        bot.voice_clients[0].stop()
    else:
        await ctx.send("재생중이 아닙니다.")


@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    if bot.voice_clients == []:
        await channel.connect()
        await ctx.send("현재 연결한 음성 채널: " + str(bot.voice_clients[0].channel))
    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))


@bot.command()
async def queue(ctx, url):
    mls.append(url)


# =============================== SPECIAL =======================================


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어를 찾지 못했습니다. .sshs 을 입력하여 명령어를 확인하세요.")
    elif isinstance(error, commands.NotOwner):
        await ctx.send('봇 주인만 사용 가능한 명령어입니다')


# =============================== LEVEL =======================================


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "!reset":
        await bot.process_commands(message)
        return
    else:
        userExistance, userRow = checkUser(message.author.name, message.author.id)
        channel = message.channel
        if userExistance:
            levelUp, lvl = levelupCheck(userRow)
            if levelUp:
                print(message.author, "가 레벨업 했습니다")
                print("")
                embed = discord.Embed(title="레벨업", description=None, color=0x00A260)
                embed.set_footer(text=message.author.name + "이 " + str(lvl) + "레벨 달성!")
                await channel.send(embed=embed)
            else:
                modifyExp(userRow, 0.25)
                print("------------------------------\n")

        await bot.process_commands(message)

bot.run(token)
