# neural-art

Neural Style Transfer done from the CLI using a VGG backbone and presented as an MP4.

Weights can be downloaded from [here](https://files.catbox.moe/wcao20.pth). The downloaded file (renamed to `vgg_conv_weights.pth`) should be placed in `./weights/` and it will be ignored when pushing, as seen in `./.gitignore`. **Update:** Alternatively, if the `./weights/` directory is empty, `./neuralart.py` will automatically download publicly available VGG19 weights for the user.

More in depth information about Neural Style Transfer ( NST ) can be found in this great [paper](https://arxiv.org/abs/1705.04058). Make sure to check [Requirements](#requirements) and [Usage](#usage) as well as the [Video Gallery](#results-after-running-neural-art-click-on-dropdown-for-video-gallery).

### Why use this in 2024 ?

Because Style Transfer hasn't changed drastically in terms of actual results in the past years. I personally find a certain beauty in inputting a style and content image rather than a well curated prompt with a dozen of switches. Consider this repo as a quick and simple ***just works*** solution that can run on both CPU and GPU effectively.

I developed this tool as a means to obtain fancy images and visuals for me and my friends. It somehow grew into something bigger that is actually usable, so much so that I got to integrate it in a workflow in conjunction with [Stable Diffusion](https://github.com/CompVis/stable-diffusion) ( see also [here](https://github.com/AUTOMATIC1111/stable-diffusion-webui) ) which I want to develop a plugin for.

## Requirements

Clone the repository:

```bash
git clone https://github.com/xAlpharax/neural-art

# or via ssh
git clone git@github.com:xAlpharax/neural-art.git
```

Create a virtual environment to separate the required packages from system-wide packages:

```bash
virtualenv path/to/neural-art

source path/to/neural-art/bin/activate
```

( ! ) When you're finished with the environment:

```bash
# deactivate
```

All the required packages are listed in `./requirements.txt` as per python etiquette:

```bash
pip install -r requirements.txt
```

## Usage

The main script sits comfortably in `./stylize.sh`, run it from the project's root directory:

```bash
./stylize.sh path/to/style_image path/to/content_image
```

A helper script is also available to run `./stylize.sh` for each distinct pair of images present in the `./Images/` directory:

```bash
./all.sh
```

Moreover, `./all.sh` is aware of the already rendered mp4 files and will skip stylizing the combinations that are already present. In contrast, `./stylize.sh` overwrites images and videos.

### Output videos / images and temporary files

The stylization process outputs a video in the format `./content_in_style.mp4` with `content` and `style` being the 2nd and 1st command line arguments of the `./stylize.sh` script.

If, at any point, you need the individual frames that comprise the generated `./content_in_style.mp4`, check the `./Output/` directory for `.png` images with frames at each iteration.
The `./neuralart.py` code that sits at the heart of this project generates raw numpy array data to `./images.npy` which in turn is manipulated by `./renderer.py` to output frames as `.png` images.

These intermediary outputs are temporarily stored and get removed each time the `./stylize.sh` script is run.

All the stylize combinations from the `./Images/` directory have been saved to [this archive](https://drive.google.com/file/d/1k_ECmiHe3l0uS0ps2faWk8PHAOaNYZPp). Check the video gallery below to go through some of them that look the best:


<details>


<summary><h3>Results - Click on dropdown menu for video gallery</h3></summary>


Starry Night in various other styles 8

https://github.com/xAlpharax/neural-art/assets/42233094/6d60fa23-45eb-4af6-a41d-e97df4cc2fb7

https://github.com/xAlpharax/neural-art/assets/42233094/83160305-e397-40f8-94f6-db61fc25b4a4

https://github.com/xAlpharax/neural-art/assets/42233094/4ff8fa14-50c0-4d5f-b744-098555681cde

https://github.com/xAlpharax/neural-art/assets/42233094/fe75e32d-d0f1-43eb-a5dc-8a74c1eeceec

https://github.com/xAlpharax/neural-art/assets/42233094/131cfbae-ca6c-4b06-aa01-05e1f2557021

https://github.com/xAlpharax/neural-art/assets/42233094/4e108c08-c365-49e1-ad14-0d993621d6d2

https://github.com/xAlpharax/neural-art/assets/42233094/bdfd99d0-06de-4753-899c-6c0e22b05b83

https://github.com/xAlpharax/neural-art/assets/42233094/e50cf174-20c9-4dc1-9cc9-960122147bae


Monet in various other styles 7

https://github.com/xAlpharax/neural-art/assets/42233094/49b04fe6-494f-47d5-9827-eb6dfbf850dd

https://github.com/xAlpharax/neural-art/assets/42233094/71419dbf-ab55-4011-9ce3-b4c1b9fbd5d6

https://github.com/xAlpharax/neural-art/assets/42233094/11081f9d-a629-4693-9894-fb5d9eb55ad1

https://github.com/xAlpharax/neural-art/assets/42233094/b282f2b9-bf52-4653-9b01-37fe90e99a47

https://github.com/xAlpharax/neural-art/assets/42233094/c8f54e6c-0067-4240-af20-85a9427b53b8

https://github.com/xAlpharax/neural-art/assets/42233094/1d632241-3e6c-4f46-9186-e92421d2b29c

https://github.com/xAlpharax/neural-art/assets/42233094/0be8f741-c424-4f47-956d-4308c1f5ec14


Colorful in various other styles 6

https://github.com/xAlpharax/neural-art/assets/42233094/510b5591-a3a1-4205-9533-b40046164852

https://github.com/xAlpharax/neural-art/assets/42233094/73788e8b-c6cc-4436-9286-c8a3ac183095

https://github.com/xAlpharax/neural-art/assets/42233094/60130d15-6cdd-4c9e-96f5-66d6f47959de

https://github.com/xAlpharax/neural-art/assets/42233094/b0d62d42-9c57-4426-ba3a-ac852f4872b2

https://github.com/xAlpharax/neural-art/assets/42233094/953660a6-070e-4f62-81dd-4b97a25dfb8f

https://github.com/xAlpharax/neural-art/assets/42233094/d7f6cd57-7524-42de-a098-c491324c50a3


Azzalee in various other styles 5

https://github.com/xAlpharax/neural-art/assets/42233094/ec8595af-7b96-4810-b888-c6ef80a1d6da

https://github.com/xAlpharax/neural-art/assets/42233094/91a49410-a9d5-46ae-8fa6-57715d18b485

https://github.com/xAlpharax/neural-art/assets/42233094/1c16a765-4321-45db-a119-c5b44edf9b4a

https://github.com/xAlpharax/neural-art/assets/42233094/b2375f7c-46cf-45a3-89cb-4dbf54e68ca4

https://github.com/xAlpharax/neural-art/assets/42233094/927f429d-e8a5-4165-b2b5-79a1338651e0


Jitter Doll in various other styles 5

https://github.com/xAlpharax/neural-art/assets/42233094/9d988d8e-b6c0-4dfd-9f3d-5cb006901aaa

https://github.com/xAlpharax/neural-art/assets/42233094/40e05578-881e-4be8-a8e2-75ed388f1ace

https://github.com/xAlpharax/neural-art/assets/42233094/5a98489c-8ad9-4708-8b47-35af1e216c1b

https://github.com/xAlpharax/neural-art/assets/42233094/bbca966d-bba1-4f3c-927f-3ca7836fe150

https://github.com/xAlpharax/neural-art/assets/42233094/2347bfa3-f4c4-402b-b9c9-bef48f2c147b


Shade in various other styles 7

https://github.com/xAlpharax/neural-art/assets/42233094/da894522-1cfc-492d-b2ec-7f0a6a23fb4d

https://github.com/xAlpharax/neural-art/assets/42233094/682427bb-f5c1-439d-b535-9cb056a9a022

https://github.com/xAlpharax/neural-art/assets/42233094/4f9a1e7a-1930-4503-8288-0353b63a213b

https://github.com/xAlpharax/neural-art/assets/42233094/082be485-ff88-48d0-960e-0883e903dfc2

https://github.com/xAlpharax/neural-art/assets/42233094/80015d89-5a75-4487-b4c7-a7b04341585b

https://github.com/xAlpharax/neural-art/assets/42233094/d277e8df-eef7-4f99-9a52-0bd908a30f2e

https://github.com/xAlpharax/neural-art/assets/42233094/fb5a8ffe-5aca-42bb-941f-bbd37eef9fe3


Abstract in various other styles 6

https://github.com/xAlpharax/neural-art/assets/42233094/50bb24f6-f869-4508-8598-9d0795adcc2e

https://github.com/xAlpharax/neural-art/assets/42233094/f38d2c3e-54f2-442a-a583-a1327cd763d4

https://github.com/xAlpharax/neural-art/assets/42233094/1fd17d45-51ae-4d1f-9b43-776beb0a802b

https://github.com/xAlpharax/neural-art/assets/42233094/f282cc37-17bb-451a-b213-0bb6ad3de5a7

https://github.com/xAlpharax/neural-art/assets/42233094/b2ec336a-ed80-4750-b620-d600987dd3cc

https://github.com/xAlpharax/neural-art/assets/42233094/89bc91fd-c311-4d8c-a1fc-b2a747432fc0


Gift in various other styles 5

https://github.com/xAlpharax/neural-art/assets/42233094/0423c75c-3db5-45f6-b579-ef1c0fe95475

https://github.com/xAlpharax/neural-art/assets/42233094/18182505-e66d-4d2e-86e1-b0094ee11cfc

https://github.com/xAlpharax/neural-art/assets/42233094/5ae434ae-936f-4ca0-bfc6-29775355505f

https://github.com/xAlpharax/neural-art/assets/42233094/1713e3bb-c34b-4790-8c30-3447aedfbcd3

https://github.com/xAlpharax/neural-art/assets/42233094/9a87adc8-d00d-4303-bd2f-3677d6a68ce7


kanade in various other styles 8

https://github.com/xAlpharax/neural-art/assets/42233094/695b3a78-0cb2-4a10-97f2-8d3a875ff265

https://github.com/xAlpharax/neural-art/assets/42233094/1d991b79-dca1-4fe6-bda6-9a8d38f134e7

https://github.com/xAlpharax/neural-art/assets/42233094/bd2b83b1-823b-4734-88d6-622858e18b74

https://github.com/xAlpharax/neural-art/assets/42233094/411ada80-b4db-4721-b0d7-7be059e96970

https://github.com/xAlpharax/neural-art/assets/42233094/4a6cf35b-087b-4b9a-b617-f9f22ca48047

https://github.com/xAlpharax/neural-art/assets/42233094/6bea757f-1918-4674-9324-c57b4cd3401a

https://github.com/xAlpharax/neural-art/assets/42233094/10c7c5fb-1a9b-4e19-82e7-e2d27cb2b079

https://github.com/xAlpharax/neural-art/assets/42233094/89ad03b0-8213-4b70-9b6a-b1ac55e8f2d0


bunnies in various other styles 5

https://github.com/xAlpharax/neural-art/assets/42233094/29bbcfa0-fd2e-484c-abf4-5bbcfe7aee44

https://github.com/xAlpharax/neural-art/assets/42233094/286f23cb-90ed-4ba1-b79c-06450d15e7bb

https://github.com/xAlpharax/neural-art/assets/42233094/a9ab3606-921e-4add-adf0-2b927a5dc62b

https://github.com/xAlpharax/neural-art/assets/42233094/ac94a895-5e7f-4c77-8e24-9c297a970f6a

https://github.com/xAlpharax/neural-art/assets/42233094/86113129-c4be-445d-a017-6fa394d83fda


cute in various other styles 5

https://github.com/xAlpharax/neural-art/assets/42233094/6b7fc161-ff87-4b68-8035-7bb3c3e5a417

https://github.com/xAlpharax/neural-art/assets/42233094/4dceae73-1ad4-4ed2-b8bf-6f7e909a1440

https://github.com/xAlpharax/neural-art/assets/42233094/667a66c1-f4f9-408e-aa9c-06c7e4af21e0

https://github.com/xAlpharax/neural-art/assets/42233094/f4334996-f1a5-4c57-add1-8781dfc6a8e0

https://github.com/xAlpharax/neural-art/assets/42233094/92c5f9bb-4224-4d0f-af2f-f7113904ed0f


kek in various other styles 2

https://github.com/xAlpharax/neural-art/assets/42233094/36dd6f3f-aca6-4e0f-8be8-3fd3ec4ab772

https://github.com/xAlpharax/neural-art/assets/42233094/3bd2433a-54d1-40e2-9d00-cb165f6a2985


Tarantula reference:)

https://github.com/xAlpharax/neural-art/assets/42233094/555a4675-da19-4fa6-9104-1ee2c63a7f8b


</details>


## Contributing

Any sort of help, especially regarding the QoS ( Quality of Service ) of the project, is appreciated. Feel free to open an issue in the **Issues** tab and discuss the possible changes there. As of now, **neural-art** would be in great need of a clean and friendly arguments handler ( i.e. the one the `argparse` python package provides ) in order to accommodate to a cleaner interface for `./neuralart.py` and / or `./stylize.sh`.

Thank you. Happy neural-art-ing !
