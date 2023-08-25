from fastapi import FastAPI
from pyxi_couchbase_client import CouchbaseQryManager, CouchbaseCmdManager, Qry, Cmd
from reqs import CmdReq, QryReq
import asyncio

app = FastAPI()


@app.get("/couchbase/query")
async def query(req: QryReq):
    manager = CouchbaseQryManager()
    result = manager.query(Qry(req.query, req.params))
    return {"result": result}


@app.post("/couchbase/command")
async def command(req: CmdReq):
    manager = CouchbaseCmdManager(req.bucket_name, req.scope_name, req.collection_name)
    await manager.command(Cmd(req.key, req.payload))
    return {"status": "accepted"}


if __name__ == "__main__":

    async def main():
        pass

    asyncio.run(main())
