"""
This code is only made for educational and practice purposes. 
Author and Async Development are not responsible for misuse.

GhoSty OwO Auto HuntBot Farm - A Discord Self-Bot for OwO Farming with HuntBot
Stable Build Version: 00825.0.0.1

GitHub: https://github.com/WannaBeGhoSt
Discord: https://discord.gg/SyMJymrV8x
"""

import os as brutality_ghosty
brutality_ghosty.system("pip install discord.py==1.7.3 colorama requests pillow numpy")

import discord
import json as ghostop
import re
import importlib.util
import asyncio as made_by_ghosty
from datetime import datetime, timedelta
from colorama import Fore, Style, init
from discord.ext import commands

init(autoreset=True)

GhoStyCoreHbSolver = None
GhoStySyncedCaptchaSolve = None
GhoStySolveNormalCap = None
GhoStyHbAlrActiveVar = False
GhoStyHuntbotTimestampJson = "ghostyhbtps.json"

print(
    f"""{Fore.BLUE}

░░░░░░░█░░░░░░░█░░░░███████░░░░░░░░███████░░░░
░░░░░░░█░░░░░░██░░░██░░░░░█░░░░░░░██░░░░░░░░░░░░░█████░░░░█░░░░███░░░░░
░░░░░░░█░░░░░██░░░░█░░░░░██░░░░░░░█░░░░░░█████░░░█░░░█░░░░██░░░█░█░░░░░
░░░░░░██░░░░░█░░░░██░░░███░░░░░░░░█░░░░░░█░░░█░░░█░░░░█░░░███░█░░█░░░░░
░░░░░░████████░░░░█░░████░░░░░░░░█░░░█░░█░░░░█░░█░░░░██░░██░███░░█░░░░░
░░░░░░█░░░░░█░░░░████░░░░█░░░░░░██████░███████░░██████░░░█░░██░░░█░░░░░
░░░░░██░░░░░█░░░░█░░░░░░░█░░░░░░█░░░░░█░░░░░░█░░█░██░░░░██░░░░░░░█░░░░░
░░░░░█░░░░░██░░░██░░░░░░██░░░░░██░░░░░█░░░░░██░█░░░██░░░█░░░░░░░░██░░░░
░░░░░█░░░░░█░░░░█░░░░░░██░░░░░░█░░░░░██░░░░░█░░█░░░░█░░░█░░░░░░░░░█░░░░
░░░░██░░░░░█░░░░██░░███░░░░░░░█░░░░░░█░░░░░░░░░
               ░░████░░░


                                                             Async Development Stable Build Version: 090825.0.0.2 (Patch Fix){Style.RESET_ALL}"""
)

ghostyop = discord.Intents.all()
ghosty = commands.Bot(command_prefix=".", self_bot=True, intents=ghostyop)
ghosty.remove_command("help")

def FetchCoreGhoStySolver():
    global GhoStyCoreHbSolver, GhoStySyncedCaptchaSolve, GhoStySolveNormalCap
    try:
        path = brutality_ghosty.path.join(brutality_ghosty.path.dirname(__file__), "ghostycorehb.py")
        if not brutality_ghosty.path.exists(path):
            print(f"{Fore.RED}❌ GhoSty Core Module Not Found.")
            return False

        spec = importlib.util.spec_from_file_location("corehb", path)
        GhoStyCoreHbSolver = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(GhoStyCoreHbSolver)

        GhoStySolveNormalCap = getattr(GhoStyCoreHbSolver, "GhoStySolveNormalCap", None)
        GhoStySyncedCaptchaSolve = getattr(GhoStyCoreHbSolver, "GhoStySyncedCaptchaSolve", None)

        if GhoStySolveNormalCap and GhoStySyncedCaptchaSolve:
            print(f"{Fore.GREEN}✅ GhoSty Core Module fetched successfully")
            return True
        else:
            print(f"{Fore.RED}❌ GhoSty Core Module functions missing")
            return False
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to Fetch GhoSty Core Module: {e}")
        return False

