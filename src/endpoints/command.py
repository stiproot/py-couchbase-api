from fastapi import APIRouter
from pyxi_couchbase_client import CouchbaseCmdManager, CbCmd
from models.cmd_req import CmdReq

router = APIRouter()


@router.post("/command")
async def command(req: CmdReq):
    manager = CouchbaseCmdManager(req.bucket_name, req.scope_name, req.collection_name)
    # await manager.command(CbCmd(req.key, req.payload))
    await manager.command(CbCmd(req.key, {}))
    return {"status": "accepted"}
