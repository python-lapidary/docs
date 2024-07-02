# [Lapidary](lapidary/docs/index.md)

Python DSL for Web API clients.

## Features

- [x] In-python DSL for writing Web API clients declaratively
- [x] Use pydantic models for JSON data
- [ ] Compatibility with OpenAPI
    - [3.0 (in-progress)](lapidary-render/docs/openapi.md)
    - 3.1 (planned)

# [Lapidary Render](./lapidary-render/docs/index.md)

Code generator that creates Web API client code from an OpenAPI document.

## Features

- [x] Deliver IDE-friendly client code that simplifies communication with API servers.

- [x] The generator code should be simple.

    Lapidary-render does most of the processing in Python, only leaving the rendering to Jinja templates.

- [x] Client code should be simple.

    The generated code uses the `lapidary` DSL library, which makes the client code DRY and similar in style to API servers that use Litestar or FastAPI.

- [ ] Compatible changes to the OpenAPI document should result in compatible changes to the generated code.

    Whenever possible, generated names should not depend on elements position, or the presence or absence of other elements.

    *Starting from version 1.0; terms and conditions apply.*
