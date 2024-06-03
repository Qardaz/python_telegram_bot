from datetime import datetime
from database.database_models import History


def history_input_func(message):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    History.create(user_id=message.from_user.id, datetime=date, message=message.text)
