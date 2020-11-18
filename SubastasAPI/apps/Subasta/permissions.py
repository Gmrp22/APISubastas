from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Permitir que solo los dueños del producto puedan crear Subastas
    """
    message= 'No tiene permisos para editar esta subastas'
    metodos=['PUT', 'DELETE']
    def has_object_permission(self, request, view, obj):
        print(obj.Nombre_Producto.Vendedor)
        if request.method in self.metodos and  obj.Nombre_Producto.Vendedor == request.user:
            return True        
        return False