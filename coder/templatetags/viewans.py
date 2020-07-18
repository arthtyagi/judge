from django import template
from coder.models import Question
register =template.Library()

@register.filter(name='submissions', is_safe=True)
def submissions(question):
    return question.answer_set.all()
