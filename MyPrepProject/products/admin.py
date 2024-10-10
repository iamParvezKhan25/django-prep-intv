from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import (
    Category,
    Colour,
    Size,
    DeliveryTime,
    Product,
    SubProduct,
    Stock,
    Images,
)

# Register models with admin interface (customizing titles)
admin.site.register(Category, admin_options={'verbose_name': _('Category'), 'verbose_name_plural': _('Categories')})
admin.site.register(Colour, admin_options={'verbose_name': _('Colour'), 'verbose_name_plural': _('Colours')})
admin.site.register(Size, admin_options={'verbose_name': _('Size'), 'verbose_name_plural': _('Sizes')})
admin.site.register(DeliveryTime, admin_options={'verbose_name': _('Delivery Time'), 'verbose_name_plural': _('Delivery Times')})
admin.site.register(Product, admin_options={'verbose_name': _('Product'), 'verbose_name_plural': _('Products')})
admin.site.register(SubProduct, admin_options={'verbose_name': _('Sub Product'), 'verbose_name_plural': _('Sub Products')})
admin.site.register(Stock, admin_options={'verbose_name': _('Stock'), 'verbose_name_plural': _('Stocks')})
admin.site.register(Images, admin_options={'verbose_name': _('Image'), 'verbose_name_plural': _('Images')})