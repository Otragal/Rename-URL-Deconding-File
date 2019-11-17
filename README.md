# Rename-URL-Deconding-File
If you downoad  videos from Youtube, all file names will have URL code.. So I created python3 program to raname all these files in directory to make easy in my life.

## Variables

There is an important variable to start the program:

***path***: variable where you set you directory where you download from Youtube. Just copy the directory and set it.

### Notes

To use Rename URL decode, I imported **os** and **urllib.parse**. I found some decode problens in **urlib.parse.unquote** that can't convert some code and will show *errors* during running. To resolve, you need edit yourself

**ASCII Encoding Reference not possible convert**

| Character | From UTF-8 |
| --- | --- |
| * | %2A |
| / | %2F |
| " | %22 |
| ? | %3F |

