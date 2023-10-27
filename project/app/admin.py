import time
from typing import Any

from django.contrib.admin import ModelAdmin, register, StackedInline, TabularInline, action
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.utils import timezone
from django.db import transaction
import requests

from app.models import Product, Payment, Order, Status, TypePayment
from app.utils.request_utils import ConfirmationOrder

@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name','picture',
                    'content','price')
    


@register(Status)
class StatusAdmin(ModelAdmin):
    list_display = ('status', )

@register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ('total_sum', 'date_create', 'date_confirmation', 'status')
    fields = ('total_sum', 'date_create', 'date_confirmation', 'status')
    readonly_fields = ('date_create',)
    change_form_template = 'app/admin/change_form.html'
    
    @transaction.atomic
    def changeform_view(self, request, object_id, form_url, extra_context) -> Any:
        extra_context  = extra_context if extra_context else {}
        from app.models import Payment as Paym
        #проверяем есть ли Платеж у Текущего объекта Заказа
        if Paym.objects.filter(order__id=object_id).exists():
            #проверяем статуc Платежа
            extra_context['visible_custom_button'] = Paym.objects.get(order__id=object_id).status.status == 'Оплачен'
        else:
            extra_context['visible_custom_button'] = False
        return super().changeform_view(request, object_id, form_url, extra_context)
    
    @transaction.atomic
    def response_change(self, request, obj):
        if "_customaction" in request.POST:
            # обрабатываем логику кнопки подтверждения заказа
            obj.date_confirmation = timezone.now()
            is_confirmed = ConfirmationOrder.order_is_confirmed(obj)
            time.sleep(3)
            if is_confirmed:
                status, _ = Status.objects.get_or_create(status='Подтвержден', defaults={'status':'Подтвержден'})
                obj.status = status
                obj.save()
        return super().response_change(request, obj)

@register(TypePayment)
class TypePaymentAdmin(ModelAdmin):
    list_display = ('type_payment',)

@register(Payment)
class Payment(ModelAdmin):
    list_display = ('amount','status','type_payment',)


