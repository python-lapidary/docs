# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

__all__ = (
    'ApiClient',
)

import lapidary.runtime
import pydantic
import typing_extensions as typing
import annotated_types
import datetime
import test_dummy.components.requestBodies.dummy.content.applicationu_ljson.schema.schema
import test_dummy.components.schemas.all.schema
import test_dummy.components.schemas.schema1.schema
import test_dummy.paths.u_linline_schema_propertiesu_l.get.responses.default.content.applicationu_ljson.schema.schema
import test_dummy.paths.u_ltestu_l.get.parameters.meta
import test_dummy.paths.u_ltestu_l.get.parameters.u_n.schema.schema
import test_dummy.paths.u_ltestu_l.get.responses.default.headers
import types


class ApiClient(lapidary.runtime.ClientBase):
    
    def __init__(
        self,
        *, base_url: str = '/',
        **kwargs,
    ) -> None:
        super().__init__(
            security=(
                {'oauth-refresh': ('read', 'write')},
                {'oauth': ('read', 'write')},
                {'api-key': ()},
                {'api-key-cookie': ()},
                {'api-key-query': ()},
                {'http_basic': ()},
                {'http_digest': ()},
            ),
            base_url=base_url,
            **kwargs,
        )
    
    @lapidary.runtime.get('/test/',)
    async def test_op(
        self: typing.Self,
        *, param1_q: typing.Annotated[
            typing.Union[
            typing.Annotated[
                int,
                annotated_types.Ge(20,),
            ],
            test_dummy.components.schemas.all.schema.all,
            test_dummy.components.schemas.schema1.schema.schema1,
        ],
            lapidary.runtime.Query('param1',),
        ],
        param2_q: typing.Annotated[
            typing.Union[
            test_dummy.paths.u_ltestu_l.get.parameters.u_n.schema.schema.schema,
            None,
        ],
            lapidary.runtime.Query('param2',),
        ] = None,
        param3_q: typing.Annotated[
            typing.Union[
            datetime.date,
            None,
        ],
            lapidary.runtime.Query('param3',),
        ] = None,
        meta: typing.Annotated[
            typing.Union[
            test_dummy.paths.u_ltestu_l.get.parameters.meta.RequestMetadata,
            None,
        ],
            lapidary.runtime.Metadata,
        ] = None,
    ) -> typing.Annotated[
            typing.Union[
            tuple[
                test_dummy.components.schemas.all.schema.all,
                test_dummy.paths.u_ltestu_l.get.responses.default.headers.ResponseMetadata,
            ],
            tuple[
                test_dummy.components.schemas.all.schema.all,
                None,
            ],
        ],
            lapidary.runtime.Responses({
                'default': lapidary.runtime.Response(
                    lapidary.runtime.Body({
                        'application/json': test_dummy.components.schemas.all.schema.all,
                    },),
                    test_dummy.paths.u_ltestu_l.get.responses.default.headers.ResponseMetadata,
                ),
                '2XX': lapidary.runtime.Response(
                    lapidary.runtime.Body({
                        'application/json': test_dummy.components.schemas.all.schema.all,
                    },),
                ),
            },),
        ]:
        pass
    
    @lapidary.runtime.get('/inline_schema_properties/',)
    async def inline_schema_properties(
        self: typing.Self,
    ) -> typing.Annotated[
            tuple[
            test_dummy.paths.u_linline_schema_propertiesu_l.get.responses.default.content.applicationu_ljson.schema.schema.schema,
            None,
        ],
            lapidary.runtime.Responses({
                'default': lapidary.runtime.Response(
                    lapidary.runtime.Body({
                        'application/json': test_dummy.paths.u_linline_schema_propertiesu_l.get.responses.default.content.applicationu_ljson.schema.schema.schema,
                    },),
                ),
            },),
        ]:
        pass
    
    @lapidary.runtime.get(
        '/custom-security',
        security=({'oauth': ('read',)},),
    )
    async def customSecurity(
        self: typing.Self,
    ) -> typing.Annotated[
            tuple[
            list[test_dummy.components.schemas.all.schema.all,],
            None,
        ],
            lapidary.runtime.Responses({
                'default': lapidary.runtime.Response(
                    lapidary.runtime.Body({
                        'application/json': list[test_dummy.components.schemas.all.schema.all,],
                    },),
                ),
            },),
        ]:
        pass
    
    @lapidary.runtime.get(
        '/insecure',
        security=(),
    )
    async def insecure(
        self: typing.Self,
        body: typing.Annotated[
            test_dummy.components.requestBodies.dummy.content.applicationu_ljson.schema.schema.schema,
            lapidary.runtime.Body({
                'application/json': test_dummy.components.requestBodies.dummy.content.applicationu_ljson.schema.schema.schema,
            },),
        ],
    ) -> typing.Annotated[
            tuple[
            test_dummy.components.schemas.all.schema.all,
            None,
        ],
            lapidary.runtime.Responses({
                'default': lapidary.runtime.Response(
                    lapidary.runtime.Body({
                        'application/json': test_dummy.components.schemas.all.schema.all,
                    },),
                ),
            },),
        ]:
        pass
