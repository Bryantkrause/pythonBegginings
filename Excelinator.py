from dataclasses import dataclass
import json
from openpyxl import load_workbook
import datetime



workbook = load_workbook('ForkliftEverything.xlsx')
workbook.sheetnames
# print(workbook.sheetnames)
sheet = workbook.active

@dataclass
class Product:
    id: str
    parent: str
    title: str
    category: str

@dataclass
class Review:
    id: str
    customer_id: str
    stars: int
    headline: str
    body: str
    date: datetime.datetime



# Product fields
PRODUCT_ID = 3
PRODUCT_PARENT = 4
PRODUCT_TITLE = 5
PRODUCT_CATEGORY = 6

# Review fields
REVIEW_ID = 14
REVIEW_CUSTOMER = 2
REVIEW_STARS = 7
REVIEW_HEADLINE = 12
REVIEW_BODY = 13
REVIEW_DATE = 1


workbook = load_workbook(filename="ForkliftEverything.xlsx", read_only=True)
sheet = workbook.active

products = []
reviews = []


# Using the values_only because you just want to return the cell value
for row in sheet.iter_rows(min_row=2, values_only=True):
    product = Product(id=row[PRODUCT_ID],
                      parent=row[PRODUCT_PARENT],
                      title=row[PRODUCT_TITLE],
                      category=row[PRODUCT_CATEGORY])
    products.append(product)

    # You need to parse the date from the spreadsheet into a datetime format
    spread_date = row[REVIEW_DATE]
    # parsed_date = datetime.strptime(spread_date, "%Y-%m-%d")

    review = Review(id=row[REVIEW_ID],
                    customer_id=row[REVIEW_CUSTOMER],
                    stars=row[REVIEW_STARS],
                    headline=row[REVIEW_HEADLINE],
                    body=row[REVIEW_BODY],
                    date=spread_date)
    reviews.append(review)

print(products[0])
print(reviews[0])
# print(sheet['A1:C10'])

# for row in sheet.iter_rows(
#     min_row=1,
#     max_row=2,
#     min_col=1,
#     max_col=3,
#     values_only=True):
#     print(row)

# for row in sheet.rows:
#     print(row)
# products = {}
# for row in sheet.iter_rows(
#         min_row=2,
#         min_col=4,
#         max_col=7,
#         values_only=True):
#     product_id=row[0]
#     product = {
#         'parent': row[1],
#         'title': row[2],
#         'category': row[3]
#     }
#     products[product_id] = product
