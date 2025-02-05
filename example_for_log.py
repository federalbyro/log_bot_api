# example_for_log.py
import logging
from logging.handlers import RotatingFileHandler


# Здесь задана глобальная конфигурация для всех логгеров:
logging.basicConfig(
    level=logging.DEBUG,
    filename='program.log', 
    filemode='w',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)

# Здесь установлены настройки логгера для текущего файла — example_for_log.py:
logger = logging.getLogger(__name__)
# Устанавливаем уровень, с которого логи будут сохраняться в файл:
logger.setLevel(logging.INFO)
# Указываем обработчик логов:
handler = RotatingFileHandler('my_logger.log', maxBytes=50000000, backupCount=5)
logger.addHandler(handler)

logger.debug('123')
logger.info('message is not')
logger.warning('big')
logger.error('bot error')
logger.critical('critical')