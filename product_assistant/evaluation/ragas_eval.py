from ragas import SingleTurnSample
from utils.model_loader import ModelLoader
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.metrics import LLMContextPrecisionWithoutReference, ResponseRelevancy
import grpc.experimental.aio as grpc_aio
grpc_aio.init_grpc_aio()
model_loder=ModelLoader()

def evaluate_context_precision():
    """_summary_
    """
    pass

def evaluate_response_relevancy(query):
    """

    Args:
        query (_type_): _description_
    """
    pass