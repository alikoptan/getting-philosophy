### A Python script to check the [Getting to Philosophy](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy) law.

### Install & Run
1. Run ```pip install requirements.txt```
2. Pass the link(s) as an argument to the python script. e.g.

```python script.py "https://en.wikipedia.org/wiki/Special:Random" "https://en.wikipedia.org/wiki/B_sharp_tree"```

### Scraping
Following the chain consists of:

1. Selecting all ```<p>``` elements, specificly the ones under ```mw-content-text``` id.
2. Removing all content between brackets. 
3. Selecting all links that direct to existing Wiki pages (excluding links to files).
4. Picking the first valid link, repeat.


