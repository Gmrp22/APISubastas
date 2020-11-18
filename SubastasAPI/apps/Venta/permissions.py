from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Permitir que solo los dueños de la subasta puedan modificar
    """
    message= 'No tiene permisos para editar esta venta'
    metodos=['PUT', 'DELETE']
    def has_object_permission(self, request, view, obj):
        if request.method in self.metodos and  obj.Subasta.Nombre_Producto.Vendedor == request.user:
            return True        
        return False
    
class IsOwnerOrReadOnlyCreate(BasePermission):
    """
    Permitir que solo los dueños del producto puedan crear subasta
    """
    message= 'No tiene permisos para editar esta venta'
    metodos=['CREATE']
    def has_object_permission(self, request, view, obj):
        print(obj.Vendedor)
        print("*//")
        print(request.user)
        if request.method in self.metodos and  obj.Vendedor == request.user:
            return False        
        return False