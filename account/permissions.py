from rest_framework.permissions import BasePermission, IsAdminUser

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the authenticated user has the role attribute
        return getattr(request.user, 'role', None) == 'student'


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return getattr(request.user,'role',None)=='teacher'
        
class IsAdminOrTeacher(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        # Check if the user is an admin user
        if IsAdminUser().has_permission(request, view):
            return True
        # Check if the user has the role of teacher
        return getattr(request.user, 'role', None) == 'teacher'

