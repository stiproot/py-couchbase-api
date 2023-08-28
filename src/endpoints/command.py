from fastapi import APIRouter
from pyxi_couchbase_client import CouchbaseCmdManager, CbCmd
from models.cmd_req import CmdReq
import json

router = APIRouter()


@router.post("/command")
async def command(req: CmdReq):
    manager = CouchbaseCmdManager(req.bucket_name, req.scope_name, req.collection_name)

    data = json.loads(req.payload)
    cb_cmd = CbCmd(req.key, data)

    await manager.command(cb_cmd)

    return {"status": "accepted"}
