from _parser import parse_lrc, parse_srt
from time_convert import microseconds_to_lrc_time, microseconds_to_timedelta
from os import path
from datetime import timedelta
import srt


def lrc2srt(lrc_path, srt_path='', lrc_encoding='utf-8', srt_encoding='utf-8'):
    result = parse_lrc(lrc_path, lrc_encoding)

    old_fn = list(path.splitext(lrc_path))
    old_fn[-1] = '.srt'
    new_fn = ''.join(old_fn)

    srt_path = path.join(srt_path, new_fn) if srt_path else new_fn
    subs = []
    for index, time in enumerate(result['time_list']):
        try:
            end_time = microseconds_to_timedelta(
                result['time_list'][index + 1]
            )
        except IndexError:
            end_time = \
                microseconds_to_timedelta(time)\
                + timedelta(seconds=10)
        start_time = microseconds_to_timedelta(time)

        subs.append(
            srt.Subtitle(
                index=None,
                start=start_time,
                end=end_time,
                content=srt.make_legal_content(
                    '\n'.join(result['lyric_list'][time]))
            )
        )

    with open(srt_path, 'w+', encoding=srt_encoding) as srt_file:
        srt_file.write(srt.compose(subs))


def srt2lrc(srt_path, lrc_path='', lrc_encoding='utf-8', srt_encoding='utf-8'):
    result = parse_srt(srt_path, srt_encoding)

    old_fn = list(path.splitext(srt_path))
    old_fn[-1] = '.lrc'
    new_fn = ''.join(old_fn)

    lrc_path = path.join(lrc_path, new_fn) if lrc_path else new_fn
    with open(lrc_path, 'w+', encoding=lrc_encoding) as lrc_file:
        for time in result['time_list']:
            for lyric in result['lyric_list'][str(time)]:
                lrc_file.write(f'[{microseconds_to_lrc_time(time)}]{lyric}\n')
