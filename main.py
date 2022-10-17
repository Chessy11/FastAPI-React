from re import A
from traceback import print_tb
from typing import Optional
from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
#import Session'
from fastapi.staticfiles import StaticFiles
from database.db import  get_db, engine
from sqlalchemy.orm import Session
from models import tables
import requests
import schedule
import time
import json

from utils.envs import settings

tables.Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")  # define the directory for the static files

# @app.get("/", response_class=HTMLResponse)
# def index(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})





# query_1 = "chicken"

#get first 10 recipes



query_1 = "chicken"

api_url = f"https://api.edamam.com/api/recipes/v2?type=public&q={query_1}&app_id={settings.recipes_appid}&app_key={settings.recipes_appkey}"


        
# api_uri = f"https://api.edamam.com/api/recipes/v2/%s/?type=public&q={query_1}&app_id={settings.recipes_appid}&app_key={settings.recipes_appkey}"


#get 10 recipes
@app.get("/recipes", response_class=HTMLResponse)
def get_recipes(request: Request):
    url = requests.get(f"{api_url}")
    recipes = url.json()

    r = json.dumps(recipes)
    loaded_r = json.loads(r)
    
    # for i in loaded_r:
    #     if i  == "hits":
    #         for j in loaded_r[i]:
    #             uri = j["recipe"]["uri"]
    #             uri = uri.replace("http://www.edamam.com/ontologies/edamam.owl#", "")
    #             print (uri)
    
    uris = []
    
    for i in loaded_r:
        if i  == "hits":
            for j in loaded_r[i]:
                uri = j["recipe"]["uri"]
                uri = uri.replace("http://www.edamam.com/ontologies/edamam.owl#", "")
                uris.append(uri)


            
   
    return templates.TemplateResponse("index.html", {"request": request, "items": loaded_r, "uri": uris})





# #get 1 recipe
@app.get("/recipes/{uri}", response_class=HTMLResponse)
def get_recipe(request: Request, uri: str):
    api_uri = f"https://api.edamam.com/api/recipes/v2/{uri}?type=public&q={query_1}&app_id={settings.recipes_appid}&app_key={settings.recipes_appkey}"
    url = requests.get(f"{api_uri}")
    recipe = url.json()
    r = json.dumps(recipe)
    loaded_r = json.loads(r)
    
    # for i in loaded_r:
    #     if i == "recipe":
    #         for j in loaded_r[i]:
    #             if j == "ingredientLines":
    #                 ingredients = loaded_r[i][j]
    #                 for k in ingredients:
    #                     ingr = k
    #                     print(k)       '
    
    # for i in loaded_r:
    #     if i == "recipe": 
                       
    return templates.TemplateResponse("detail.html", {"request": request, "items": loaded_r, })




#create search function
@app.get("/search", response_class=HTMLResponse)
def search(request: Request, query: Optional[str]):
    url = requests.get(f"https://api.edamam.com/api/recipes/v2?type=public&q={query}&app_id={settings.recipes_appid}&app_key={settings.recipes_appkey}")
    recipes = url.json()
    r = json.dumps(recipes)
    loaded_r = json.loads(r)
    for i in loaded_r:
        #get only labels from loaded_r
        if i == "hits":
            for j in loaded_r[i]:
                print(j["recipe"]["label"])
                label = j["recipe"]["label"]
                #get image
                image = j["recipe"]["image"]
                #print first 50 letters of ingredient
                ingredient = j["recipe"]["ingredientLines"][:50]
                
                
                print("ID", id)
                print("LABEL:",label)
                print("IMAGE:",image)
                print("INGREDIENT:",ingredient)
                
    return templates.TemplateResponse("search_results.html", {"request": request, "items": loaded_r})




                
        
