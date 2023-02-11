import uuid

from plantstore.generated.server import AddOwnerRequest
from plantstore.generated.server import ApiAuth
from plantstore.generated.server import PlantOwner
from plantstore.generated.server.resources.owner.service.service import (
    AbstractOwnerService,
)


# Here's how you implement your endpoints. Notice there's no networking logic!
# That's all handled by Fern under the hood.
# If you forget to implement any endpoints, you'll get a mypy error when you
# register the server in main.py.
class OwnerService(AbstractOwnerService):
    def add(self, *, body: AddOwnerRequest, auth: ApiAuth) -> PlantOwner:
        raise RuntimeError("Not implemented")

    def delete(self, *, owner_id: uuid.UUID, auth: ApiAuth) -> None:
        raise RuntimeError("Not implemented")
