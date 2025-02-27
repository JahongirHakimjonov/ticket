import os

from django.conf import settings
from django.utils.translation import activate, gettext as _
from telebot import TeleBot
from telebot.types import Message

from apps.bot.logger import logger
from apps.bot.utils.language import set_language_code
from apps.ticket.models import BotUsers, Ticket


def handle_all_tickets(message: Message, bot: TeleBot):
    user = BotUsers.objects.get(telegram_id=message.from_user.id)
    orders = Ticket.objects.filter(order__user_id=user.id)
    activate(set_language_code(message.from_user.id))
    if not orders.exists():
        bot.send_message(message.chat.id, _("Sizda hech qanday chipta mavjud emas."))
        return

    for order in orders:
        file_path = os.path.join(settings.MEDIA_ROOT, order.ticket.name)
        logger.info(f"Trying to send ticket to user {user.id}")
        if os.path.exists(file_path):
            text = order.ticket_id
            bot.send_document(message.chat.id, order.ticket, caption=text)
            logger.info(f"All tickets sent to user {user.id}")
        else:
            logger.error(f"File not found: {file_path}")
            bot.send_message(
                message.chat.id, _("Chiptani yuklab bo'lmadi, fayl topilmadi.")
            )