GhoStyCoreAvailCheck = FetchCoreGhoStySolver()

def ParseGhoStyTimeStrs(time_str):
    time_str = time_str.upper().strip()
    h = int(re.search(r'(\d+)H', time_str).group(1)) if 'H' in time_str else 0
    m = int(re.search(r'(\d+)M', time_str).group(1)) if 'M' in time_str else 0
    return timedelta(hours=h, minutes=m)

def LoadGhoStysHbData():
    try:
        if brutality_ghosty.path.exists(GhoStyHuntbotTimestampJson):
            with open(GhoStyHuntbotTimestampJson, "r") as f:
                return ghostop.load(f)
    except: pass
    return {}

def SaveHbDataGhoStys(data):
    with open(GhoStyHuntbotTimestampJson, "w") as f:
        ghostop.dump(data, f, indent=4)

def GhoStyEmbedParser(msg_content):
    try:
        content = msg_content.lower().replace(",", "")
        match = re.search(r"current max autohunt:.*?for (\d+) cowoncy", content)
        if match:
            return int(match.group(1))
    except: pass
    return 20000 

async def GhoStyCapUrlSolver(url):
    if not GhoStyCoreAvailCheck:
        return None
    try:
        if GhoStySolveNormalCap:
            try: return await GhoStySolveNormalCap(url)
            except: pass
        if GhoStySyncedCaptchaSolve:
            try: return GhoStySyncedCaptchaSolve(url)
            except: pass
    except: pass
    return None

async def GhoStyHbTimerLooped():
    await ghosty.wait_until_ready()
    while not ghosty.is_closed():
        try:
            data = LoadGhoStysHbData()
            if data.get("is_hunting") and "next_huntbot_time" in data:
                next_time = datetime.fromisoformat(data["next_huntbot_time"])
                now = datetime.now()
                if now >= next_time + timedelta(seconds=15):
                    print(f"{Fore.CYAN}⏳ HuntBot time reached! Re-triggering...{Style.RESET_ALL}")
                    channel_id = data.get("channel_id")
                    if channel_id:
                        channel = ghosty.get_channel(int(channel_id))
                        if channel:
                            hunt_stage = data.get("hunt_stage", "normal")
                            
                            if hunt_stage == "waiting_for_return":
                                await channel.send("ohb")
                                print(f"{Fore.GREEN}📤 Auto-sent: ohb (hunt return){Style.RESET_ALL}")
                            else:
                                optimal_cowoncy = data.get("optimal_cowoncy", 20000)
                                await channel.send(f"owo hb {optimal_cowoncy}")
                                print(f"{Fore.GREEN}📤 Auto-sent: owo hb {optimal_cowoncy}{Style.RESET_ALL}")
                            
                            await made_by_ghosty.sleep(4)
                            await GhoStyHbMsgAutoCheck(channel, data.get("optimal_cowoncy", 20000))
                        else:
                            print(f"{Fore.RED}⚠️ Channel ID {channel_id} not found{Style.RESET_ALL}")

                    data["is_hunting"] = False
                    data.pop("next_huntbot_time", None)
                    data.pop("hunt_stage", None)  
                    SaveHbDataGhoStys(data)

            await made_by_ghosty.sleep(30) 
        except Exception as e:
            print(f"{Fore.RED}🔁 HuntBot Timer Error: {e}{Style.RESET_ALL}")
            await made_by_ghosty.sleep(60)

