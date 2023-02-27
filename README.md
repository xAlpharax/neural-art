# neural-art
Neural Style Transfer done from the CLI using a VGG backbone and presented as an MP4.

Weights can be downloaded from [here](https://m1.afileditch.ch/ajjMsHrRhnikrrCiUXgY.pth). The downloaded file should be placed in `./weights/` and will be ignored when pushing as seen in `./.gitignore`

### Why use this in 2023 ?
Because style transfer hasn't changed drastically in terms of actual results in the past years. I personally find a certain beauty in inputing a style and content image rather than a well curated prompt with a dozen of switches. Consider this repo as a quick *just works* solution that can run on both CPU and GPU effectively.

## Usage

The script sits comfortably in `./stylize.sh` so just run it in the project directory:

```bash
./stylize.sh path/to/style_image path/to/content_image
```

### Requirements

All requirements are specified in `./requirements.txt` as per python etiquette:

```bash
pip install -r requirements.txt
```
