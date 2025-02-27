from django.utils.translation import activate, gettext as _
from telebot import TeleBot
from telebot.types import (
    CallbackQuery,
)

from apps.bot.handlers.buy_ticket import handle_buy_ticket_callback
from apps.bot.handlers.donate import handle_cancel, handle_donation
from apps.bot.handlers.language import handle_language_selection
from apps.bot.handlers.payme import handle_payme_callback
from apps.bot.handlers.select_count import (
    handle_select_count_callback,
    handle_confirm_selection,
    handle_setnumber_selection,
)
from apps.bot.handlers.select_seat import handle_select_seat_callback
from apps.bot.logger import logger
from apps.bot.utils.language import set_language_code


def handle_callback_query(call: CallbackQuery, bot: TeleBot):
    activate(set_language_code(call.from_user.id))
    if call.data.startswith("buy_ticket_"):
        handle_buy_ticket_callback(call, bot)
        logger.info(f"User {call.from_user.id} selected a concert.")
    elif call.data.startswith("select_seat_"):
        handle_select_seat_callback(call, bot)
        logger.info(f"User {call.from_user.id} selected a seat.")
    elif call.data.startswith("select_count_"):
        handle_select_count_callback(call, bot)
        logger.info(f"User {call.from_user.id} selected a count.")
    elif call.data == "noop":
        bot.answer_callback_query(call.id, _("Qatorni tanlang"))
        logger.info(f"User {call.from_user.id} selected no operation.")
    elif call.data == "seat":
        bot.answer_callback_query(call.id, _("O'rindiqni tanlang"))
        logger.info(f"User {call.from_user.id} selected a seat.")
    elif call.data == "select_payment":
        bot.answer_callback_query(call.id, _("To'lov turini tanlang"))
        logger.info(f"User {call.from_user.id} selected a payment method.")
    elif call.data == "choice_type":
        bot.answer_callback_query(call.id, _("Joylashuvni tanlang"))
        logger.info(f"User {call.from_user.id} selected a seat type.")
    elif call.data.startswith("payme_"):
        handle_payme_callback(call, bot)
        logger.info(f"User {call.from_user.id} selected PayMe.")
    elif call.data == "payme_checked":
        bot.answer_callback_query(call.id, _("PayMe tanlandi."))
        logger.info(f"User {call.from_user.id} selected PayMe.")
    elif call.data == "cancel":
        handle_cancel(call, bot)
        logger.info(f"User {call.from_user.id} cancelled the operation.")
    elif call.data.isdigit():
        handle_donation(call, bot)
        logger.info(f"User {call.from_user.id} donated.")
    elif call.data == "lang_ru" or call.data == "lang_uz":
        handle_language_selection(call, bot)
        logger.info(f"User {call.from_user.id} selected a language.")
    elif call.data.startswith("select_setnumber_"):
        handle_setnumber_selection(call, bot)
        logger.info(f"User {call.from_user.id} selected a set number.")
    elif call.data.startswith("confirm_"):
        handle_confirm_selection(call, bot)
        logger.info(f"User {call.from_user.id} confirmed the selection.")
    else:
        bot.answer_callback_query(call.id, _("Unknown action."))
        logger.info(f"User {call.from_user.id} performed an unknown action.")
