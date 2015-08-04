# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class BlogPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (GET, POST, PUT o DELETE)
        """
        # Importamos aqui para quitar la dependencia cíclica
        from blog.api import BlogListAPI
        # si quiere crear un post debede estar autenticado
        if request.method == "POST" and request.user.id != None and request.user.id == request.data.get('owner'):
            return True
        # si no es POST, el superusuario siempre puede
        elif request.user.is_superuser:
            return True
        # si es un GET a la vista de detalle, tomo la decisión en has_object_permissions
        elif request.method == "GET":
            return True
        else:
            # GET a /api/1.0/blogs/
            return False