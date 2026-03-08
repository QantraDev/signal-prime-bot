import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

pairs = ["EUR/USD","GBP/USD","USD/JPY","AUD/USD","BTC/USD"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [["📊 Get Signal"]]

    await update.message.reply_text(
        "🚀 Signal Prime+\n\nاضغط للحصول على إشارة.",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    pair = random.choice(pairs)
    direction = random.choice(["⬆️ CALL", "⬇️ PUT"])

    msg = f"""
📊 Trading Signal

Pair: {pair}
Time: 1M
Signal: {direction}

    await update.message.reply_text(msg)

app = ApplicationBuilder().token("8781347026:AAGKmToy2Gln5qlbNkGnCmdJsxxGqb8qAKA").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, signal))

app.run_polling()
