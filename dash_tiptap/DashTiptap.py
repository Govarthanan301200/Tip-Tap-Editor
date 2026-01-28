# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class DashTiptap(Component):
    """A DashTiptap component.


Keyword arguments:

- id (string; optional)

- mentions (list of dicts; optional)

    `mentions` is a list of dicts with keys:

    - id (string | number; required)

    - label (string; required)

- value (string; default '<p>Hello World! Type @ to mention someone.</p>')"""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'dash_tiptap'
    _type = 'DashTiptap'
    Mentions = TypedDict(
        "Mentions",
            {
            "id": typing.Union[str, NumberType],
            "label": str
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        mentions: typing.Optional[typing.Sequence["Mentions"]] = None,
        value: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'mentions', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'mentions', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashTiptap, self).__init__(**args)

setattr(DashTiptap, "__init__", _explicitize_args(DashTiptap.__init__))
