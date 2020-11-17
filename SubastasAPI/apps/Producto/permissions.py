from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BaseException):
    """Permiso para que solo el dueño pueda editar"""
    metodos=['PUT']
    mensaje='No tiene permisos'
    def has_permission(self, request, view):
        if request.method in self.metodos:
            return True
        return False


    def has_object_permission(self, request, view, obj):
        if request.method in self.metodos:
            return True
        return obj.user == request.user