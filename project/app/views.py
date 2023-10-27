from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView, View
from rest_framework.viewsets import ViewSet
from django.db import transaction

from app.models import Payment, Product, Order
from app.serializers.serializers import ProductSerializer, OrderSerializer, PaymentSerializer

class ProductView(APIView):

    @transaction.atomic
    def get(self, request):
        products: list[Product] = Product.objects.all()
        print(products)
        serialized_data = ProductSerializer(products, many=True)
        return Response(serialized_data.data)

class OrderView(APIView):
    
    @transaction.atomic
    def post(self, request):
        products_id = [id['id'] for id in request.data]
        products = Product.objects.filter(id__in=products_id)
        if not products:
            return Response(status=418, data={'message': 'Products not found'})
        price_products = 0
        for product in products:
            price_products += product.price
        order = Order.objects.create(total_sum = price_products)
        ser = OrderSerializer(order)
        return Response(ser.data)


class PaymentView(APIView):

    @transaction.atomic
    def post(self, request):
        order_id = request.data['id']
        if not (order:= Order.objects.filter(id=order_id).last()):
            return Response(status=418, data={'message': f'Not find order with {order_id=}'})
        order = Order.objects.get(id=request.data['id'])
        payment = Payment.objects.create(amount = order.total_sum, order=order)
        ser = PaymentSerializer(payment)
        return Response(ser.data)
        

    


    

