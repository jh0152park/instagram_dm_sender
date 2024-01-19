### Installation

```
pip install instagrapi
```

If occurred `No module named 'PIL'` then try to install `npm install pollow`

### Check it out!! [Doc](https://github.com/subzeroid/instagrapi?tab=readme-ov-file)

# When occurred `Input should be a valid datetime, dates after 9999 are not supported as unix timestamps [type=datetime_parsing, input_value='1702926042126901', input_type=str]` error

When try send direct message to someone with `user_id` by `direct_send`function above error might be occurred.

Its due to `instragram` returning data as a big numbers like above error, and `extract_direct_message` function inside of `extractors.py` dose not accept that type of date input.

So, have to fixed the `extract_direct_message` code.

## How to find the path of `instagrapi` installed.

1. open terminal
2. enter `pip show instagrapi`
3. find `Location` category and copy the path (inaddition the actual path gonna be `<virtualenv_name>/lib/<python_ver>/site-packages`)
4. move to the copied path
5. find out `instagrapi` folder or path
6. open `extractors.py`
7. import `from datetime import datetime` at the top of the file
8. find `extract_direct_message` function and then replace as below
9. run python script again
10. being happy🤩

```python
def extract_direct_message(data):
    data["id"] = data.get("item_id")
    # Handle replied messages, media shares, and other relevant data
    if "replied_to_message" in data:
        data["reply"] = extract_reply_message(data["replied_to_message"])
    if "media_share" in data:
        ms = data["media_share"]
        if not ms.get("code"):
            ms["code"] = InstagramIdCodec.encode(ms["id"])
        data["media_share"] = extract_media_v1(ms)
    if "media" in data:
        data["media"] = extract_direct_media(data["media"])
    if "voice_media" in data:
        if "media" in data["voice_media"]:
            data["media"] = extract_direct_media(data["voice_media"]["media"])
    clip = data.get("clip", {})
    if clip:
        if "clip" in clip:
            clip = clip.get("clip")
        data["clip"] = extract_media_v1(clip)
    xma_media_share = data.get("xma_media_share", {})
    if xma_media_share:
        data["xma_share"] = extract_media_v1_xma(xma_media_share[0])

    # Handle timestamp conversion
    timestamp = data.get("timestamp")
    if timestamp:
        try:
            # Convert the timestamp to seconds from microseconds
            timestamp_seconds = int(timestamp) / 1_000_000

            # Convert the timestamp to a datetime object
            dt = datetime.fromtimestamp(timestamp_seconds)

            # Format the datetime object as a string
            data["timestamp"] = dt.strftime("%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            # If parsing fails, set the timestamp to None
            data["timestamp"] = None

    return DirectMessage(**data)
```
