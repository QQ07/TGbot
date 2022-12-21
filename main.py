from telegram.ext import *
from Responses import *
# from drive import *

print("Bot started")

def start_command(update , context):
    update.message.reply_text('...WELCOME TO PAYROLL MANAGEMENT SYSTEM...')

def help_command(update , context):
    update.message.reply_text('This bot contain many functions:')
    # update.message.reply_text('')
    update.message.reply_text('to execute admin commands type # and then your password\nThen your command to be executed.')
    update.message.reply_text('to view various admin commands click /admin')
    update.message.reply_text('\n\nTo view payroll of any employee: \nPayroll of employee ID')

def admin(update , context):
    update.message.reply_text("#password Add Employee ID Name Base Salary\n#password delete employee ID \n\nSimilarly for taxes and allowances")

def handle_message(update, context):
    text = str(update.message.text)
    response = responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"update caused error {context.error}")

def main():
    updater = Updater("<<API key of our group17 bot>>", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("admin", admin))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()