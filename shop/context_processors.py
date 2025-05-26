from .models import Cart

def cart(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_count = cart_items.count()
        cart_total = sum(item.total_price() for item in cart_items)
    else:
        cart_count = 0
        cart_total = 0
    return {
        'cart_count': cart_count,
        'cart_total': cart_total,
    }
