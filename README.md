# Rss to txt file

This code is useful to get info from a rss feed and store on a text file.

It is used as a cron job that gathers info from specific sources and saves them on a text file. 

## Instalation

```
git clone https://github.com/GabrielRF/RssToFile
cd RssToFile
pip3 install -r requirements.txt
```

Then set the configuration file

```
cp bot.conf_sample bot.conf
vi bot.conf
```

## Usage

```
python3 rsstofile.py RSS1
```
