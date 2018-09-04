# Audible Language Flashcards

Command-line utility that plays all .mp3 files within the same directory and all subdirectories in a random order, and quizzes you on each audio snippet's English translation.

## Instructions

Place all audio files in the same directory as the `practice.py` file, or organize them however you please in subdirectories (as long as `practice.py` is kept in the main directory). Each audio file's name should be its English translation. If there are multiple acceptable answers for one audio file, separate each answer with an underscore in the audio file's name.

### Audio File Name Examples

* Words
  * `person.mp3`
  * `truly_very_really.mp3`
* Phrases
  * `thankYou.mp3`
  * `ohReally_isThatSo.mp3`
  
### Commands

When prompted to type a guess, precede your response with a "." to invoke one of the following available commands:

* `skip`: Skips the audio snippet that was last played, and reveals all acceptable answers for that snippet.
* `repeat`: Repeats the audio snippet that was last played.
* `quit`: Quits the utility.
* `help`: Displays available commands.
  
### Dependencies

* This utility is written in **Python 2.7.**
* Uses the [`playsound`](https://pypi.org/project/playsound/) module.

## Backstory

While studying a foreign language in college, I was searching for an effective and entertaining way to learn new vocabulary. I was tired of flashcards, and I wanted a solution that involved audible comprehension of the language, since I was getting enough reading and writing practice from the assignments for the course. As each new unit arrived, my instructor provided students with recordings of themself saying each new word or phrase in the foreign language, but I wasn't sure how to study with these. Manually playing each recording wasn't helping me learn, because I already knew the translation of the audio file that I was about to play --- it was in the audio file's name. I needed something that would play each audio file in a random order, and not reveal the translation to me until I had made a guess. I also wanted to be able to organize the audio files by which unit they were a part of. This situation of mine led to the creation of this utility.
