import telebot
from apscheduler.schedulers.background import BackgroundScheduler
import time
import os
from datetime import datetime
import logging
from dotenv import load_dotenv
import pytz
from apscheduler.triggers.cron import CronTrigger

# Configuração básica de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[logging.FileHandler('bot.log')]
)
logger = logging.getLogger(__name__)

# Carrega variáveis de ambiente
load_dotenv()

# Configurações do bot
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
SCHEDULE_HOUR = int(os.getenv('SCHEDULE_HOUR'))
SCHEDULE_MINUTE = int(os.getenv('SCHEDULE_MINUTE'))

# Configuração do fuso horário
TIMEZONE = pytz.timezone('America/Sao_Paulo')

if not TOKEN:
    logger.error("Token do bot não configurado")
    exit(1)

bot = telebot.TeleBot(TOKEN)
scheduler = None

def send_scheduled_message():
    """Envia a mensagem agendada"""
    if not CHAT_ID:
        logger.error("CHAT_ID não configurado")
        return

    try:
        current_time = datetime.now(TIMEZONE)
        logger.info(f"Enviando mensagem agendada às {current_time.strftime('%H:%M:%S')}")
        
        # Separa os IDs por vírgula e remove espaços em branco
        chat_ids = [id.strip() for id in CHAT_ID.split(',')]
        
        # Envia a mensagem para cada ID
        for chat_id in chat_ids:
            try:
                bot.send_message(chat_id, f"Hello World - Horário atual: {current_time.strftime('%H:%M:%S')}")
                logger.info(f"Mensagem enviada com sucesso para o chat_id: {chat_id}")
            except Exception as e:
                logger.error(f"Erro ao enviar mensagem para o chat_id {chat_id}: {str(e)}")
                
    except Exception as e:
        logger.error(f"Erro ao processar envio de mensagens: {str(e)}")

def main():
    try:
        logger.info("Iniciando bot...")
        
        # Verifica conexão do bot
        bot_info = bot.get_me()
        logger.info(f"Bot conectado: {bot_info.username}")

        # Configura o scheduler
        scheduler = BackgroundScheduler()
        
        # Adiciona o job com o horário do .env
        scheduler.add_job(
            send_scheduled_message,
            trigger=CronTrigger(
                hour=SCHEDULE_HOUR,
                minute=SCHEDULE_MINUTE,
                timezone=TIMEZONE
            ),
            id='send_message',
            name='Enviar mensagem diária',
            replace_existing=True
        )
        
        scheduler.start()
        logger.info(f"Mensagem agendada para {SCHEDULE_HOUR:02d}:{SCHEDULE_MINUTE:02d} (horário de São Paulo)")
        
        # Inicia o polling
        bot.polling(none_stop=True)
        
    except Exception as e:
        logger.error(f"Erro no bot: {str(e)}")
    finally:
        if scheduler:
            scheduler.shutdown()
        logger.info("Bot encerrado")

if __name__ == "__main__":
    main()