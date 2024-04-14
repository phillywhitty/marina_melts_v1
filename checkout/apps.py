from django.apps import AppConfig


# Define a configuration class for the 'checkout' app
class CheckoutConfig(AppConfig):
    name = 'checkout'
# Define a method that is executed when the app is ready
    def ready(self):
        # Import signals module to ensure signals are registered
        import checkout.signals
