import stripe
from app.core.config import settings

stripe.api_key = settings.stripe_api_key

class PaymentService:
    @staticmethod
    def create_checkout_session(customer_email: str, price_id: str):
        return stripe.checkout.Session.create(
            mode="subscription",
            customer_email=customer_email,
            line_items=[{"price": price_id, "quantity": 1}],
            success_url="https://avantops.ai/success",
            cancel_url="https://avantops.ai/cancel",
        )
