import time

from django.db import DatabaseError

from apps.payme.utils.logging import logger
from apps.payme.utils.get_params import get_params
from apps.payme.models import MerchantTransactionsModel
from apps.payme.serializers import MerchantTransactionsModelSerializer


class PerformTransaction:
    """
    PerformTransaction class
    That's used to perform a transaction.

    Full method documentation
    -------------------------
    https://developer.help.paycom.uz/metody-merchant-api/performtransaction
    """

    def __call__(self, params: dict) -> tuple:
        serializer = MerchantTransactionsModelSerializer(data=get_params(params))
        serializer.is_valid(raise_exception=True)
        clean_data: dict = serializer.validated_data
        response: dict = None
        try:
            transaction = MerchantTransactionsModel.objects.get(
                _id=clean_data.get("_id"),
            )
            transaction.state = 2
            if transaction.perform_time == 0:
                transaction.perform_time = int(time.time() * 1000)

            transaction.save()
            response: dict = {
                "result": {
                    "perform_time": int(transaction.perform_time),
                    "transaction": transaction.transaction_id,
                    "state": int(transaction.state),
                }
            }
        except DatabaseError as error:
            logger.error("error while getting transaction in db: %s", error)

        return transaction.order_id, response
