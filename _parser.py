from time_convert import lrc_time_to_timedelta, timedelta_to_microseconds
import re
import srt

timestamp_regex = re.compile(r'\[[0-9]{2}:[0-9]{2}\.[0-9]{2,3}\]')


def parse_lrc(file_path, file_encoding):
    time_list = []
    lyric_list = {}

    with open(file_path, 'r', encoding=file_encoding) as lyric:
        lines = lyric.read().splitlines()
        for line in lines:
            if all_time := re.findall(timestamp_regex, line):
                for time in all_time:
                    time = time.replace('[', '', 1).replace(']', '', 1)
                    time = str(timedelta_to_microseconds(
                        lrc_time_to_timedelta(time)
                    ))
                    time_list.append(time)
                    try:
                        lyric_list[time]
                    except KeyError:
                        lyric_list[time] = []
                    finally:
                        lyric_list[time].append(
                            line.replace(''.join(all_time), '')
                        )

    # import json
    # with open('debug_parse_lrc.json', 'w+', encoding='utf-8') as debug_json:
    #     debug_json.write(json.dumps(result, ensure_ascii=False))

    return {
        'time_list': sorted(list(set(time_list)), key=int),
        'lyric_list': lyric_list,
    }


def parse_srt(file_path, file_encoding):
    time_list = []
    lyric_list = {}

    with open(file_path, 'r', encoding=file_encoding) as srt_file:
        subs = srt.parse(srt_file)
        for sub in subs:
            time = timedelta_to_microseconds(sub.start)
            time_list.append(time)
            lyric_list[str(time)] = sub.content.split('\n')

    # import json
    # with open('debug_parse_srt.json', 'w+', encoding='utf-8') as debug_json:
    #     debug_json.write(json.dumps(result, ensure_ascii=False))

    return {
        'time_list': sorted(list(set(time_list)), key=int),
        'lyric_list': lyric_list,
    }
