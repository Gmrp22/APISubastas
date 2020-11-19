from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Permitir que solo los dueños del producto puedan modificarlo o borrarlo
    """
    message = 'No tiene permisos para modificar el producto'
    metodos = ['PUT', 'DELETE']

    def has_object_permission(self, request, view, obj):
        if request.method in self.metodos and obj.Vendedor == request.user:
            return True
        return False
