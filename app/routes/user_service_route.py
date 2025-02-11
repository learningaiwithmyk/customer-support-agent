from fastapi import APIRouter,HTTPException
from typing import Dict,Optional
from pydantic import BaseModel

from app.services.intent_service import IntentService
from app.services.entity_service import EntityService
from app.services.package_service import PackageService
from app.services.policy_info_service import PolicyInfoService

router=APIRouter()

intent_service=IntentService()
entity_service=EntityService()

services={
    "track_package":PackageService(),
    "return_policy":PolicyInfoService()
}

user_context:Dict[str,Dict[str,Optional[str]]]={}

"""
user_context={
                            "123":{
                                            "pending_intent":"track_package",
                                            "required_field":"order_id"
                                     }
                        }
"""

class UserRequest(BaseModel):
    input_statement:str
    user_id:str

@router.post("/user_request")
async def process_user_request(request:UserRequest):
    try:
        user_id=request.user_id
        user_input=request.input_statement

        if user_context.get(user_id):
            context_info=user_context[user_id]
            pending_intent=context_info["pending_intent"]
            required_field=context_info["required_field"]

            if required_field and pending_intent:
                result=services[pending_intent].fetch_details(user_input.strip())
                user_context.pop(user_id)

                if not result:
                    raise HTTPException(status_code=400,
                                        detail=f"Sorry unable to find details for your request:{user_input}")

                return {"service_response": result}

        #find intent using intent service class
        intent=intent_service.get_intent(user_input)
        if not intent or intent not in services:
            raise HTTPException(status_code=400,detail="intent not found or not supported")

        #find entities using entity service class
        entities=entity_service.get_entities(user_input)


        #Fetch details from db based on intent and entities
        if intent=="track_package":
            order_id=entities.get("order_id")

            if not order_id:

                user_context[user_id]={"pending_intent":"track_package","required_field":"order_id"}
                return  {"message":"Order number required to fetch data, kindly provide order details"}

            result=services[intent].fetch_details(order_id)

        elif intent=="return_policy":
            product_category=entities.get("product_category")

            if not product_category:
                result=services[intent].fetch_details("return_policy","")
            else:
                result = services[intent].fetch_details("return_policy", product_category)

        else:
            result=services[intent].fetch_details(user_input)

        if not result:
            raise HTTPException(status_code=400, detail=f"Sorry unable to find details for your request:{user_input}")

        return {"service_response":result}

    except HTTPException as http_err:
        raise http_err

    except Exception as err:
        raise HTTPException(status_code=500,detail=str(err))



















