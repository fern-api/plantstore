import uuid

from plantstore.generated.server import AddPlantRequest
from plantstore.generated.server import ApiAuth
from plantstore.generated.server.resources.plant.service.service import (
    AbstractPlantService,
)


# Here's how you implement your endpoints. Notice there's no networking logic!
# That's all handled by Fern under the hood.
# If you forget to implement any endpoints, you'll get a mypy error when you
# register the server in main.py.
class PlantService(AbstractPlantService):
    def add(self, *, body: AddPlantRequest, auth: ApiAuth) -> None:
        raise RuntimeError("Not implemented")

    def find(self, *, plant_id: uuid.UUID, auth: ApiAuth) -> Plant:
        raise RuntimeError("Not implemented")

    def delete(self, *, plant_id: uuid.UUID, auth: ApiAuth) -> None:
        raise RuntimeError("Not implemented")