async def GhoStyHbMsgAutoCheck(channel, cowoncy_amount):
    try:
        await made_by_ghosty.sleep(1)
        messages = await channel.history(limit=5).flatten()

        for msg in messages:
            if msg.author.id != 408785106942164992:
                continue

            msg_content = str(msg.content)
            if not msg_content and msg.embeds:
                embed = msg.embeds[0]
                msg_content = (embed.description or "") + "".join(f"{f.name}\n{f.value}" for f in embed.fields)
            msg_content_lower = msg_content.lower()

            if "i will be back in" in msg_content_lower:
                match = re.search(r"i will be back in (\d+h\s*\d*m?|\d+m)", msg_content_lower)
                if match:
                    time_str = match.group(1).strip()
                    delta = ParseGhoStyTimeStrs(time_str)
                    next_time = datetime.now() + delta
                    
                    data = LoadGhoStysHbData()
                    data.update({
                        "next_huntbot_time": next_time.isoformat(),
                        "is_hunting": True,
                        "last_updated": datetime.now().isoformat(),
                        "channel_id": channel.id
                    })
                    SaveHbDataGhoStys(data)
                    
                    print(f"{Fore.GREEN}⏰ Next huntbot in {delta} (at {next_time.strftime('%H:%M:%S')}){Style.RESET_ALL}")
                    return True

            if "here is your password!" in msg_content_lower and msg.attachments:
                url = msg.attachments[0].url
                print(f"{Fore.CYAN}🔍 Solving captcha from {url}{Style.RESET_ALL}")
                result = await GhoStyCapUrlSolver(url)

                if result:
                    await made_by_ghosty.sleep(2)
                    await channel.send(f"owo autohunt {cowoncy_amount} {result}")
                    print(f"{Fore.GREEN} ✅ Auto-solved captcha: `{result}` (Used {cowoncy_amount}){Style.RESET_ALL}")
                    

                    await made_by_ghosty.sleep(4)
                    return await GhoStyHbMsgAutoCheck(channel, cowoncy_amount)
                else:
                    print(f"{Fore.RED} ❌ Failed to solve captcha{Style.RESET_ALL}")
                    return False

            if ("you spent" in msg_content_lower and "cowoncy" in msg_content_lower and 
                "i will be back in" in msg_content_lower):
                match = re.search(r"i will be back in (\d+h\s*\d*m?|\d+m)", msg_content_lower)
                if match:
                    time_str = match.group(1).strip()
                    delta = ParseGhoStyTimeStrs(time_str)
                    next_time = datetime.now() + delta
                    
                    data = LoadGhoStysHbData()
                    data.update({
                        "next_huntbot_time": next_time.isoformat(),
                        "is_hunting": True,
                        "last_updated": datetime.now().isoformat(),
                        "channel_id": channel.id,
                        "hunt_stage": "waiting_for_return" 
                    })
                    SaveHbDataGhoStys(data)
                    
                    print(f"{Fore.GREEN}🎯 Hunt started! Will return in {delta} (at {next_time.strftime('%H:%M:%S')}){Style.RESET_ALL}")
                    return True

            if "i am back with" in msg_content_lower and "animals" in msg_content_lower:
                print(f"{Fore.GREEN}🎉 Hunt completed! Bot is back with loot{Style.RESET_ALL}")
                await made_by_ghosty.sleep(15)
                await channel.send("ohb")
                print(f"{Fore.YELLOW}📤 Sent: ohb (after hunt return){Style.RESET_ALL}")
                await made_by_ghosty.sleep(4)

                messages2 = await channel.history(limit=5).flatten()
                for m2 in messages2:
                    if m2.author.id != 408785106942164992:
                        continue
                    mc2 = str(m2.content)
                    if not mc2 and m2.embeds:
                        emb2 = m2.embeds[0]
                        mc2 = (emb2.description or "") + "".join(f"{f.name}\n{f.value}" for f in emb2.fields)
                    if "beep. boop. i am huntbot" in mc2.lower():
                        optimal_cowoncy = GhoStyEmbedParser(mc2)
                        data = LoadGhoStysHbData()
                        data["optimal_cowoncy"] = optimal_cowoncy
                        SaveHbDataGhoStys(data)
                        await made_by_ghosty.sleep(2)
                        await channel.send(f"owo hb {optimal_cowoncy}")
                        print(f"{Fore.GREEN}📤 Auto-sent: owo hb {optimal_cowoncy}{Style.RESET_ALL}")
                        await made_by_ghosty.sleep(4)
                        return await GhoStyHbMsgAutoCheck(channel, optimal_cowoncy)


        return False
    except Exception as e:
        print(f"{Fore.RED}⚠️ Error in GhoStyHbMsgAutoCheck: {e}{Style.RESET_ALL}")
        return False

