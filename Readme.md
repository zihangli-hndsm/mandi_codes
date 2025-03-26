# Documentation
## About this project
In the project, a corpus called "Mandi corpus" is created, which contains 43 speakers' recording of their Chinese mandarin and dialects. There are also corresponding Textgrid annotation files for each audio file, and creating them is our work goal.
## Results
The project is completed. However, we did not achieve 100% automatic processing, i. e. some work had to be done manually. For each audio file, a corresponding txt transcription is given, and we implemented the automatic Textgrid file transfer from txt transcription, but the text in the transferred Textgrid files are not aligned with the audio. We had to manually adjust the boundary to align the text with the audio to the sentence level, and then it would be ready to be run. After manual alignment, the rest of the work was completed by programs.
## How it is implemented
Given the text of the recordings, we use Montreal Forced Aligner (MFA) to automatically generate alignments for each recording, and also annotate each word by their phonemes, from pre-created dictionaries. To implement this, we need to firstly use scripts to create unaligned Textgrid files from txt transcriptions, and then manually adjust the boundaries so that the tiles in Textgrid match the articulations at the sentence level. Then the files would be runnable, and put in MFA to generate word-by-word alignments and the annotations. 
**Generated evenly divided textgrid**
![example_pic_1](/assets/img/example_step_1.png "Generated evenly divided textgrid")
**Textgrid manually aligned to the sentence level**
![example_pic_2](/assets/img/example_step_2.png "Textgrid manually aligned to the sentence level")
**After the two runs with different models (final result)**
![example_pic_3](/assets/img/example_step_3.png "After the two runs with different models (final result)")
## The use of MFA models
From several test runs, we found that one alignment model (mandarin_mfa) is better at tokenizing the Chinese sentences, but bad at transferring graphemes to phonemes (G2P). So we use this model to do the first run, tokenizing everything, and remove the bad G2P results for the second run, where we use a model (zh-CN_vxc_acoustic17) better at G2P to generate the phonemes. Some words were not in the dictionary, so we had to manually add some of them.
## The use of tools
The assistant of ChatGPT is used when writing Python scripts to process the txt transcriptions.
## Group member responsibilities
We are a group of 2. We are both pretty fully engaged in the project. There are not many but small differences in our responsibilities: roughly speaking, I am responsible of writing documents, writing codes, running the model, and Shunan is responsible of processing unaligned Textgrid files to make sure they are runnable.
## Detailed explanation of the scripts
### tsv_to_textgrid_single.py
This script reads tsv annotation files and convert them to textgrid files.
### combine_lines.py
Adjusts the form of transcriptions to fit the tsv to textgrid process.
### tier_separator.py
Removes the second tier of textgrid files, which is used to process the results of the first model.
### add_space_in_textgrid.py
Separates the sentence labels into word labels.
## Discussion
We started the project with the plan of automating everything, but we didn't manage to automate the alignment of sentences. We have expected MFA to be able to accomplish this, but we found that it only works at the sentence level, and the sentences had to be divided manually. This was extremely time-consuming, but we have automated everything apart from this, making the project nevertheless accomplishable. In the future, I expect to see automatic sentence alignment based on transformer model with very good performances, as it works well in understanding tokenizable information.
