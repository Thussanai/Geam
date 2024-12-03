import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

from myserver import server_on

# โหลด environment variables จากไฟล์ .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# ตั้งค่าการเข้าถึงข้อความของบอท
intents = discord.Intents.default()
intents.message_content = True  # เพื่อให้บอทสามารถอ่านข้อความได้

bot = commands.Bot(command_prefix='!', intents=intents)

# ส่วนที่หนึ่ง: เมื่อบอทพร้อมทำงาน
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# ส่วนที่สอง: เริ่มเกม
@bot.command(name='start')
async def start_game(ctx):
    await ctx.send('Welcome to Realm of Echoes!')
    # เริ่มต้นการเลือกดินแดน
    await ctx.send('Choose your starting zone: 1. Forest of Ancients 2. Desert of Desolation 3. Frost Peaks')

# ส่วนที่สาม: การต่อสู้
@bot.command(name='attack')
async def attack(ctx):
    damage = 10  # ค่าความเสียหายตัวอย่าง
    await ctx.send(f'{ctx.author} attacked and dealt {damage} damage!')

@bot.command(name='defend')
async def defend(ctx):
    await ctx.send(f'{ctx.author} is defending and reduces damage by 50%!')

@bot.command(name='use_skill')
async def use_skill(ctx, skill: str):
    if skill.lower() == 'fireball':
        damage = 20  # ค่าความเสียหายจากสกิล Fireball
        await ctx.send(f'{ctx.author} used Fireball and dealt {damage} damage!')
    else:
        await ctx.send(f'The skill {skill} is not recognized.')

# ส่วนที่สี่: ระบบดินแดนและศัตรู
@bot.command(name='start_forest')
async def start_forest(ctx):
    await ctx.send('You have entered the Forest of Ancients.')

@bot.command(name='encounter')
async def encounter(ctx):
    enemy = 'Glacial Seraphim'  # ศัตรูตัวอย่าง
    await ctx.send(f'You encountered a {enemy}!')

@bot.command(name='equip_sword')
async def equip_sword(ctx):
    sword = 'Flame Sword'  # ตัวอย่างอาวุธ
    await ctx.send(f'{ctx.author} equipped a {sword}.')

# เรียกใช้เซิร์ฟเวอร์ Flask
server_on()

# เริ่มบอท
bot.run(TOKEN)
