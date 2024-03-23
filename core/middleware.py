from django.shortcuts import redirect

class PaymentTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.session.get('payment_in_progress'):
            if not request.session.get_expiry_age() > 0:
                # Payment timed out, redirect to search-account
                del request.session['payment_in_progress']
                return redirect('core:search-account')

        response = self.get_response(request)
        return response
