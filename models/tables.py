from cmath import rect
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Float
from sqlalchemy.orm import relationship
from database.db import Base
from sqlalchemy.dialects.postgresql import JSON

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    # recipe = Column(JSON)
    label = Column(String)
    health_labels = Column(String)
    
    
