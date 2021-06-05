# Alamari

### A typical package to get all your utilities

The package was invented out of necessity, out of boredom and above all due to need (I'm serious).

"A collection of utils that you might not require but might need."

> Bored Me, 2021

## FAQs

### Q1. What I'm getting out of this package?

```python
>>> import alamari
```

ANS: Glad you thought. You get this beautifully named package called `alamari`. Isn't this word beautiful? Just think about it, you get to import this beautifully-named-and-thought-out package inside your side projects. Now you maybe wondering, how did this guy knows about my 213th side project? Well, this is due to this package which has `telemetry` installed by default. It tracks user when they install this package. I know I'm getting nowhere here, actually that's how is this package, it lets you nowhere (just kidding). Skip to the next question.

```python

# Convert Section

# convert to integer with a smart AI (lol)
>>> from alamari.convert import *
>>> to_integer('abc123abc456')
>>> 123,456

# convert to roman from devanagiri
>>> to_roman('तनहुँ ब्यास नगरपालिका सागेकी २२ वर्षीया युवतीकी एक जना आमाजु पर्ने थिइन्')
>>> tanahun byaasa nagarapaalikaa saageki 22 warsiyaa yuwatiki eka janaa amaaju parne thiin

# convert to nepali date from english date
>>> to_nepali_miti(2021, 6, 7)
>>> '2078-02-24'

# Utils Section

# checks if url resolves (sorry for bad example but lol)
>>> from alamari.utils import *
>>> url_resolves('https://github.com/sidbelbase/alamari/raw/main/README.md')
>>> False

# replace something from a text if you feel awkward
>>> replace('I love this alamari package', 'alamari', 'daraaazzz')
>>> I love this daraaazzz package

# get datetime object from a string or text
>>> parse_date('In year 2021, a great guy made a package in June fifth at 5:55')
>>> datetime(2021,6,5,5,55,0)

# pluralize the given singular unit
>>> pluralize('knife')
>>> knives

# ordinalize the given number (idk why i added this util)
>>> ordinalize(34)
>>> '34th'

# Humanize Section

# humanize number in nepali form i.e yeti much crore, yeti lakh, yeti hajar YK
>>> from alamari.humanize import *

>>> number(12345675)
>>> '1,23,45,675'

>>> number(9.54)
>>> '09'

# humanize datetime stuffs
>>> date(any_date = '2021-06-07 05:55:55.185035')
>>> 5 hours ago

# humanize nepali datetime
>>> date(local_date = '2021-06-07 05:55:55.185035')
>>> just now
```

## Installation

```shell
$ pip install alamari
```

## Documentation

Sorry, complete documentations cannot be found. You need to go inside the alamari folder and peek inside each files. You have my permission to copy the code and modify like you want. But don't. I made this package for a reason. Remember, every time you copy my code, I'll receive a alert (telemetry magic)

## Contribution

For contributing this blissful package, please add all the utils you would love to see. Also add comments and docstrings to help people navigate through the pain they might hold for several years & I don't want to be remembered that way. Please send all the issues and pull requests.

NOTE: Please don't send your issues and pull-requests during fridays. You may don't want to disturb me during my favorite day. If you do that, I'll press this auto-destroy-button & this package will be just a stardust.

Let's see who wins, people who think this package is a absolute trash press that `star` button & people who think the other way press `fork` button and contribute.

### Made with ❤️ in Nepal.
