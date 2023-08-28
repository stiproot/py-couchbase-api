from fastapi import APIRouter
from pyxi_couchbase_client import CouchbaseQryManager, CbQry
from models.qry_req import QryReq
from couchbase.result import QueryResult
import json

router = APIRouter()


@router.post("/query")
async def query(req: QryReq):
    manager = CouchbaseQryManager()

    qry = CbQry(req.query, req.params)

    result: QueryResult = manager.query(qry)

    rows = result.rows()

    json_result = list(rows)

    # print(json_result[0]["collection_tmp"])

    return {"result": json_result}
