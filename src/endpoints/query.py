from fastapi import APIRouter
from pyxi_couchbase_client import CouchbaseQryManager, CbQry
from models.qry_req import QryReq

router = APIRouter()


@router.get("/query")
async def query(req: QryReq):
    manager = CouchbaseQryManager()
    # result = manager.query(CbQry(req.query, req.params))
    result = manager.query(CbQry(req.query, []))
    return {"result": result}
