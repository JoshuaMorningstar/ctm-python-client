
from __future__ import annotations
import attrs
import typing
import enum

from aapi.bases import AAPIObject

@attrs.define
class SiteStandardData(AAPIObject):

    _type: str = attrs.field(init=False, default='SiteStandardData', metadata={
                             '_aapi_repr_': 'Type', '_type_aapi_': 'SiteStandardData'})
    object_name: str = attrs.field(metadata={'_aapi_name_': True})
