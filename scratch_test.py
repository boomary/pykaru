import sys

import click
import boto3
import botocore
import tablib
import openpyxl

DISTRIBUTIONS = 'Distributions'
DISTRIBUTION_ID = 'DistributionId'
NUM_ALIASES = 'NumAliases'
ALIAS = 'Alias'

DISTRIBUTION_LIST = 'DistributionList'
MARKER = 'Marker'
NEXT_MARKER = 'NextMarker'
MAX_ITEMS = 'MaxItems'
IS_TRUNCATED = 'IsTruncated'
QUANTITY = 'Quantity'
ITEMS = 'Items'

ID = 'Id'
ARN = 'ARN'
STATUS = 'Status'
LAST_MODIFIED_TIME = 'LastModifiedTime'
DOMAIN_NAME = 'DomainName'
ALIASES = 'Aliases'

# session = boto3.Session(profile_name='sec_nonprod',
#                             region_name='us-east-1')

# cloudfront = session.client('cloudfront')
# maxItems = 100
# truncated = True
# marker = None

# # Init worksheets 
# distSheet = tablib.Dataset()
# distSheet.headers = [ID, 
#                     ARN, 
#                     STATUS, 
#                     LAST_MODIFIED_TIME,
#                     DOMAIN_NAME,
#                     NUM_ALIASES]

# alaiseSheet = tablib.Dataset()
# alaiseSheet.headers = [ID, ALIAS]

# originSheet = tablib.Dataset()
# pathSheet = tablib.Dataset()

# while truncated:
#     if (marker is not None):
#         response = cloudfront.list_distributions(Marker=marker,
#                                                     MaxItems=str(maxItems))
#     else:
#           response = cloudfront.list_distributions(MaxItems=str(maxItems))
      
#     # DistributionList header
#     dJson = response.get('DistributionList')   

#     quantity = int(dJson.get('Quantity'))
#     truncated = dJson.get('IsTruncated')
#     marker = dJson.get('NextMarker') 
    

#     # DistributionList items  
#     dJson = dJson.get(ITEMS)
#     for distro in dJson:
#         distroId = distro.get(ID)        
#         aliases = distro.get(ALIASES)
#         numAliases = aliases.get(QUANTITY)

#         # Append aliseSheet
#         if numAliases > 0:
#             for alias in aliases.get(ITEMS):
#                 alaiseSheet.append([distroId, alias])

#         # Append distroSheet
#         distSheet.append([distroId,
#                             distro.get(ARN),
#                             distro.get(STATUS),
#                             distro.get(LAST_MODIFIED_TIME),
#                             distro.get(DOMAIN_NAME),
#                             numAliases])



# book = tablib.Databook()
# book.add_sheet(distSheet)
# book.add_sheet(alaiseSheet)

# with open('venv/test.xlsx', 'wb') as f:
#     f.write(book.export('xlsx'))

book = openpyxl.load_workbook('venv/test.xlsx')

SHEET_NAMES = [DISTRIBUTIONS, ALIASES]
i = 0
for sheetname in book.sheetnames:
    sheet = book[sheetname]
    sheet.title = SHEET_NAMES[i]
    sheet.auto_filter.ref = sheet.dimensions
    i += 1

book.save('venv/test.xlsx')
