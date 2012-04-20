"""Create (more scilifelab specific) reports on google docs.
"""

import bcbio.google.bc_metrics
import bcbio.google.spreadsheet

# Structure of the Delivery worksheet
DELIVERY_STATUS_HEADER = [ \
"Sample name",
"Number of reads ordered",
"Number of reads delivered",
"Is sample finished?",
"Comment",
"Delivery dates",
"Read pairs delivered at each delivery"]


def create_project_delviery_report_on_gdocs(fc, encoded_credentials, gdocs_folder):
    """Summarizes delivery status in a 'Delivery' worksheet on a Google
    spreadsheet.
    """
    pass


def write_project_delivery_status_to_gdocs(client, ssheet, proj_data):
    """Summarizes delivery status in a 'Delivery' worksheet on a Google
    spreadsheet.
    """
    wsheet_title = "Delivery"

    delivery_wsheet = bcbio.google.spreadsheet.get_worksheet(client, ssheet, wsheet_title)

    num_rows = bcbio.google.spreadsheet.row_count(delivery_wsheet)
