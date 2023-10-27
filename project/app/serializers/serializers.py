from rest_framework.serializers import Serializer, ModelSerializer

from app.models import Payment, Product, Order, Status, TypePayment

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class StatusSerializer(ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    status = StatusSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class TypePaymentSerializer(ModelSerializer):
    class Meta:
        model = TypePayment
        fields = '__all__'

class PaymentSerializer(ModelSerializer):
    type_payment= TypePaymentSerializer()

    class Meta:
        model = Payment
        fields = '__all__'
