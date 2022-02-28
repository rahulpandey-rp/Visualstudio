from django import template
from store.models import OrderModel

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = OrderModel.objects.filter(user=user, status=False)
        if qs.exists():
            return qs[0].items.count()
    return 0
