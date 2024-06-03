from database.database_models import History


def history_output_func(message):
    output_message = 'История Ваших последних 10 запросов:\n'
    for history in (History.select().order_by(History.datetime.desc())
            .where(History.user_id == message.from_user.id).limit(10)):
        output_message += f'{history.datetime} {history.message}\n'

    return output_message
