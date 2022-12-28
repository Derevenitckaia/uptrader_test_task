from django import template
from menu.models import MenuItem
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('list_menus.html', takes_context=True)
def draw_menu(context, menu_name):

    items = MenuItem.objects.filter(cat__name=menu_name).filter(parent=None)

    request_path = context['request'].path
    request_path = request_path[1:]

    local_context = {'items': items,
                     'menu_name': menu_name,
                     }

    try:
        active_item = MenuItem.objects.get(id=request_path)
    except ObjectDoesNotExist:
        pass
    else:
        ancestor_active_item_ids = active_item.get_ancestor_ids() + [active_item.id]
        local_context['ancestor_active_item_ids'] = ancestor_active_item_ids

    return local_context


@register.inclusion_tag('list_items.html', takes_context=True)
def draw_items(context, item_id):

    childrens = MenuItem.objects.filter(parent=item_id)
    local_context = {'childrens': childrens,
                     'ancestor_active_item_ids': '', 
                     }

    if 'ancestor_active_item_ids' in context:
        local_context['ancestor_active_item_ids'] = context['ancestor_active_item_ids']

    return local_context

