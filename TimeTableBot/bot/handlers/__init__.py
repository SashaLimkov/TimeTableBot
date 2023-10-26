from aiogram import Dispatcher
from aiogram.dispatcher import filters

from . import commands

def setup(dp: Dispatcher):
    dp.register_message_handler(
        commands.echo
    )
    # dp.register_message_handler(
    #     commands.new_user,
    #     filters.CommandStart(),
    #     NotRegistered(),
    #     state="*",
    # )
    # dp.register_message_handler(
    #     commands.old_user,
    #     filters.CommandStart(),
    #     state="*",
    # )
    # dp.register_message_handler(
    #     commands.select_language,
    #     filters.Command("language"),
    #     state="*",
    # )
    # dp.register_message_handler(
    #     commands.set_language,
    #     state=LanguageState.SELECTING,
    # )