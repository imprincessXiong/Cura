# Copyright (c) 2018 Ultimaker B.V.
# Cura is released under the terms of the LGPLv3 or higher.
from UM import i18nCatalog
from UM.Message import Message


## Class that contains all the translations for this module.
class T:
    _I18N_CATALOG = i18nCatalog("cura")

    SENDING_DATA_TEXT = _I18N_CATALOG.i18nc("@info:status", "Sending data to remote cluster")
    SENDING_DATA_TITLE = _I18N_CATALOG.i18nc("@info:status", "Sending data to remote cluster")


## Class responsible for showing a progress message while a mesh is being uploaded to the cloud.
class CloudProgressMessage(Message):
    def __init__(self):
        super().__init__(
            text = T.SENDING_DATA_TEXT,
            title = T.SENDING_DATA_TITLE,
            progress = -1,
            lifetime = 0,
            dismissable = False,
            use_inactivity_timer = False
        )

    ## Shows the progress message.
    def show(self):
        self.setProgress(0)
        super().show()

    ## Updates the percentage of the uploaded.
    #  \param percentage: The percentage amount (0-100).
    def update(self, percentage: int) -> None:
        if not self._visible:
            super().show()
        self.setProgress(percentage)

    ## Returns a boolean indicating whether the message is currently visible.
    @property
    def visible(self) -> bool:
        return self._visible