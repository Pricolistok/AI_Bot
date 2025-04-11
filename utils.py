from shutil import rmtree
from os import mkdir
from dataclasses import dataclass


@dataclass()
class UtilsSettings:
    photo_id: int = 0
    document_id: int = 0


async def createDir():
    mkdir('documents')
    mkdir('pictures')

async def removeDir():
    rmtree('documents/')
    rmtree('pictures/')