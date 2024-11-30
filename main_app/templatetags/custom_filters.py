from django import template

register = template.Library()

@register.filter
def topic_id_or_all(topic):
    return topic.id if topic else 'all'
