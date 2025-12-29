from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Menu
from django.urls import reverse
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect



def index(request):
    return render(request, 'index.html')

def menus(request):
    menu_list = Menu.objects.all()
    return render(request, 'menus.html', {'menu_list': menu_list})

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
        alamat = request.POST.get("alamat")

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
            + f"\nAlamat Pengiriman:\n{alamat}\n"
        )

        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                "no-reply@lospollos.com",          # from
                ["wagistop78@gmail.com"],
                fail_silently=False,        # to
        )
        except Exception as e:
            print("EMAIL ERROR", e);
        

        request.session["cart"] = {}
        success = True

    return render(request, "order.html", {
        "menu_list": menu_list,
        "cart": cart,
        "total": total,
        "success": success
    })

def contact_send(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        send_mail(
            subject="Contact Form - Los Pollos Hermanos",
            message=f"Nama: {name}\nEmail: {email}\nWA: {phone}\n\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

    return redirect("/")  # balik ke index