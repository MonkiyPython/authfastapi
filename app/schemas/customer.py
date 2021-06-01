from pydantic import BaseModel


class New(BaseModel):
    customer_name: str
    customer_email: str
