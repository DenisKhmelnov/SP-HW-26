from typing import Union, Any

from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD = ('filter', 'map', 'unique', 'limit', 'sort', 'regex')

class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)


    @validates_schema
    def validate_cmd_params(self, values: Any, *args, **kwargs) -> Any:
        if values['cmd'] not in VALID_CMD:
            raise ValidationError('cmd1 contains not valid value')
        return values


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)