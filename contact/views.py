from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages


def contact(request):
    """ contact page """

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_message = request.POST['message']

        contact_name = message_name.strip()
        message = message_message.strip()

        if not message:
            saved_name = contact_name
            saved_email = message_email

            messages.error(
                request,
                'Please include a message.'
                )
            return render(request, 'contact/contact.html', {
                'saved_name': saved_name,
                'saved_email': saved_email,
            })

        elif not contact_name:
            saved_email = message_email
            saved_message = message

            messages.error(
                request,
                'Please include your name.'
                )
            return render(request, 'contact/contact.html', {
                'saved_message': saved_message,
                'saved_email': saved_email,
            })

        else:
            send_mail(
                f'Message from {contact_name}',
                message_message,
                message_email,
                ['l.lynch.engineer@gmail.com', ],
                )

        return render(request, 'contact/contact.html', {
            'contact_name': contact_name,
        })

    else:
        return render(request, 'contact/contact.html')
