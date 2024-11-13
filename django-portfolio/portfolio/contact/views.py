#----- contact/views.py -----#
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Contact view that handles form submission and email sending
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Compose the email
        subject = f"New message from {name}"
        message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [from_email]

        try:
            # Send email
            send_mail(subject, message_body, from_email, recipient_list, fail_silently=False)
            # Success message and redirect to the success page
            messages.success(request, "Your message has been sent successfully!")
            return redirect('success')  # Redirect to success page
        except Exception:
            # Error message and redirect back to contact page
            messages.error(request, "There was an error sending your message. Please try again later.")
            return redirect('contact')  # Redirect back to contact form in case of error

    # Render the contact form page
    return render(request, 'contact/contact_form.html')


# Success view that renders the success page after successful form submission
def success_view(request):
    return render(request, 'contact/success.html')
