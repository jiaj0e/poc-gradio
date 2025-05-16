from pydantic import BaseModel, Field


class BodyGenAiPostRequest(BaseModel):
    contents: list[dict[str, str]] = Field(
        ...,
        description="List of contents to be generated.",
        example=[{"parts": [{"text": "Explain how AI works in a few words"}]}],
    )


class GenAiPostRequest(BaseModel):
    """
    Request model for make a request to an model.
    """

    data: BodyGenAiPostRequest = Field(
        ...,
        description="Request data for the model.",
    )


class TextPart(BaseModel):
    text: str


class ContentParts(BaseModel):
    parts: list[TextPart]
    role: str


class Candidate(BaseModel):
    content: ContentParts
    finishReason: str
    avgLogprobs: float


class TokenDetails(BaseModel):
    modality: str
    tokenCount: int


class UsageMetadata(BaseModel):
    promptTokenCount: int
    candidatesTokenCount: int
    totalTokenCount: int
    promptTokensDetails: list[TokenDetails]
    candidatesTokensDetails: list[TokenDetails]


class GenAiResponse(BaseModel):
    """
    Response model for make a request to an model.
    """

    candidates: list[Candidate]
    usageMetadata: UsageMetadata
    modelVersion: str
