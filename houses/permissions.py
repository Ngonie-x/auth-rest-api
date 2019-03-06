from rest_framework import permissions


# class UpdateOwnHouse(permissions.BasePermission):
#     """Allow users to edit their own house"""

#     def has_object_permission(self, request, view, obj):
#         """Check user is trying to edit their own house"""

#         if request.method in permissions.SAFE_METHODS:
#             return True

#         return obj.user==request.user
        


# class PostOwnHouse(permissions.BasePermission):
#     """Allow users to update their own house"""

#     def has_object_permissions(self, request, view, obj):
#         """checks if the user is trying to update their own house"""

#         #they can view other people's statuses but can't update them
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         return obj.house_model.user == request.user