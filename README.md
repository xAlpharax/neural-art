# neural-art

Neural Style Transfer done from the CLI using a VGG backbone and presented as an MP4.

Weights can be downloaded from [here](https://m1.afileditch.ch/ajjMsHrRhnikrrCiUXgY.pth). The downloaded file should be placed in `./weights/` and any file will be ignored from there when pushing, as seen in `./.gitignore`. Update: Alternatively, if the `./weights/` directory is empty, `./neuralart.py` will automatically download the aforementioned default weights.

### Why use this in 2023 ?

Because Style Transfer hasn't changed drastically in terms of actual results in the past years. I personally find a certain beauty in inputting a style and content image rather than a well curated prompt with a dozen of switches. Consider this repo as a quick ***just works*** solution that can run on either CPU or GPU effectively.

## Usage

The script sits comfortably in `./stylize.sh` so run it (strictly from the project directory):

```bash
./stylize.sh path/to/style_image path/to/content_image
```

A helper script is also available to run `./stylize.sh` for each distinct pair of images present in the `./Images/` directory:

```bash
./all.sh
```

If, at any point, curious of the individual frames that comprise the generated `./content_in_style.mp4` check `./Output/`
There's also a (redundant) `./images.npy` file that contains raw array data. `./clear_dir.sh` removes redundant files each time they're no longer needed.

### Requirements

All requirements are specified in `./requirements.txt` as per python etiquette:

```bash
pip install -r requirements.txt
```
