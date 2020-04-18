# COVID-19 Tracker

Quick script to compare how fast COVID-19 is spreading in different countries, using the Johns Hopkins CSSE dataset.

## Usage

```
pip install -r requirements.txt
python plot.py Italy US Canada --log
python plot.py --deaths --save deaths.png
python plot.py --daily --per-million Canada US
```

## Data

Johns Hopkins University CSSE, https://github.com/CSSEGISandData/COVID-19
