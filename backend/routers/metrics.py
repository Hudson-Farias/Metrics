from fastapi import APIRouter, File, UploadFile, HTTPException
from pandas import read_csv, read_excel
from io import StringIO, BytesIO

from models.metrics import MetricsModel

from metrics.MRR import MRR
from metrics.ChurnRate import ChurnRate

router = APIRouter()

accepted_formats = [
    'text/csv',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
]

@router.post("/metrics", status_code = 201, response_model = MetricsModel)
async def metrics(file: UploadFile = File(...)):
    content_type = file.content_type

    if content_type not in accepted_formats:
         raise HTTPException(status_code = 415, detail = f'Unsupported file type.')

    content = await file.read()

    if content_type == 'text/csv':
        content_decode = content.decode('utf-8')
        content_stream = StringIO(content_decode)

        df = read_csv(content_stream)

    else:
        content_stream = BytesIO(content)

        df = read_excel(content_stream)

    mrr = MRR(df)
    chunrate = ChurnRate(df)

    if not mrr.columns_checked or not chunrate.columns_checked:
        raise HTTPException(status_code = 422, detail = f'Missing required columns.')

    response = MetricsModel(
        mrr = mrr.calc(), 
        chunrate = chunrate.calc()
    )

    return response