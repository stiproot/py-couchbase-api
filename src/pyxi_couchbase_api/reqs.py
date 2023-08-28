class CmdReq:
    bucket_name: str
    scope_name: str
    collection_name: str
    key: str
    payload: str


class QryReq:
    query: str
    params: [str]
