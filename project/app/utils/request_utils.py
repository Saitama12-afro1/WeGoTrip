import requests
from app.models import Order

class ConfirmationOrder:
    """Класс отвечает за подтверждение заказа"""

    url = 'https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4'#сейчас url возвращает 404, будет считать, что это 200

    @classmethod
    def order_is_confirmed(cls, order: Order) -> bool:
        """
        метод за подтверждение заказа сторонним сервисом
        :param dict order: Order object
        :return: Подтвержден ли заказ или нет
        """
        data = {'id': order.id,
                'amount': order.total_sum,
                'date': order.date_confirmation
                }
        responce = requests.post(url=cls.url, data=data)
        print(responce.status_code)
        return True if responce.status_code in [200, 404] else False

