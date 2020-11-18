from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Permitir que solo los dueños de la subasta puedan modificar
    """
    message= 'No tiene permisos para editar esta subastas'
    metodos=['PUT', 'DELETE']
    def has_object_permission(self, request, view, obj):
        if request.method in self.metodos and  obj.Nombre_Producto.Vendedor == request.user:
            return True        
        return False

        