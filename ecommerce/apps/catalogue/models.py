from os import access
from threading import activeCount

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ecommerce.apps.account.models import Customer
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """
    Category Table implimented with MPTT.
    """

    name = models.CharField(
        verbose_name=_("Nombre de la categoría"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_("URL de la categoría"), max_length=255, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Categoría")
        verbose_name_plural = _("Categorías")

    def get_absolute_url(self):
        return reverse("catalogue:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """
    ProductType Table will provide a list of the different types
    of products that are for sale.
    """

    name = models.CharField(verbose_name=_("Nombre producto"), help_text=_("Requerido"), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Tipo de producto")
        verbose_name_plural = _("Tipos de producto")

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    """
    The Product Specification Table contains product
    specifiction or features for the product types.
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=_("Nombre"), help_text=_("Requerido"), max_length=255)

    class Meta:
        verbose_name = _("Especificación del producto")
        verbose_name_plural = _("Especificaciones del producto")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    The Product table contining all product items.
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(
        verbose_name=_("Título"),	
        help_text=_("Requerido"),
        max_length=255,
    )
    stock = models.PositiveIntegerField(null=True, default=0)
    vendedor = models.CharField(
        verbose_name=_("Nombre vendedor"),	
        help_text=_("Requerido"),
        max_length=50,
        default=""
    )
    description = models.TextField(verbose_name=_("Descripción"), help_text=_("No requerido"), blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.PositiveIntegerField(
        verbose_name=_("Precio normal"),
        help_text=_("Valor por ítem"),
        error_messages={
            "name": {
                "max_length": _("El precio normal debe ser mayor a 0"),
            },
        },
    )
    discount_price = models.PositiveIntegerField(
        verbose_name=_("Discount price"),
        help_text=_("Descuento por ítem"),
        error_messages={
            "name": {
                "max_length": _("El precio normal debe ser mayor a 0"),
            },
        },
    )
    is_active = models.BooleanField(
        verbose_name=_("Visibilidad del producto"),
        help_text=_("Publicado o no publicado"),
        default=True,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_wishlist", blank=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Producto")
        verbose_name_plural = _("Productos")

    def get_absolute_url(self):
        return reverse("catalogue:product_detail", args=[self.slug])

    def __str__(self):
        return self.title


class ProductSpecificationValue(models.Model):
    """
    The Product Specification Value table holds each of the
    products individual specification or bespoke features.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=_("value"),
        help_text=_("Product specification value (maximum of 255 words"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Especificación del producto")
        verbose_name_plural = _("Especificaciones del producto")

    def __str__(self):
        return self.value


class ProductImage(models.Model):
    """
    The Product Image table.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Texto alternativo"),
        help_text=_("Porfavor ingrese un texto alternativo"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Imagen del producto")
        verbose_name_plural = _("Imágenes del producto")
