import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="file_info_api")
def get_files(req: func.HttpRequest) -> func.HttpResponse:
    """
    GET /files endpoint
    Returns metadata about files in Blob Storage
    """
    logging.info('File Info API endpoint called')
    
    try:
       #TODO:  Connect to real Azure Blob Storage and query actual files
        files = [
            {
                "name": "invoice_2026_01.csv",
                "size": 2048,
                "upload_date": "2026-04-24",
                "status": "processed"
            },
            {
                "name": "report_q1.xlsx",
                "size": 5120,
                "upload_date": "2026-04-23",
                "status": "pending"
            }
        ]
        
        return func.HttpResponse(
            json.dumps(files),
            status_code=200,
            mimetype="application/json"
        )
    
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": "Failed to retrieve files"}),
            status_code=500,
            mimetype="application/json"
        )