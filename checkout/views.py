from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SalePaymentForm
import stripe
from .models import Sale, SaleProduct
from products.models import Product
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def charge(request, total_sale_price=None, template_name='charge.html'):

    current_user = request.user

    if request.method == "POST":
        form = SalePaymentForm(
            request.POST,
            cart=request.session.get('cart'),
            total_sale_price=total_sale_price,
            user_id=current_user.id)

        if form.is_valid():  # charges the card

            number = form.cleaned_data['number']
            exp_month = form.cleaned_data['expiration'].month
            exp_year = form.cleaned_data['expiration'].year
            cvc = form.cleaned_data['cvc']

            try:

                token = stripe.Token.create(
                    card={
                        "number": number,
                        "exp_month": exp_month,
                        "exp_year": exp_year,
                        "cvc": cvc
                    },
                )

                charge = stripe.Charge.create(
                    amount=round(float(total_sale_price) * 100),
                    currency='gbp',
                    description='Example charge',
                    source=token.id,
                )

                if charge['paid']:
                    sale = Sale.objects.create(
                        charge_id=charge['id'],
                        price_in_cents=charge['amount'],
                        user_id=form.user_id)

                    for key, value in form.cart.items():
                        SaleProduct.objects.create(
                            sale_id=sale.id, product_id=key, quantity=value)
                        product = Product.objects.get(pk=key)
                        old_total_amount_paid = product.total_amount_paid
                        new_total_amount_paid = (
                            product.total_amount_paid + (product.price*value))
                        Product.objects.filter(id=key).update(
                            total_amount_paid=new_total_amount_paid)

                    messages.add_message(
                        request, messages.SUCCESS, "Success! We've charged your card!")
                    request.session['cart'] = {}
                    return redirect('products')

            except stripe.error.CardError as e:
                # Since it's a decline, stripe.error.CardError will be caught
                body = e.json_body
                err = body.get('error', {})
                messages.add_message(
                    request, messages.ERROR, err.get('message'))

            except stripe.error.RateLimitError as e:
                # Too many requests made to the API too quickly
                body = e.json_body
                err = body.get('error', {})
                messages.add_message(
                    request, messages.ERROR, err.get('message'))

            except stripe.error.InvalidRequestError as e:
                # Invalid parameters were supplied to Stripe's API
                # Since it's a decline, stripe.error.CardError will be caught
                body = e.json_body
                err = body.get('error', {})
                messages.add_message(
                    request, messages.ERROR, err.get('message'))

            except stripe.error.AuthenticationError as e:
                # Authentication with Stripe's API failed
                # (maybe you changed API keys recently)
                # Since it's a decline, stripe.error.CardError will be caught
                body = e.json_body
                err = body.get('error', {})
                messages.add_message(
                    request, messages.ERROR, err.get('message'))

            except stripe.error.APIConnectionError as e:
                # Network communication with Stripe failed
                # Since it's a decline, stripe.error.CardError will be caught
                body = e.json_body
                err = body.get('error', {})
                messages.add_message(
                    request, messages.ERROR, err.get('message'))

            except stripe.error.StripeError as e:
                # Display a very generic error to the user, and maybe send
                # yourself an email
                # Since it's a decline, stripe.error.CardError will be caught
                body = e.json_body
                err = body.get('error', {})
                messages.add_message(
                    request, messages.ERROR, err.get('message'))

            except Exception as e:
                # Something else happened, completely unrelated to Stripe
                # Since it's a decline, stripe.error.CardError will be caught
                body = e.json_body
                err = body.get('error', {})
                messages.add_message(
                    request, messages.ERROR, err.get('message'))

    else:
        form = SalePaymentForm()

    args = {'form': form}
    return render(request, template_name, args)