async def CheckGhoStyHbMsgFetch(ctx, cowoncy_amount=None):

    global GhoStyHbAlrActiveVar
    try:
        await made_by_ghosty.sleep(1)
        messages = await ctx.channel.history(limit=5).flatten()

        for msg in messages:
            if msg.author.id != 408785106942164992:
                continue

            msg_content = str(msg.content)
            if not msg_content and msg.embeds:
                embed = msg.embeds[0]
                msg_content = (embed.description or "") + "".join(f"{f.name}\n{f.value}" for f in embed.fields)
            msg_content_lower = msg_content.lower()

            if "beep. boop. i am huntbot" in msg_content_lower:
                optimal_cowoncy = GhoStyEmbedParser(msg_content)
                print(f"{Fore.CYAN} HuntBot: Found optimal cowoncy: {optimal_cowoncy}{Style.RESET_ALL}")
                
                data = LoadGhoStysHbData()
                data["optimal_cowoncy"] = optimal_cowoncy
                data["channel_id"] = ctx.channel.id
                SaveHbDataGhoStys(data)
                
                await made_by_ghosty.sleep(2)
                await ctx.send(f"owo hb {optimal_cowoncy}")
                print(f"{Fore.GREEN}📤 Auto-sent: owo hb {optimal_cowoncy}{Style.RESET_ALL}")
                await made_by_ghosty.sleep(4)
                return await CheckGhoStyHbMsgFetch(ctx, optimal_cowoncy)

            if "i will be back in" in msg_content_lower:
                match = re.search(r"i will be back in (\d+h\s*\d*m?|\d+m)", msg_content_lower)
                if match:
                    time_str = match.group(1).strip()
                    delta = ParseGhoStyTimeStrs(time_str)
                    next_time = datetime.now() + delta
                    
                    data = LoadGhoStysHbData()
                    data.update({
                        "next_huntbot_time": next_time.isoformat(),
                        "is_hunting": True,
                        "last_updated": datetime.now().isoformat(),
                        "channel_id": ctx.channel.id
                    })
                    SaveHbDataGhoStys(data)
                    
                    GhoStyHbAlrActiveVar = True
                    print(f"{Fore.GREEN}⏰ Next huntbot in {delta} (at {next_time.strftime('%H:%M:%S')}){Style.RESET_ALL}")
                    await ctx.send(f" ⏰ HuntBot will trigger in {delta}")
                    return True

            if "here is your password!" in msg_content_lower and msg.attachments:
                url = msg.attachments[0].url
                print(f"{Fore.CYAN}🔍 Solving captcha from {url}{Style.RESET_ALL}")
                result = await GhoStyCapUrlSolver(url)

                if result:
                    use_cowoncy = cowoncy_amount or LoadGhoStysHbData().get("optimal_cowoncy", 20000)
                    await made_by_ghosty.sleep(2)
                    await ctx.send(f"owo autohunt {use_cowoncy} {result}")
                    await ctx.send(f"✅ Auto-solved captcha: `{result}` (Used {use_cowoncy})")
                    
                    await made_by_ghosty.sleep(4)
                    return await CheckGhoStyHbMsgFetch(ctx, use_cowoncy)
                else:
                    await ctx.send(" ❌ GhoSty Core Module failed to solve captcha. Please join the support server to get help.")
                    return False

            if ("you spent" in msg_content_lower and "cowoncy" in msg_content_lower and 
                "i will be back in" in msg_content_lower):
                match = re.search(r"i will be back in (\d+h\s*\d*m?|\d+m)", msg_content_lower)
                if match:
                    time_str = match.group(1).strip()
                    delta = ParseGhoStyTimeStrs(time_str)
                    next_time = datetime.now() + delta
                    
                    data = LoadGhoStysHbData()
                    data.update({
                        "next_huntbot_time": next_time.isoformat(),
                        "is_hunting": True,
                        "last_updated": datetime.now().isoformat(),
                        "channel_id": ctx.channel.id,
                        "hunt_stage": "waiting_for_return" 
                    })
                    SaveHbDataGhoStys(data)
                    
                    GhoStyHbAlrActiveVar = True
                    print(f"{Fore.GREEN}🎯 Hunt started Will return in {delta} (at {next_time.strftime('%H:%M:%S')}){Style.RESET_ALL}")
                    await ctx.send(f"🎯 Hunt active Bot will return in {delta}")
                    return True

            if "i am back with" in msg_content_lower and "animals" in msg_content_lower:
                print(f"{Fore.GREEN}Hunt completed Bot is back{Style.RESET_ALL}")
                await ctx.send("Hunt completed Checking stats in 15 seconds...")
                await made_by_ghosty.sleep(15)
                await ctx.send("ohb")
                print(f"{Fore.YELLOW}📤 Sent: ohb (after hunt return){Style.RESET_ALL}")
                await made_by_ghosty.sleep(4)

                messages2 = await ctx.channel.history(limit=5).flatten()
                for m2 in messages2:
                    if m2.author.id != 408785106942164992:
                        continue
                    mc2 = str(m2.content)
                    if not mc2 and m2.embeds:
                        emb2 = m2.embeds[0]
                        mc2 = (emb2.description or "") + "".join(f"{f.name}\n{f.value}" for f in emb2.fields)
                    if "beep. boop. i am huntbot" in mc2.lower():
                        optimal_cowoncy = GhoStyEmbedParser(mc2)
                        data = LoadGhoStysHbData()
                        data["optimal_cowoncy"] = optimal_cowoncy
                        SaveHbDataGhoStys(data)
                        await made_by_ghosty.sleep(2)
                        await ctx.send(f"owo hb {optimal_cowoncy}")
                        print(f"{Fore.GREEN}📤 Auto-sent: owo hb {optimal_cowoncy}{Style.RESET_ALL}")
                        await made_by_ghosty.sleep(4)
                        return await CheckGhoStyHbMsgFetch(ctx, optimal_cowoncy)


        return False
    except Exception as e:
        print(f"{Fore.RED}⚠️ Error in CheckGhoStyHbMsgFetch: {e}{Style.RESET_ALL}")
        return False

