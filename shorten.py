# import mido
# from mido import MidiFile, MidiTrack, Message

# def extract_midi_section(input_file, output_file, start_time, end_time):
#     mid = MidiFile(input_file)
#     extracted_mid = MidiFile()

#     for i, track in enumerate(mid.tracks):
#         extracted_track = MidiTrack()
#         extracted_mid.tracks.append(extracted_track)

#         current_time = 0

#         for msg in track:
#             current_time += msg.time

#             # Check if the current message is within the specified time range
#             if start_time <= current_time <= end_time:
#                 extracted_track.append(msg)

#     extracted_mid.save(output_file)

# # Example usage
# input_file = 'melody/001/001melody.mid'
# output_file = '001melody_shortened.mid'
# start_time = 7 * mido.second2tick(1, ticks_per_beat=960, tempo=120)  # Assuming 480 ticks per beat
# end_time = 13 * mido.second2tick(1, ticks_per_beat=960, tempo=120)

# extract_midi_section(input_file, output_file, start_time, end_time)

import mido
from mido import MidiFile, MidiTrack

def shorten_midi(input_file_path, output_file_path, start_bar, end_bar):
    mid = MidiFile(input_file_path)

    ticks_per_beat = mid.ticks_per_beat
    ticks_per_bar = ticks_per_beat * 4  # Assuming 4/4 time signature

    start_tick = (start_bar - 1) * ticks_per_bar  # Convert bar to ticks
    end_tick = end_bar * ticks_per_bar  # Convert bar to ticks

    new_midi = MidiFile(ticks_per_beat=mid.ticks_per_beat)

    for i, track in enumerate(mid.tracks):
        new_track = MidiTrack()
        new_midi.tracks.append(new_track)

        for msg in track:
            if msg.type == 'note_on' or msg.type == 'note_off':
                if msg.time < start_tick:
                    continue
                elif msg.time >= end_tick:
                    break
                else:
                    msg.time -= start_tick

            new_track.append(msg)

    new_midi.save(output_file_path)

# Example usage:
input_file_path = 'melody/001/001melody.mid'
output_file_path = 'melody/001/001melody_shortened.mid'
start_bar = 7
end_bar = 13

shorten_midi(input_file_path, output_file_path, start_bar, end_bar)