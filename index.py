import discord
from discord.ext import commands, tasks
import os
import typing
import random
import string
import asyncio
import random
from discord import *
import discord.utils
from itertools import cycle
import datetime
from datetime import datetime
from discord.ext.commands.cooldowns import BucketType


def pretty(number):
	return ("{:,}".format(number))


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(case_insensitive=True,
                      command_prefix="-",
                      intents=intents)  # bot prefix


client.remove_command(
    'help')  # removes the default help msg so it can be reset



@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers | -help | -invite"))
  print('\nOnline.\n')
  global startdate
  startdate = datetime.now()
  





def genCode(length):
	code = ''.join(random.SystemRandom().choice(string.ascii_letters +
	                                            string.digits)
	               for _ in range(length))
	return code


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def nitro(ctx, amount: typing.Optional[int] = 100):
	codeStr = ''
	if amount > 7500:
		amount = 7500
	for x in range(amount):
		if x == amount - 1:
			codeStr += "discord.gift/" + genCode(16)
		else:
			codeStr += "discord.gift/" + genCode(16) + "\n"
		if x == amount - 1:
			name = ''.join(random.SystemRandom().choice(string.ascii_letters +
			                                            string.digits)
			               for _ in range(3)) + "codes.txt"
			f = open(name, "x")
			f.write(codeStr)
			f.close()
			await ctx.author.send(file=discord.File(r'./' + name))
			await ctx.author.send("**__All codes are unchecked__\n**")
			embed = discord.Embed(title="Nitro codes generated",
			                      description="",
			                      color=discord.Colour.green())
			embed.add_field(
			    name=
			    f"{ctx.author}, `{pretty(amount)} nitro codes` were sent to your DMs",
			    value="__All codes are **unchecked**__",
			    inline=False)
			await ctx.send(embed=embed)
			os.remove(name)
			logchannel = await client.fetch_channel('839549309249912842')
			embed = discord.Embed(title="Nitro codes generated",
			                      description="",
			                      color=discord.Colour.purple())
			embed.add_field(name=f"By: {ctx.author}",
			                value=f"Server: {ctx.guild}",
			                inline=False)
			await logchannel.send(embed=embed)


@nitro.error
async def nitro_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		retry_after = int(error.retry_after)
		default_length = 30
		s20 = 840339612672458753  #20s cooldown role id
		s10 = 840339646008655872  # 10s role cooldown id
		n = 840339661292568578  # no cooldown role id
		for role in ctx.message.author.roles:
			if n == role.id:  #no cooldown
				nitro.reset_cooldown(ctx)
				return await ctx.reinvoke()
			if retry_after <= default_length - 10 and s10 == role.id:  # 10s cooldown
				nitro.reset_cooldown(ctx)
				return await ctx.reinvoke()
			if retry_after <= default_length - 20 and s20 == role.id:  # 1m cooldown
				nitro.reset_cooldown(ctx)
				return await ctx.reinvoke()
			else:
				pass

		rA = retry_after
		for role in ctx.message.author.roles:
			if s10 == role.id:
				rA = rA - (default_length - 10)  #10s cooldown
			if s20 == role.id:
				rA = rA - (default_length - 20)  # 20s cooldown

		# retry after msg
		retryAfter = ""
		if int(int(rA) / 60) > 0:
			retryAfter += f"{int(int(rA) / 60)}m "
		if int(rA) - (int(int(rA) / 60) * 60) > 0:
			retryAfter += f"{int(rA) - (int(int(rA) / 60) * 60)}s"
		embed = discord.Embed(
		    title="Cooldown",
		    description=
		    f"This command is on cooldown try again in {retryAfter}",
		    color=discord.Color.red())
		await ctx.send(embed=embed)


# ----- Robux -----
def robuxCode(length):
	s = ''.join(random.SystemRandom().choice(string.digits)
	            for _ in range(length))
	code = ' '.join(s[i:i + 3]
	                for i in range(0, len(s), 3))[::-1].replace(" ", "",
	                                                            1)[::-1]
	return code


