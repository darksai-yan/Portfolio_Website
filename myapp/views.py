from django.shortcuts import render

from myapp.models import ArtWork
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm
import json
import os
from django.shortcuts import render


# Create your views here.
class MainPage(ListView):
    model = ArtWork
    template_name = 'myapp/artwork_list.html'
    context_object_name = 'artworks'
    def get_queryset(self):
        return ArtWork.objects.filter(
            is_best=True
        ).order_by('-date_created')


def contact_ajax_view(request):
    if request.method == 'POST':
        try:
            # Читаємо дані, які прийшли через fetch (JSON)
            data = json.loads(request.body)
            form = ContactForm(data)

            if form.is_valid():
                name = form.cleaned_data['name']
                user_email = form.cleaned_data['email']
                message = form.cleaned_data['message']

                # Формуємо лист
                subject = f'New inquiry from portfolio by {name}'
                body = f"Name: {name}\nEmail: {user_email}\n\nMessage:\n{message}"

                email = EmailMessage(
                    subject=subject,
                    body=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[os.getenv('ADMIN_EMAIL')],  # Твоя пошта
                    reply_to=[user_email],  # Щоб ти міг легко натиснути "Відповісти"
                )
                email.send(fail_silently=False)

                subject_to_user = "Thank you for your message!"
                body_to_user = f"Hello, {name}!\n\nThank you for your message. I will review it and get back to you as soon as possible.\n\nBest regards,\nYan"

                user_reply = EmailMessage(
                    subject=subject_to_user,
                    body=body_to_user,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[user_email],  # Пошта клієнта, яку він вписав у форму
                )
                user_reply.send(fail_silently=False)

                return JsonResponse({'success': True, 'message': 'Message sent successfully! Thank you.'})
            else:
                # Якщо валідація не пройшла (наприклад, кривий email)
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
                
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Invalid method'}, status=405)




def privacy_view(request):
    return render(request, 'myapp/privacy.html')