@ghosty.command(aliases=["h"])
async def help(ctx):
    ghosty_help = """
# 🤑 GhoSty OwO HuntBot Farm 🤑 
Prefix: `.`

**__Main__**
 🌟 .huntbot: *Starts The AutoBot*
 🔍 .help: *Shows This Message*

**__Features__**
 ⚠ Ban Bypass
 🤖 Auto HuntBot Deploy
 💎 Auto Solve Captcha
 🏹 Fast And Secure

**__Made with 💖 and 🧠 by GhoSty [Async Development]__** 
"""
    await ctx.send(ghosty_help) 

@ghosty.command()
async def huntbot(ctx):
    try:
        await ctx.message.delete()
        await made_by_ghosty.sleep(0.5)
        await ctx.send("owo hb")
        print(f"{Fore.YELLOW}📤 Sent: owo hb{Style.RESET_ALL}")

        data = LoadGhoStysHbData()
        data["channel_id"] = ctx.channel.id
        SaveHbDataGhoStys(data)

        await made_by_ghosty.sleep(4)
        await CheckGhoStyHbMsgFetch(ctx)
    except Exception as e:
        print(f"{Fore.RED}⚠️ Error in .huntbot command: {e}{Style.RESET_ALL}")

@ghosty.event
async def on_ready():
    print(f"{Fore.GREEN}✅ {ghosty.user} is ready!{Style.RESET_ALL}")
    ghosty.loop.create_task(GhoStyHbTimerLooped())
print(f"{Fore.LIGHTRED_EX} > Made By GhoSty [Async Development]{Style.RESET_ALL}")
with open("config.json") as f:
    config = ghostop.load(f)

ghosty.run(config["TOKEN"], bot=False)