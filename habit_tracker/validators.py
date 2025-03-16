from datetime import timedelta

from rest_framework.serializers import ValidationError


class HabitValidators:

    def __call__(self, value):
        value = dict(value)
        if value.get("complete_time") > timedelta(seconds=120):
            raise ValidationError("Время выполнения привычки не может составлять больше 2-х минут !")

        elif int(value.get("period")) < 1 or int(value.get("period")) > 7:
            raise ValidationError("Внимание! Выполнять привычку нужно не реже чем 1 раз в 7 дней!")

        elif value.get("nice_habit") is False and not value.get("award") and not value.get("associated_habit"):
            raise ValidationError(
                "У полезной привычки необходимо заполнить одно из полей: "
                "'Вознаграждение' или 'Связанная привычка'! "
            )

        elif value.get("nice_habit") is False and value.get("award") and value.get("associated_habit"):
            raise ValidationError(
                "У полезной привычки необходимо заполнить только одно из полей:"
                "'Вознаграждение' или 'Связанная привычка'!"
            )

        elif value.get("nice_habit") is True and value.get("associated_habit"):
            raise ValidationError("У приятной привычки не может быть связанной привычки!")

        elif value.get("nice_habit") is True and value.get("award"):
            raise ValidationError("У приятной привычки не может быть вознаграждения!")
