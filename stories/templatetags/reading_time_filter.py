from django import template
register = template.Library()


@register.filter(name='reading_time')
def reading_time(value):

    if not isinstance(value, str):
        return 0

    word_count = len(value.split())
    minutes = round(word_count / 200)

    if minutes < 1:
        return "под 1 мин. ⏱️"
    return f"около {minutes} мин. ⏱️"