@client.command(aliases=["roblox"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def robux(ctx, amount: typing.Optional[int] = 100):
	codeStr = ''
	if amount > 7500:
		amount = 7500
	for x in range(amount):
		codeStr += "" + robuxCode(10) + "\n"
		if x == amount - 1:
			name = ''.join(random.SystemRandom().choice(string.ascii_letters +
			                                            string.digits)
			               for _ in range(3)) + "codes.txt"
			f = open(name, "x")
			f.write(codeStr)
			f.close()
			await ctx.author.send(file=discord.File(r'./' + name))
			await ctx.author.send("**__All codes are unchecked__\n**")
			embed = discord.Embed(title="Nitro codes generated",
			                      description="",
			                      color=discord.Colour.green())
			embed.add_field(
			    name=
			    f"{ctx.author}, `{pretty(amount)} robux codes` were sent to your DMs",
			    value="__All codes are **unchecked**__",
			    inline=False)
			await ctx.send(embed=embed)
			os.remove(name)
			logchannel = await client.fetch_channel('839549309249912842')
			embed = discord.Embed(title="Robux codes generated",
			                      description="",
			                      color=discord.Colour.purple())
			embed.add_field(name=f"By: {ctx.author}",
			                value=f"Server: {ctx.guild}",
			                inline=False)
			await logchannel.send(embed=embed)


@robux.error
async def robux_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		retry_after = int(error.retry_after)
		default_length = 30
		s20 = 840339612672458753  #20s cooldown role id
		s10 = 840339646008655872  # 10s role cooldown id
		n = 840339661292568578  # no cooldown role id
		for role in ctx.message.author.roles:
			if n == role.id:  #no cooldown
				nitro.reset_cooldown(ctx)
				return await ctx.reinvoke()
			if retry_after <= default_length - 10 and s10 == role.id:  # 10s cooldown
				nitro.reset_cooldown(ctx)
				return await ctx.reinvoke()
			if retry_after <= default_length - 20 and s20 == role.id:  # 1m cooldown
				nitro.reset_cooldown(ctx)
				return await ctx.reinvoke()
			else:
				pass

		rA = retry_after
		for role in ctx.message.author.roles:
			if s10 == role.id:
				rA = rA - (default_length - 10)  #10s cooldown
			if s20 == role.id:
				rA = rA - (default_length - 20)  # 20s cooldown

		# retry after msg
		retryAfter = ""
		if int(int(rA) / 60) > 0:
			retryAfter += f"{int(int(rA) / 60)}m "
		if int(rA) - (int(int(rA) / 60) * 60) > 0:
			retryAfter += f"{int(rA) - (int(int(rA) / 60) * 60)}s"
		embed = discord.Embed(
		    title="Cooldown",
		    description=
		    f"This command is on cooldown try again in {retryAfter}",
		    color=discord.Color.red())
		await ctx.send(embed=embed)


# ----- Steam -----
def steamCode(length):
	s = ''.join(random.SystemRandom().choice(string.ascii_letters +
	                                         string.digits)
	            for _ in range(length))
	code = '-'.join(s[i:i + 5] for i in range(0, len(s), 5))
	return code


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def steam(ctx, amount: typing.Optional[int] = 100):
	codeStr = ''
	if amount > 7500:
		amount = 7500
	for x in range(amount):
		codeStr += "" + steamCode(15) + "\n"
		if x == amount - 1:
			name = ''.join(random.SystemRandom().choice(string.ascii_letters +
			                                            string.digits)
			               for _ in range(3)) + "codes.txt"
			f = open(name, "x")
			f.write(codeStr)
			f.close()
			await ctx.author.send(file=discord.File(r'./' + name))
			await ctx.author.send("**__All codes are unchecked__**")
			embed = discord.Embed(title="Nitro codes generated",
			                      description="",
			                      color=discord.Colour.green())
			embed.add_field(
			    name=
			    f"{ctx.author}, `{pretty(amount)} steam codes` were sent to your DMs",
			    value="__All codes are **unchecked**__",
			    inline=False)
			await ctx.send(embed=embed)
			os.remove(name)
			logchannel = await client.fetch_channel('839549309249912842')
			embed = discord.Embed(title="Steam codes generated",
			                      description="",
			                      color=discord.Colour.purple())
			embed.add_field(name=f"By: {ctx.author}",
			                value=f"Server: {ctx.guild}",
			                inline=False)
			await logchannel.send(embed=embed)


@steam.error
async def steam_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		retry_after = int(error.retry_after)
		default_length = 30
		s20 = 840339612672458753  #20s cooldown role id
		s10 = 840339646008655872  # 10s role cooldown id
		n = 840339661292568578  # no cooldown role id
		for role in ctx.message.author.roles:
			if n == role.id:  #no cooldown
				nitro.reset_cooldown(ctx)
				return await ctx.reinvoke()
			if retry_after <= default_length - 10 and s10 == role.id:  # 10s cooldown
				nitro.reset_cooldown(ctx)
				return await ctx.reinvoke()
			if retry_after <= default_length - 20 and s20 == role.id:  # 1m cooldown
				nitro.reset_cooldown(ctx)
				return await ctx.reinvoke()
			else:
				pass

		rA = retry_after
		for role in ctx.message.author.roles:
			if s10 == role.id:
				rA = rA - (default_length - 10)  #10s cooldown
			if s20 == role.id:
				rA = rA - (default_length - 20)  # 20s cooldown

		# retry after msg
		retryAfter = ""
		if int(int(rA) / 60) > 0:
			retryAfter += f"{int(int(rA) / 60)}m "
		if int(rA) - (int(int(rA) / 60) * 60) > 0:
			retryAfter += f"{int(rA) - (int(int(rA) / 60) * 60)}s"
		embed = discord.Embed(
		    title="Cooldown",
		    description=
		    f"This command is on cooldown try again in {retryAfter}",
		    color=discord.Color.red())
		await ctx.send(embed=embed)


# ----- Minecraft -----
@client.command(aliases=['minecraft'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def mc(ctx):
	file = open("mc.txt").read().split('\n')
	rline = file[random.randint(0, len(file) - 1)]
	name = ''.join(
	    random.SystemRandom().choice(string.ascii_letters + string.digits)
	    for _ in range(3)) + "codes.txt"
	f = open(name, "x")
	f.write(rline)
	f.close()
	await ctx.author.send(file=discord.File(r'./' + name))
	await ctx.author.send("**__All codes are unchecked__**")
	embed = discord.Embed(title="Minecraft codes generated",
	                      description="",
	                      color=discord.Colour.green())
	embed.add_field(
	    name=f"{ctx.author}, `1 minecraft account` was sent to your DMs",
	    value="__All codes are **unchecked**__",
	    inline=False)
	await ctx.send(embed=embed)
	os.remove(name)
	logchannel = await client.fetch_channel('839549309249912842')
	embed = discord.Embed(title="Minecraft codes generated",
	                      description="",
	                      color=discord.Colour.purple())
	embed.add_field(name=f"By: {ctx.author}",
	                value=f"Server: {ctx.guild}",
	                inline=False)
	await logchannel.send(embed=embed)


@mc.error
async def mc_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(
		    f"{ctx.author.mention}, you are on cooldown! ({int(error.retry_after)} seconds)"
		)


# ----- ip vanish -----
@client.command(aliases=['ipv', 'vanish'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def ipvanish(ctx):
	file = open("ipvanish.txt").read().split('\n')
	rline = file[random.randint(0, len(file) - 1)]
	name = ''.join(
	    random.SystemRandom().choice(string.ascii_letters + string.digits)
	    for _ in range(3)) + "codes.txt"
	f = open(name, "x")
	f.write(rline)
	f.close()
	await ctx.author.send(file=discord.File(r'./' + name))
	await ctx.author.send("**__All codes are unchecked__**")
	embed = discord.Embed(title="Ipvanish codes generated",
	                      description="",
	                      color=discord.Colour.green())
	embed.add_field(
	    name=f"{ctx.author}, `1 Ipvanish account` was sent to your DMs",
	    value="__All codes are **unchecked**__",
	    inline=False)
	await ctx.send(embed=embed)
	os.remove(name)
	logchannel = await client.fetch_channel('839549309249912842')
	embed = discord.Embed(title="Ipvanish codes generated",
	                      description="",
	                      color=discord.Colour.purple())
	embed.add_field(name=f"By: {ctx.author}",
	                value=f"Server: {ctx.guild}",
	                inline=False)
	await logchannel.send(embed=embed)


@ipvanish.error
async def ipvanish_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(
		    f"{ctx.author.mention}, you are on cooldown! ({int(error.retry_after)} seconds)"
		)


# ----- Hulu -----
@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def hulu(ctx):
	file = open("mc.txt").read().split('\n')
	rline = file[random.randint(0, len(file) - 1)]
	name = ''.join(
	    random.SystemRandom().choice(string.ascii_letters + string.digits)
	    for _ in range(3)) + "codes.txt"
	f = open(name, "x")
	f.write(rline)
	f.close()
	await ctx.author.send(file=discord.File(r'./' + name))
	await ctx.author.send("**__All codes are unchecked__**")
	embed = discord.Embed(title="Hulu accounts generated",
	                      description="",
	                      color=discord.Colour.green())
	embed.add_field(
	    name=f"{ctx.author}, `1 hulu account` was sent to your DMs",
	    value="__All codes are **unchecked**__",
	    inline=False)
	await ctx.send(embed=embed)
	os.remove(name)
	logchannel = await client.fetch_channel('839549309249912842')
	embed = discord.Embed(title="Minecraft codes generated",
	                      description="",
	                      color=discord.Colour.purple())
	embed.add_field(name=f"By: {ctx.author}",
	                value=f"Server: {ctx.guild}",
	                inline=False)
	await logchannel.send(embed=embed)


@hulu.error
async def hulu_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(
		    f"{ctx.author.mention}, you are on cooldown! ({int(error.retry_after)} seconds)"
		)


# ----- Nord -----
@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def nord(ctx):
	file = open("nord.txt").read().split('\n')
	rline = file[random.randint(0, len(file) - 1)]
	name = ''.join(
	    random.SystemRandom().choice(string.ascii_letters + string.digits)
	    for _ in range(3)) + "nord.txt"
	f = open(name, "x")
	f.write(rline)
	f.close()
	await ctx.author.send(file=discord.File(r'./' + name))
	await ctx.author.send("**__All codes are unchecked__**")
	embed = discord.Embed(title="Nord codes generated",
	                      description="",
	                      color=discord.Colour.green())
	embed.add_field(
	    name=f"{ctx.author}, `1 Nord account` was sent to your DMs",
	    value="__All codes are **unchecked**__",
	    inline=False)
	await ctx.send(embed=embed)
	os.remove(name)
	logchannel = await client.fetch_channel('839549309249912842')
	embed = discord.Embed(title="Nord codes generated",
	                      description="",
	                      color=discord.Colour.purple())
	embed.add_field(name=f"By: {ctx.author}",
	                value=f"Server: {ctx.guild}",
	                inline=False)
	await logchannel.send(embed=embed)

@nord.error
async def nord_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(
		    f"{ctx.author.mention}, you are on cooldown! ({int(error.retry_after)} seconds)"
		)



# ----- Nord -----
@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def twitch(ctx):
	file = open("twitch.txt").read().split('\n')
	rline = file[random.randint(0, len(file) - 1)]
	name = ''.join(
	    random.SystemRandom().choice(string.ascii_letters + string.digits)
	    for _ in range(3)) + "twitch.txt"
	f = open(name, "x")
	f.write(rline)
	f.close()
	await ctx.author.send(file=discord.File(r'./' + name))
	await ctx.author.send("**__All codes are unchecked__**")
	embed = discord.Embed(title="Twitch codes generated",
	                      description="",
	                      color=discord.Colour.green())
	embed.add_field(
	    name=f"{ctx.author}, `1 Twitch token` was sent to your DMs",
	    value="__All codes are **unchecked**__",
	    inline=False)
	await ctx.send(embed=embed)
	os.remove(name)
	logchannel = await client.fetch_channel('839549309249912842')
	embed = discord.Embed(title="Twitch codes generated",
	                      description="",
	                      color=discord.Colour.purple())
	embed.add_field(name=f"By: {ctx.author}",
	                value=f"Server: {ctx.guild}",
	                inline=False)
	await logchannel.send(embed=embed)

@nord.error
async def twitch_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(
		    f"{ctx.author.mention}, you are on cooldown! ({int(error.retry_after)} seconds)"
		)


























#help
@client.command(aliases=["h"])
async def help(ctx):
	embed = discord.Embed(title="Help for the bot",
	                      description="Here are all the commands",
	                      color=discord.Colour.purple())
	embed.add_field(name="-gen",
	                value="Shows all the generation commands",
	                inline=True)
	embed.add_field(name="-ping", value="Get the ping of the bot", inline=True)
	embed.add_field(name="-invite",
	                value="Invite the bot to your server",
	                inline=True)
	embed.add_field(
	    name="__All codes are **unchecked**, meaning they don't always work!__",
	    value="redacted",
	    inline=False)
	embed.set_footer(icon_url=ctx.author.avatar_url,
	                 text=f"Requested by {ctx.author.name}")
	await ctx.send(embed=embed)


# gen help
@client.command(aliases=["generate", "g", "stock"])
async def gen(ctx):
	embed = discord.Embed(title="Generation Info",
	                      description="",
	                      color=discord.Colour.purple())
	embed.add_field(name="-nitro <amount **optional**>",
	                value="Generates nitro codes",
	                inline=True)
	embed.add_field(name="-robux <amount **optional**>",
	                value="Generates robux codes",
	                inline=True)
	embed.add_field(name="-steam <amount **optional**>",
	                value="Generates steam codes",
	                inline=True)
	embed.add_field(name="-mc ",
	                value="Generates minecraft accounts",
	                inline=True)
	embed.add_field(name="-hulu ",
	                value="Generates hulu  accounts",
	                inline=True)
	embed.add_field(name="-nord ",
	                value="Generates nord accounts",
	                inline=True)
	embed.add_field(name="-ipvanish ",
	                value="Generates ipvanish accounts",
	                inline=True)
	embed.add_field(name="-twitch",
	                value="Generate a twitch token",
	                inline=True)
	embed.add_field(
	    name="__All codes are **unchecked**, meaning they don't always work!__",
	    value="[Join our support server](https://discord.gg/5AKW2uE8eC)",
	    inline=False)
	embed.set_footer(icon_url=ctx.author.avatar_url,
	                 text=f"Requested by {ctx.author.name}")
	await ctx.send(embed=embed)


# Embed
@client.command(aliases=['e', 'emb'])
@commands.has_permissions(administrator=True)
async def embed(ctx, *, message):
	emb = discord.Embed(title="",
	                    description=message,
	                    color=discord.Colour.blue())
	emb.set_footer(text="")
	await ctx.send(embed=emb)


@embed.error
async def embed_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send(
		    f"{ctx.author.mention}, you don't have permission to use this command!"
		)


#ping
@client.command()
async def ping(ctx):
	embed = discord.Embed(title="Bot ping",
	                      description=f"{round(client.latency * 1000)}ms",
	                      color=discord.Colour.purple())
	await ctx.send(embed=embed)




# invite
@client.command()
async def invite(ctx):
	embed = discord.Embed(color=discord.Colour.purple())
	embed.add_field(
	    name="Invite me to your server!",
	    value=
	    "redacted",
	    inline=False)
	await ctx.send(embed=embed)


# server count
@client.command()
async def servers(ctx):
  servers = list(client.guilds)
  await ctx.send(f"Connected on {str(len(servers))} servers:")


client.run("token")
