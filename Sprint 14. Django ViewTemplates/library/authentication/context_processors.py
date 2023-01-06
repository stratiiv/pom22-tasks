from .models import CustomUser
def auth_context_processor(request):
    username=''
    is_active=False
    for user in CustomUser.objects.all():
        if user.is_active==True:
            username=f'{user.last_name} {user.first_name} {user.middle_name}'
            is_active=user.is_active
            is_admin=True if user.role==1 else False
            break
    return {'username':username,'logged_in':is_active,'is_admin':is_admin}