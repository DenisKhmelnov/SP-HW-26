from typing import Union, Tuple

from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError


from builder import query_builder
from db import db
from models import BatchRequestParams

main_bp = Blueprint('main', __name__)

@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Union[Response, Tuple]:
    try:
        params = BatchRequestParams().load(data=request.json)
    except ValidationError as error:
        return jsonify(error.messages), 400

    result = None
    for query in params['queries']:
        result = query_builder(
            cmd=query['cmd'],
            value=query['value'],
            data=result,
        )

    return jsonify(result)

@main_bp.route('/test_db')
def test_db():
    result = db.session.execute('SELECT 1').scalar_one()
    return jsonify(
        {
            'result': result,
        }
    )
