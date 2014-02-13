from django.shortcuts import render


def home(request):
    """
    Sends the visitor to the homepage

    :param request: http request object
    :return:
    """
    return render(request, template_name='pi.html')
