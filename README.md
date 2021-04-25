# ez-Write

![Alt Text](https://github.com/Pravallika-Myneni/speech-to-handwritten-notes/blob/main/ez-write%20Pitch.gif)

## Inspiration
As Grammarly says, “writing’s not that easy.” We were inspired for 4 main reasons:
1) Everyone hates writing pages and pages of words for classes, and we wanted to automate the process so it’s less tiring and menial.

2) Dysgraphia is a learning disability which interferes with an individual’s ability to write legibly. It begins at a young age in some children, and there is typically no cure. This may affect self-esteem, and we wanted to create a tool which could help those affected.

3) Doctor’s messy handwriting on prescriptions allegedly causes thousands of deaths worldwide every year. We wanted to make it easier so they can simply record what they want to say, for a legible output.

4) Learning to write new languages can be difficult, so with this tool, users can speak and upload audio files, and see what it looks like written out.

## What it does
ez-write aims to make writing easier and more automated, by converting your audio files into handwritten text. The steps are as follows:

1) User opens the web-page and uploads an audio recording of them speaking

2) The program produces a transcript in plain text

3) The text is then analyzed and converted into handwritten text (see “what’s next” section), and the user can save it as a PDF file.


## How we built it
We used Python libraries and Flask for the back end, along with Tensorflow and some Machine Learning to analyze the text from audio. We used HTML and CSS styling for the front end.

## Challenges we ran into
It was difficult to convert text into handwriting, we ran into several bugs along the way, and had to do a ton of Googling and asking the mentors for assistance to solve any problems. Additionally, we had to learn how to use libraries (Flask and Tensorflow), and it was difficult to integrate the backend to frontend.

## Accomplishments that we're proud of
Having a working product within 24 hours! Additionally, working together to try and figure out how to implement our idea. 3/4 of us were total beginners, so we're proud that we were able to successfully create a functioning web app.

## What we learned
How to use programming libraries, how to build a web app, and how to do front end styling with HTML, CSS, React, and Bootstrap

## What's next for ez-write
A few key features we’d like to add are:
1) Microphone feature so user can speak audio directly

2) User can upload their own handwriting sample to create a personalized font

3) Support for several types of audio files

4) More styling features, including bold, underline, font size, diagrams, plus different colours to choose from

5) Support for languages and alphabets other than English

6) More than one page of text output at once, so users won’t have to run the program separately for each page
