from django.utils import timezone
from django.utils.translation import activate, gettext as _
from telebot import TeleBot
from telebot.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from apps.bot.keyboard import get_main_buttons
from apps.bot.logger import logger
from apps.bot.utils import update_or_create_user
from apps.bot.utils.language import set_language_code
from apps.ticket.models import Concert


def any_user(message: Message, bot: TeleBot):
    try:
        activate(set_language_code(message.from_user.id))
        if message.text.startswith("/start "):
            update_or_create_user(
                telegram_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                is_active=True,
            )
            activate(set_language_code(message.from_user.id))
            logger.info(f"User {message.from_user.id} started the bot.")
            concert_id = message.text.split(" ")[1]
            concert = Concert.objects.get(id=concert_id)
            if concert.is_active and concert.date >= timezone.now().date():
                bot.send_photo(
                    message.chat.id,
                    photo=concert.photo,
                    caption=_(
                        f"{concert.name}\n\n{concert.title}\n\n"
                        f"Sana \ Дата: {concert.date.strftime('%d.%m.%Y')}\nVaqti \ Время: {concert.time.strftime('%H:%M')}\n\n"
                        f"{concert.description}\n\n"
                        f"*📍Manzil \ Адрес:* {concert.address}\n\n"
                        f"[📍Google Xarita \ Карта Google]({concert.location_google_maps})\n[📍Yandex Xarita \ Яндекс Карта]({concert.location_yandex_maps})\n\n"
                        f"*💸Narxlar \ Цены:* {concert.min_price:,} UZS - {concert.max_price:,} UZS\n"
                    ),
                    parse_mode="Markdown",
                    reply_markup=InlineKeyboardMarkup().add(
                        InlineKeyboardButton(
                            _("Buy Tickets"), callback_data=f"buy_ticket_{concert.id}"
                        )
                    ),
                )
            else:
                bot.send_message(message.chat.id, _("This concert is not active."))
        else:
            activate(set_language_code(message.from_user.id))
            update_or_create_user(
                telegram_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                is_active=True,
            )
            logger.info(f"User {message.from_user.id} started the bot.")
            activate(set_language_code(message.from_user.id))
            bot.send_message(
                message.chat.id,
                _(
                    "Welcome to the bot! Use the inline keyboard to search for concerts."
                ),
                reply_markup=get_main_buttons(),
            )
    except Concert.DoesNotExist:
        bot.send_message(message.chat.id, _("Concert not found."))
    except Exception as e:
        bot.send_message(message.chat.id, _("An error occurred."))
        logger.error(f"Error in any_user: {e}")
