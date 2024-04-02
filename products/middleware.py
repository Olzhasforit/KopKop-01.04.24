from django.shortcuts import redirect
from django.urls import reverse

class AdminAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Проверяем, что пользователь аутентифицирован и имеет доступ к админ-панели
        if not request.user.is_authenticated and request.path.startswith('/admin/'):
            # Если пользователь не аутентифицирован, перенаправляем его на страницу входа
            return redirect(reverse('admin:login'))

        # Возвращаем результат вызова get_response
        return self.get_response(request)

