# Setup

```bash
sudo apt-get install vlc
conda create --name vlc python=3.11
conda activate vlc
conda install -c conda-forge ffmpeg
conda install -c conda-forge libstdcxx-ng
conda install -c conda-forge libffi
pip install flask requests python-vlc
```

# Client

```bash
python client.py -c <SERVER> -f <FILE>
```
