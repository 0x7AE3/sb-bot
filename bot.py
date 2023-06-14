import sys
import traceback
import asyncio
import time

import discord
from discord.ext import commands
from discord.ext.commands import BadArgument, MissingRequiredArgument, has_permissions

client = commands.Bot(command_prefix='.')


# async def imp():
#     while True:
#         await asyncio.sleep(30)
#         channel = client.get_channel(749740813554155595)
#         found = False
#         pins = await channel.pins()
#         for message in pins:
#             if 'https://redacted' in message.content:
#                 found = True
#                 break
#         if not found:
#             msg = await channel.send('https://redacted')
#             await msg.pin()
#             await msg.add_reaction('\U0001f44d')


# @client.event
# async def on_ready():
#     print('SB Bot is online!')
#     await imp()


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, BadArgument):
        await ctx.send(f"Please enter a proper arguement for this command, {ctx.author.mention}!")
        # you can also just `ctx.send(f"{error} {ctx.author.mention}")` since the error is more decriptinve
    elif isinstance(error, MissingRequiredArgument):
        await ctx.send("Missing argument in command!")
    else:
        # All other Errors not returned come here. And we can just print the default TraceBack.
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


@client.command()
@commands.has_role('Officer')
async def t(ctx, arg: float):
    await ctx.channel.send(f'Starting timer of {arg} seconds. {ctx.author.mention}')
    if arg > 10:
        await asyncio.sleep(arg - 5)
        await ctx.channel.send(f'5 seconds remaining. {ctx.author.mention}')
    await asyncio.sleep(5)
    await ctx.channel.send(f'{arg} seconds are over. {ctx.author.mention}')


@client.command()
@commands.has_role('Officer')
async def r(ctx):
    await ctx.send("------------------------------------    RESET------------------------------------")


@client.command()
async def stop(ctx):
    return
@client.command()
async def py(ctx):
    if ctx.message.author.id != 686748987029454863: return
    return eval(ctx.message)


client.run('redacted')
