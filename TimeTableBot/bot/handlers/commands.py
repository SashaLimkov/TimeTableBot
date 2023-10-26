import asyncio
from aiogram import types
from bot.config.loader import bot


async def echo(message:types.Message):
    await message.reply(
        text=message.text,
        reply=False
    )