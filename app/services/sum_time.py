from datetime import timedelta


def sum_time(total, more):
    total = str(total).split(":")
    more = str(more).split(":")
    new_total = timedelta(
        seconds=int(total[2]),
        minutes=int(total[1]),
        hours=int(total[0]),
    )
    new_more = timedelta(
        seconds=int(more[2]),
        minutes=int(more[1]),
        hours=int(more[0]),
    )
    return new_total + new_more
