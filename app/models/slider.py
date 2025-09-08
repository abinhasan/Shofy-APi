from sqlalchemy import Column, Integer, String, LargeBinary
from app.core.database import Base

class Slider(Base):
    __tablename__ = "sliders"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    sub_title = Column(String, nullable=False)
    nav_title = Column(String, nullable=False)
    #image = Column(LargeBinary, nullable=True)
    #nav_icon = Column(LargeBinary, nullable=True)
