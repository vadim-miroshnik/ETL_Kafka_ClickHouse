import logging
import uuid
from uuid import UUID

from aiokafka import AIOKafkaProducer
from fastapi import APIRouter, Depends

from api.v1.schemes import WatchingResponse
from db.kafka import get_kafka_producer

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post(
    "/{movie_id}", response_model=WatchingResponse, summary="Добавление просмотренного фрейма в кафку", description=""
)
async def watched_movies(frame: str, movie_id: UUID, kafka_producer: AIOKafkaProducer = Depends(get_kafka_producer)):
    user = uuid.uuid4()
    await kafka_producer.send_and_wait(f"{user}{movie_id}", frame.encode("UTF-8"))
    return WatchingResponse(movie_id=movie_id, user_id=user, frame=frame)
