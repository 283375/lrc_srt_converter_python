from datetime import timedelta


def microseconds_to_timedelta(ms: int):
    return timedelta(microseconds=ms * 1000)


def timedelta_to_microseconds(td: timedelta):
    return int(f"{td.seconds}{str(td.microseconds)[:3].ljust(3, '0')}")


def lrc_time_to_timedelta(lrc_time: str):
    init_split = lrc_time.split(':')
    minutes = int(init_split[0])
    second_split = init_split[1].split('.')
    seconds = int(second_split[0])
    microseconds = int(second_split[1].ljust(6, '0'))
    return timedelta(minutes=minutes, seconds=seconds,
                     microseconds=microseconds)


def microseconds_to_lrc_time(ms: int):
    td = microseconds_to_timedelta(ms)
    minutes = td.seconds // 60
    seconds = td.seconds % 60
    microseconds = td.microseconds // 1000
    return f'{str(minutes).zfill(2)}:{str(seconds).zfill(2)}.{str(microseconds).zfill(3)}'
