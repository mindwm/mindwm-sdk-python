# coding: utf-8

"""
    Mindwm API

    This document describes the documentation, a collection of JSON schemas and example cloudevent and payloads

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from MindWM.models.clipboard_context import ClipboardContext
from MindWM.models.vector2int import Vector2int
from typing import Optional, Set
from typing_extensions import Self

class Clipboard(BaseModel):
    """
    Clipboard
    """ # noqa: E501
    context: ClipboardContext
    clipboard_type: StrictStr = Field(description="Type of clipboard", alias="clipboardType")
    content: StrictStr = Field(description="Clipboard content")
    selection_start: Optional[Vector2int] = Field(default=None, alias="selectionStart")
    selection_end: Optional[Vector2int] = Field(default=None, alias="selectionEnd")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["context", "clipboardType", "content", "selectionStart", "selectionEnd"]

    @field_validator('clipboard_type')
    def clipboard_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Primary', 'Secondary', 'Clipboard']):
            raise ValueError("must be one of enum values ('Primary', 'Secondary', 'Clipboard')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Clipboard from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['context'] = self.context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of selection_start
        if self.selection_start:
            _dict['selectionStart'] = self.selection_start.to_dict()
        # override the default output from pydantic by calling `to_dict()` of selection_end
        if self.selection_end:
            _dict['selectionEnd'] = self.selection_end.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Clipboard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "context": ClipboardContext.from_dict(obj["context"]) if obj.get("context") is not None else None,
            "clipboardType": obj.get("clipboardType"),
            "content": obj.get("content"),
            "selectionStart": Vector2int.from_dict(obj["selectionStart"]) if obj.get("selectionStart") is not None else None,
            "selectionEnd": Vector2int.from_dict(obj["selectionEnd"]) if obj.get("selectionEnd") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

