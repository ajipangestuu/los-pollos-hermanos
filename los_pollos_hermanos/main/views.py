from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Menu

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def order(request):
    menu_list = Menu.objects.all()
    cart = request.session.get("cart", {})
    total = sum(item["harga"] * item["qty"] for item in cart.values())

    # tambah item ke cart
    if request.method == "POST" and "add" in request.POST:
        menu_id = request.POST.get("add")
        menu = Menu.objects.get(id=menu_id)
        if str(menu_id) in cart:
            cart[str(menu_id)]["qty"] += 1
        else:
            cart[str(menu_id)] = {"nama": menu.nama, "harga": menu.harga, "qty": 1}
        request.session["cart"] = cart
        return redirect("order")

    # hapus item dari cart
    if request.method == "POST" and "remove" in request.POST:
        menu_id = request.POST.get("remove")
        if str(menu_id) in cart:
            del cart[str(menu_id)]
        request.session["cart"] = cart
        return redirect("order")

    # checkout
    success = False
    if request.method == "POST" and "checkout" in request.POST:
        customer_email = request.POST.get("email")
        ordered_items = [
            f"{item['nama']} x{item['qty']} = Rp{item['harga']*item['qty']:,}"
            for item in cart.values()
        ]
        subject = f"Order Baru dari {customer_email}"
        message = "Pesanan Baru:\n\n" + "\n".join(ordered_items) + f"\n\nTotal: Rp{total:,}\n"
        send_mail(subject, message, customer_email, ["email_staff@lospollos.com"])
        request.session["cart"] = {}
        success = True

    return render(request, "order.html", {
        "menu_list": menu_list,
        "cart": cart,
        "total": total,
        "success": success
    })
def contact(request):
    return render(request, 'contact.html')
