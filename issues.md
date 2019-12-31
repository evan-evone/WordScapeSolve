Installing on iOS (for Pythonista) will have a `No module named: 'ctypes.macholib'` error;
this is due to a strange `ctypes` installation for Pythonista. The simplest solution is to
simply put a desktop copy of `ctypes` into `site-packages` in Pythonista.

---

Installing on iOS will also have a weird error in `enchant/_enchant.py`, in that it will be
unable to find the `'enchant' C library`. The issue appears to be that changing platforms
messes with the `enchant/lib` library, which is built for MacOS, or the `darwin` platform.

I've messed around somewhat, and here's what I came up with so far: the program works on
MacOS because it is built for the `darwin` system and `enchant/_enchant.py` knows how to
handle `darwin`---and also, from what I can tell, the file extensions appear to be
`darwin`- specific (though this is just a hypothesis). On iOS, the platform is called `ios`.
Likely, this will require a special setup within the `enchant/_enchant.py` file and possibly
special---or at least different---files in `enchant/lib`.
