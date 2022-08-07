# Listen-To-See
Analytics Club Project for the year 2021-22

## Aim of the project:
We aspire to build an audio-video captioning system that will aid the blind in their daily routines - particularly, when a scene is presented, the output will be a spoken description of the objects in the area.

## Work done so far:
- Initially started with basic image captioning models (no attention) <br>
- Focused on encoder + decoder parts separately - paper discussion & implementation - [Adaptive Attention](Image-Captioning/Adaptive%20attention%20for%20image%20captioning), [Meshed Memory Transformer](Image-Captioning/Meshed%20memory%20transformer) <br>
- Made a web application interface for the model - [Web App](Image-Captioning/webapp/notebook.ipynb) <br>

## Ideas being explored:
- [Comparison of different CNNs (ensemble approach)](https://arxiv.org/abs/2102.11506)<br>
- [Video captioning system](https://drive.google.com/file/d/175mFKQHjBBOdjeKNZIZ5ln-r7ehPDguv/view?usp=sharing) <br>
- [Using Multiple Streams of Input](Image-Captioning/Papers/Attention-Based%20Multimodal%20Fusion%20for%20Video%20Description.pdf)

## Work for future plans:
Here is a rough [Timeline of Events](Timeline.md)
- Converting to a text-to-speech system ([Tacotron](https://arxiv.org/abs/1712.05884)) <br>
- Branching to video captioning system <br>
- Updating web app UI to generate real-time video captions <br>
