from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Menu
from django.urls import reverse
from django.urls import reverse



def index(request):
    return render(request, 'index.html')

def menus(request):
    menu_list = Menu.objects.all()
    return render(request, 'menus.html', {'menu_list': menu_list})

from django.urls import reverse
from django.core.mail import send_mail

def order(request):
    menu_list = Menu.objects.all()
    cart = request.session.get("cart", {})
    total = sum(item["harga"] * item["qty"] for item in cart.values())

    # ADD TO CART
    if request.method == "POST" and "add" in request.POST:
        menu_id = request.POST.get("add")
        menu = Menu.objects.get(id=menu_id)

        if str(menu_id) in cart:
            cart[str(menu_id)]["qty"] += 1
        else:
            cart[str(menu_id)] = {
                "nama": menu.nama,
                "harga": menu.harga,
                "qty": 1
            }

        request.session["cart"] = cart
        return redirect(reverse("order") + "#cart")

    # REMOVE FROM CART
    if request.method == "POST" and "remove" in request.POST:
        menu_id = request.POST.get("remove")

        if str(menu_id) in cart:
            cart[str(menu_id)]["qty"] -= 1

            if cart[str(menu_id)]["qty"] <= 0:
                del cart[str(menu_id)]

        request.session["cart"] = cart
        return redirect(reverse("order") + "#cart")

    # CHECKOUT
    success = False
    if request.method == "POST" and "checkout" in request.POST:
        customer_email = request.POST.get("email")

        ordered_items = [
            f"{item['nama']} x{item['qty']} = Rp{item['harga']*item['qty']:,}"
            for item in cart.values()
        ]

        subject = f"Order Baru dari {customer_email}"
        message = (
            "Pesanan Baru:\n\n"
            + "\n".join(ordered_items)
            + f"\n\nTotal: Rp{total:,}\n"
            + f"\nEmail Customer: {customer_email}\n"
        )

        send_mail(
            subject,
            message,
            "no-reply@lospollos.com",          # from
            ["wagistop78@gmail.com"],          # to
        )

        request.session["cart"] = {}
        success = True

    return render(request, "order.html", {
        "menu_list": menu_list,
        "cart": cart,
        "total": total,
        "success": success
    })
