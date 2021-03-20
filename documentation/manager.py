from safedelete.models import SafeDeleteModel
from safedelete.managers import SafeDeleteManager
from safedelete import DELETED_VISIBLE_BY_PK

class MyModelManager(SafeDeleteManager):
    _safedelete_visibility = DELETED_VISIBLE_BY_PK