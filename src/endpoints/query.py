from fastapi import APIRouter
from pyxi_couchbase_client import CouchbaseQryManager, CbQry
from models.qry_req import QryReq
from couchbase.result import QueryResult
import json

router = APIRouter()


def build_indx_qry(
    indx_name: str,
    bucket_name: str,
    scope_name: str,
    collection_name: str,
    property_name: str,
):
    indx_qry = f"CREATE INDEX idx_example ON `{bucket_name}`.`{scope_name}`.`{collection_name}`({property_name})"
    return indx_qry


@router.post("/query")
async def query(req: QryReq):
    manager = CouchbaseQryManager()
    qry = CbQry(req.query, req.params)

    result: QueryResult = manager.query(qry)
    rows = result.rows()
    json_result = list(rows)

    return {"result": json_result}
