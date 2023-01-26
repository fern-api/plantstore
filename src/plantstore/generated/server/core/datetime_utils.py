import datetime


def serialize_as_utc(dt: datetime.datetime) -> str: 
    serialized_utc = dt.astimezone(datetime.timezone.utc).isoformat()
    if serialized_utc[len(serialized_utc)-6:] != "+00:00":
        raise Exception("Failed to serialize datatime as UTC. This should never happen.")
    return serialized_utc[:len(serialized_utc)-6] + "Z"