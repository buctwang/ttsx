from django.shortcuts import redirect


def is_login(func):
    def wrapper(request, *args, **kwargs):
        try:
            uid = request.session['uid']
        except KeyError:
            return redirect('/user/login/')
        return func(request, *args, **kwargs)
    return wrapper
