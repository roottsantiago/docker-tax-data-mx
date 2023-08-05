from fastapi import APIRouter


from taxdata.app.schemas.datafiscal import (
    RfcSchema,
    CurpSchema,
    NssSchema
)
from taxdata.app.utils.common import get_parse_data
from pyfiscal.generate import (
    GenerateRFC,
    GenerateCURP,
    GenerateNSS
)

router = APIRouter()


@router.get("/")
def read_root():
    """
    Api Home View
    """
    return {"data": "API PyFiscal on TaxDataMX"}


@router.post("/rfc/")
async def calculate_rfc(item: RfcSchema):
    """
    Api calculates the RFC
    """
    data = get_parse_data(item)
    response = GenerateRFC(**data).data
    return {"data": response}


@router.post("/curp/")
async def calculate_curp(item: CurpSchema):
    """
    Api calculates the CURP
    """
    data = get_parse_data(item)
    response = GenerateCURP(**data).data
    return {"data": response}


@router.post("/nss/")
async def calculate_nss(item: NssSchema):
    """
    Api calculates the last verifier digit, enter the first 10 digits.
    """
    data = GenerateNSS(nss=item.nss).data
    return {"data": data}
