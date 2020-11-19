from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Permitir que solo los dueños de la oferta puedan modificarlo
    """
    message = 'No tiene permisos para modificar la oferta'
    metodos = ['PUT', 'DELETE']

    def has_object_permission(self, request, view, obj):
        if request.method in self.metodos and obj.Usuario_oferta == request.user:
            return True
        return False


class SubastaTerminada(BasePermission):
    """
    Permiso para que solo a subastas en espera pueda agregarse
    """
    message = 'Esta subasta ha terminado'
    metodos = ['PUT']

    def has_object_permission(self, request, view, obj):
        print(obj.Subasta.Estado)
        if request.method in self.metodos and obj.Subasta.Estado == 'Espera':
            return True
        return False

