from praatio import textgrid
import os


def split_interval(input_textgrid_path, output_textgrid_path):
    # Load the TextGrid
    tg = textgrid.openTextgrid(input_textgrid_path, includeEmptyIntervals=True)

    # Assuming there's only one tier and you know its name, e.g., "words"
    tier_name = tg.tierNames[0]
    tier = tg.getTier(tier_name)

    # Create a new list of intervals
    new_intervals = []
    final_start = 0.0
    for start, end, label in tier.entries:
        if label == "sil" or label == "":
            # 如果是sil做标签，则不改变，原样照抄
            new_intervals.append((start, end, label))
        else:
            # 按空格分开第二个label的内容
            words = label.split()
            num_words = len(words)
            interval_duration = round((end - start) / num_words - 0.05, 1) #均分第二个间隔内的时间

            # Create new intervals for each word
            for i, word in enumerate(words):
                word_start = round(start + i * interval_duration, 2)
                word_end = round(word_start + interval_duration - 0.05, 4)
                new_intervals.append((word_start, word_end, word)) #添加信息到interval 间隔的列表中，结构是起始时间，结束时间，词
                new_intervals.append((word_end, round(word_end + 0.05, 4), 'sil'))

    # Create a new tier with split intervals
    new_tier = textgrid.IntervalTier(tier_name, new_intervals, tier.minTimestamp, tier.maxTimestamp)

    # Create a new TextGrid with the modified tier
    new_tg = textgrid.Textgrid()
    new_tg.addTier(new_tier)

    # Save the modified TextGrid
    new_tg.save(output_textgrid_path, format="short_textgrid", includeBlankSpaces=True)


# Example usage
files = os.listdir('./')
for file in files:
    if file.endswith('TextGrid'):
        split_interval(file, './output/' + file)
