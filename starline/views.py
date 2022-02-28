from django.shortcuts import render

# Create your views here.
from django.template import context
from django.views.generic import ListView

# from starline.forms import UserLoginForm
from starline.models import Contacts, Feedback


def contact(request):
    contacts = Contacts.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(request, template_name='contacts.html', context=context)


def feedb(request):
    feedback = Feedback.objects.all()
    context = {
        'feedback': feedback,
    }
    return render(request, template_name='feedback.html', context=context)




# def get_login(request):
#     if request.method == 'POST':
#         user_form = UserLoginForm(data=request.POST)
#         if user_form.is_valid():
#             user = user_form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         user_form = UserLoginForm
#     context = {
#         'title': 'Войти в систему',
#         'style': style,
#         'author': author,
#         'user_form': user_form
#         }
#     return render(request, 'login.html', context=context)
