# Django Permissions & Groups Setup

## Custom Permissions
•⁠  ⁠Added to ⁠ Book ⁠ model:
  - can_view
  - can_create
  - can_edit
  - can_delete

## Groups
•⁠  ⁠*Viewers* → can_view
•⁠  ⁠*Editors* → can_view, can_create, can_edit
•⁠  ⁠*Admins* → can_view, can_create, can_edit, can_delete

## Enforcement
•⁠  ⁠Views use ⁠ @permission_required ⁠ decorators:
  - book_list → requires can_view
  - book_create → requires can_create
  - book_edit → requires can_edit
  - book_delete → requires can_delete

## Testing
1.⁠ ⁠Create users in Admin.
2.⁠ ⁠Assign them to groups.
3.⁠ ⁠Log in and confirm access matches permissions.x