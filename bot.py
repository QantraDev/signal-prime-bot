from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8781347026:AAGKmToy2Gln5qlbNkGnCmdJsxxGqb8qAKA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to Signal Prime+\n\n"
        "📈 Free Trading Signals\n"
        "💰 Register and start trading!\n\n"
        "Use /signal to get a signal"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 SIGNAL\n\n"
        "Pair: EUR/USD\n"
        "Direction: CALL 📈\n"
        "Time: 1 Minute"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

print("Bot running...")

app.run_polling()
