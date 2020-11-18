from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Permitir que solo los dueños de la oferta puedan modificarlo
    """
    message= 'No tiene permisos para modificar la oferta'
    metodos=['PUT', 'DELETE']
    def has_object_permission(self, request, view, obj):
        if request.method in self.metodos and  obj.Usuario_oferta == request.user:
            return True
        return False

