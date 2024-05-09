# Alamari

### A typical package to get all your utilities (with AI capabilities)

This package was invented out of necessity, out of boredom & above all due to need (I'm serious).

##### "A collection of utils that you might not require but might need."

> Bored Me, 2021

## FAQs

### Q1. What I'm getting out of this package?

```python
>>> import alamari
```

ANS: Glad you thought. First of all, you get this beautifully named package called `alamari`. Isn't this word beautiful? Just think about it; you can import this package into your side projects. Now you may be wondering, how this guy knew about my 213th side project because this package has `telemetry` installed by default. It tracks any developer when they install this beautifully-named-and-thought-out package. I know I'm getting nowhere here, it's how it has been made, to let you nowhere (just kidding). Please, skip to the next line.

```python

# Convert Section

# convert to integer with a smart AI (lol)
>>> from alamari.convert import *
>>> to_integer('abc123abc456')
>>> '123,456'

# convert to roman from devanagari
>>> to_roman('तनहुँ ब्यास नगरपालिका सागेकी २२ वर्षीया युवतीकी एक जना आमाजु पर्ने थिइन्')
>>> 'tanahun byaasa nagarapaalikaa saageki 22 warsiyaa yuwatiki eka janaa amaaju parne thiin'

# convert to nepali date from english date
>>> to_nepali_miti(2021, 6, 7)
>>> '2078-02-24'

# Utils Section

# checks if url resolves (sorry for the bad example but lol)
>>> from alamari.utils import *
>>> url_resolves('https://raw.githubusercontent.com/sidbelbase/alamari/master/README.md')
>>> False

# replace something from a text if you feel awkward
>>> replace('I love this alamari package', 'alamari', 'daraaazzz')
>>> 'I love this daraaazzz package'

# get a datetime object from a string or text
>>> parse_date('2021, June 5th 5:55')
>>> datetime(2021, 6, 5, 5, 55)

# pluralize the given singular unit
>>> pluralize('knife')
>>> 'knifes'

# ordinalize the given number (I don't know why I added this util)
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
>>> '5 hours ago'

# humanize nepali datetime
>>> nepal_date(local_date = '2021-06-07 05:55:55.185035')
>>> 'just now'
```

## Installation

```shell
$ pip install alamari
```

## Documentation

Here's a thing mate. I want to be open about i.e. I didn't prepare any documents for it. You'll need to go inside the alamari folder and take a look inside each file. You have my permission to copy the code and modify it the way you want. But don't. I made this package for a reason & this exists for a reason. Why would you not respect my reason? Remember, every time you copy my code, I get a notification about your endeavor (telemetry magic)

## Contribution

To be part of this blissful package, please add all the utils you want if you're tired of typing and copying again and again. While adding your utils please also add comments & docstrings to help people navigate through the pain they might hold for several years & I don't want to be remembered that way. Send all your issues and pull requests my way. Peace.

NOTE: Please don't send your issues and pull requests on Fridays. You may not want to disturb me during my favorite day. If you do that, I'll press this auto-destroy button that I had built the other day & this package will be just a stardust.

Let's see who wins, people who think this package is an absolute trash press that `star` button & people who think the other way press `fork` button and contribute.

## Gratitude

Developers who came here seeing their package being used by a guy with a terrible coding pattern, I want to say that I'm forever grateful for you and your existence. Long live OSS.

### Made with ❤️ in Nepal.
