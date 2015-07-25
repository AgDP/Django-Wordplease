# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class PostPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (GET, POST, PUT o DELETE)
        """
        # Importamos aqui para quitar la dependencia cíclica
        from post.api import PostDetailAPI, PostListAPI
        # si quiere crear un post debede estar autenticado
        if request.method == "POST" and request.user != None :
            return True
        # si no es POST, el superusuario siempre puede
        elif request.user.is_superuser:
            return True
        # si es un GET a la vista de detalle, tomo la decisión en has_object_permissions
        elif isinstance(view, PostListAPI):
            return True
        # si es un PUT a la vista de detalle, tomo la decisión en has_object_permissions
        elif isinstance(view, PostDetailAPI):
            return True
        else:
            # GET a /api/1.0/users/
            return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (GET, PUT o DELETE)
        sobre el object obj
        """
        # si es superadmin, o el usuario autenticado intenta
        # hacer GET, PUT o DELETE sobre su mismo perfil
        return request.user.is_superuser or request.user == obj.blog.owner
