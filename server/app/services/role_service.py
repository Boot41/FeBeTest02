from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=255)
    permissions = models.JSONField()  # Store list of permissions in JSON format

    def __str__(self):
        return self.name

class RoleService:
    @staticmethod
    def get_all_roles():
        return Role.objects.all()

    @staticmethod
    def create_role(name, permissions):
        role = Role(name=name, permissions=permissions)
        role.save()
        return role

    @staticmethod
    def update_role(role_id, name=None, permissions=None):
        role = Role.objects.get(id=role_id)
        if name:
            role.name = name
        if permissions:
            role.permissions = permissions
        role.save()
        return role

    @staticmethod
    def delete_role(role_id):
        role = Role.objects.get(id=role_id)
        role.delete()
        return {'message': 'Role deleted successfully.'}

    @staticmethod
    def get_role_permissions(role_id):
        role = Role.objects.get(id=role_id)
        return role.permissions
