from django.core.exceptions import PermissionDenied,ObjectDoesNotExist
from django.shortcuts import render,redirect
from django.http import Http404
# from django.urls import reverse


class PermissionDeniedCustomHandler:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_exception(self, request, exception):
        if isinstance(exception, PermissionDenied):
            context = {'user': request.user}
            return render(
                request=request,
                template_name='exception_handlers/permission_denied.html/',
                context=context,
                status=403
            )
        return None
    

# class DogObjectDoesNotExistCustomHandler:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
    
#     def process_exception(self, request, exception):
#         if isinstance(exception, ObjectDoesNotExist):
#             print('awd')
#             context = {'user': request.user}
#             return render(
#                 request=request,
#                 template_name='exception_handlers/dog_not_found.html/',
#                 context=context,
#                 status=407
#             )
            # return redirect('permission_denied')
        # return None