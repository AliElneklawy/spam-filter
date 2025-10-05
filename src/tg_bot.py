import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from inference import predict

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I'm a spam filter bot.\n\n"
        "Send me an email text and I'll tell you if it's spam or not.\n"
        "Just send the email content directly (no command needed)."
    )


async def classify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages (email content)"""
    logger.info("Received classification request")

    email_data = update.message.text

    if not email_data or email_data.strip() == "":
        await update.message.reply_text("Please send me some email text to analyze.")
        return

    try:
        proba, pred = predict(email_data)
        is_spam = pred[0] == 1

        if is_spam:
            confidence = proba
        else:
            confidence = 100 - proba

        logger.info(
            f"Prediction result - is_spam: {is_spam}, confidence: {confidence:.2f}%"
        )

        result_text = "🚨 SPAM" if is_spam else "✅ HAM (Not Spam)"
        await update.message.reply_text(
            f"{result_text}\n"
            f"Confidence: {confidence:.2f}%\n\n"
            f"(Spam probability: {proba:.2f}%)"
        )
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}", exc_info=True)
        await update.message.reply_text(
            f"Sorry, an error occurred while analyzing the email: {str(e)}"
        )


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, classify))

    application.run_polling()


if __name__ == "__main__":
    main()
