from py_edamam import PyEdamam
import json
import requests
# Create an instance of the Edamam class

recipes_appid="8a0ed57c"
recipes_appkey="33a0ed97458f99bf65220cf65c45cba9"

query_1 = "chicken"

# request = requests.get(f"https://api.edamam.com/search?q={query_1}&app_id={recipes_appid}&app_key={recipes_appkey}")


# # get first recipe

# recipe = request.json()["hits"][0]["recipe"]

# #get health labels

data = {
  "recipe": {
    "uri": "string",
    "label": "string",
    "image": "string",
    "images": {
      "THUMBNAIL": {
        "url": "string",
        "width": 0,
        "height": 0
      },
      "SMALL": {
        "url": "string",
        "width": 0,
        "height": 0
      },
      "REGULAR": {
        "url": "string",
        "width": 0,
        "height": 0
      },
      "LARGE": {
        "url": "string",
        "width": 0,
        "height": 0
      }
    },
    "source": "string",
    "url": "string",
    "shareAs": "string",
    "yield": 0,
    "dietLabels": [
      "string"
    ],
    "healthLabels": [
      "string"
    ],
    "cautions": [
      "string"
    ],
    "ingredientLines": [
      "string"
    ],
    "ingredients": [
      {
        "text": "string",
        "quantity": 0,
        "measure": "string",
        "food": "string",
        "weight": 0,
        "foodId": "string"
      }
    ],
    "calories": 0,
    "glycemicIndex": 0,
    "totalCO2Emissions": 0,
    "co2EmissionsClass": "A+",
    "totalWeight": 0,
    "cuisineType": [
      "string"
    ],
    "mealType": [
      "string"
    ],
    "dishType": [
      "string"
    ],
    "instructions": [
      "string"
    ],
    "tags": [
      "string"
    ],
    "externalId": "string",
    "totalNutrients": {},
    "totalDaily": {},
    "digest": [
      {
        "label": "string",
        "tag": "string",
        "schemaOrgTag": "string",
        "total": 0,
        "daily": 0,
        "unit": "string",
        "sub": {}
      }
    ]
  },
  "_links": {
    "self": {
      "href": "string",
      "title": "string"
    },
    "next": {
      "href": "string",
      "title": "string"
    }
  }
}


#get objects from ingredients with values
# for i in data:
#     if i == "recipe":
#         for j in data[i]:
#             if j == "ingredients":
#                 for k in data[i][j]:
#                     for n in k:
#                         print(k[n])
                        
                        
digest = {'daily': 422.2290860040035, 'hasRDI': True, 'label': 'Fat', 'schemaOrgTag': 'fatContent', 'sub': [{'daily': 312.48809499328024, 'hasRDI': True, 'label': 'Saturated', 'schemaOrgTag': 'saturatedFatContent', 'tag': 'FASAT', 'total': 62.497618998656044, 'unit': 'g'}, {'daily': 0.0, 'hasRDI': False, 'label': 'Trans', 'schemaOrgTag': 'transFatContent', 'tag': 'FATRN', 'total': 1.047163345382, 'unit': 'g'}, {'daily': 0.0, 'hasRDI': False, 'label': 'Monounsaturated', 'schemaOrgTag': None, 'tag': 'FAMS', 'total': 147.39060633938868, 'unit': 'g'}, {'daily': 0.0, 'hasRDI': False, 'label': 'Polyunsaturated', 'schemaOrgTag': None, 'tag': 'FAPU', 'total': 47.35051984782951, 'unit': 'g'}], 'tag': 'FAT', 'total': 274.4489059026023, 'unit': 'g'}


# get every key and value from digest


# get every key and value from digest

for i in digest :
    for j in i:
        print(i[j])