from langchain_huggingface import HuggingFaceEndpoint

from app.config.config import HUGGINGFACE_REPO_ID,HF_TOKEN,GROQ_API_KEY
from app.common.logger import get_logger
from app.common.custom_exception import CustomException


logger = get_logger(__name__)

from langchain_groq import ChatGroq


def load_llm_GrOQ(model_name: str= "llama-3.1-8b-instant",groq_api_key: str =GROQ_API_KEY):
    try:
        logger.info("Loading LLM From Groq using LLaMA3 Model....")

        llm=ChatGroq(
            groq_api_key=groq_api_key,
            model_name=model_name,
            temperature=0.3,
            max_tokens=256,
        )
        logger.info("LLM loaded Successfully from Groq...")
        return llm 
    
    except Exception as e:
        error_message = CustomException("Failed to load an LLM from Groq", e)
        logger.error(str(error_message))
        return None 
    

def load_llm_HF(huggingface_repo_id:str= HUGGINGFACE_REPO_ID,hf_token:str=HF_TOKEN):
    try:
        logger.info(f"Loading LLM from Hugging Face using {huggingface_repo_id}...")

        llm=HuggingFaceEndpoint(
            repo_id=HUGGINGFACE_REPO_ID,
            huggingfacehub_api_token = hf_token,
            temperature=0.3,
            max_new_tokens=256,
            return_full_text=False,
        )

    
        logger.info("LLM loaded Successfully from HuggingFace...")
        return llm 
    
    except Exception as e:
        error_message = CustomException("Failed to load an LLM from HuggingFace", e)
        logger.error(str(error_message))
        return None