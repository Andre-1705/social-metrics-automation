from __future__ import annotations

import asyncio
from typing import Callable

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger


def schedule_metrics(job: Callable[[], asyncio.Future], timezone: str, minutes: int = 30) -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler(timezone=timezone)
    scheduler.add_job(job, IntervalTrigger(minutes=minutes), id="metrics-poller", replace_existing=True)
    scheduler.start()
    return scheduler
