import unittest
from unittest.mock import patch, MagicMock
from app.models import Role
from app.services import RoleService

class TestRoleService(unittest.TestCase):
    @patch('app.models.Role')
    def test_get_all_roles(self, MockRole):
        mock_role_instance = MagicMock()
        MockRole.objects.all.return_value = [mock_role_instance]
        roles = RoleService.get_all_roles()
        self.assertEqual(roles, [mock_role_instance])
        MockRole.objects.all.assert_called_once()

    @patch('app.models.Role')
    def test_create_role(self, MockRole):
        # Arrange
        MockRole.return_value = MagicMock()
        name = 'Admin'
        permissions = {'read': True, 'write': True}
        
        # Act
        role = RoleService.create_role(name, permissions)
        
        # Assert
        self.assertEqual(role.name, name)
        self.assertEqual(role.permissions, permissions)
        MockRole.return_value.save.assert_called_once()

    @patch('app.models.Role')
    def test_update_role(self, MockRole):
        # Arrange
        mock_role = MagicMock()
        MockRole.objects.get.return_value = mock_role
        role_id = 1
        new_name = 'User'
        new_permissions = {'read': True}
        
        # Act
        updated_role = RoleService.update_role(role_id, new_name, new_permissions)
        
        # Assert
        self.assertEqual(updated_role.name, new_name)
        self.assertEqual(updated_role.permissions, new_permissions)
        mock_role.save.assert_called_once()
    
    @patch('app.models.Role')
    def test_update_role_with_invalid_id(self, MockRole):
        # Arrange
        MockRole.objects.get.side_effect = Role.DoesNotExist
        role_id = 999
        new_name = 'User'
        new_permissions = {'read': True}
        
        # Act & Assert
        with self.assertRaises(Role.DoesNotExist):
            RoleService.update_role(role_id, new_name, new_permissions)

    @patch('app.models.Role')
    def test_delete_role(self, MockRole):
        # Arrange
        mock_role = MagicMock()
        MockRole.objects.get.return_value = mock_role
        role_id = 1
        
        # Act
        response = RoleService.delete_role(role_id)
        
        # Assert
        mock_role.delete.assert_called_once()
        self.assertEqual(response, {'message': 'Role deleted successfully.'})

    @patch('app.models.Role')
    def test_get_role_permissions(self, MockRole):
        # Arrange
        mock_role = MagicMock()
        mock_role.permissions = {'read': True, 'write': True}
        MockRole.objects.get.return_value = mock_role
        role_id = 1

        # Act
        permissions = RoleService.get_role_permissions(role_id)

        # Assert
        self.assertEqual(permissions, {'read': True, 'write': True})

    @patch('app.models.Role')
    def test_get_role_permissions_invalid_id(self, MockRole):
        # Arrange
        MockRole.objects.get.side_effect = Role.DoesNotExist
        role_id = 999

        # Act & Assert
        with self.assertRaises(Role.DoesNotExist):
            RoleService.get_role_permissions(role_id)

if __name__ == '__main__':
    unittest.main()