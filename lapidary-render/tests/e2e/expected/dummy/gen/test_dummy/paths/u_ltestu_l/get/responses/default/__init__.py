# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing_extensions as typing
from lapidary.runtime import *
import test_dummy.components.schemas.all.schema


class Response(ResponseEnvelope):
    body: typing.Annotated[test_dummy.components.schemas.all.schema.all, ResponseBody()]
    xu_jcount: typing.Annotated[typing.Union[None, int], Header('x-count')]
