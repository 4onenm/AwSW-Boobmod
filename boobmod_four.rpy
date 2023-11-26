init 1000 python in boobmod_four:
    boobify = {
        # Adine
        "cr/adine_normal.png": ((0,0), "cr/boobmod/adineboobs.png"),
        "cr/adine_normal_b.png": ((0,0), "cr/boobmod/adineboobs.png"),
        "cr/adine_normal_c.png": ((0,0), "cr/boobmod/adineboobs.png"),
        "cr/adine_frustrated.png": ((0,0), "cr/boobmod/adineboobs.png"),
        "cr/adine_frustrated_b.png": ((0,0), "cr/boobmod/adineboobs.png"),
        "cr/adine_frustrated_c.png": ((0,0), "cr/boobmod/adineboobs.png"),
        "cr/adine_disappoint.png": ((0,0), "cr/boobmod/adineboobs.png"),
        "cr/adine_disappoint_b.png": ((0,0), "cr/boobmod/adineboobs.png"),
        "cr/adine_disappoint_c.png": ((0,0), "cr/boobmod/adineboobs.png"),
        "cr/adine_annoyed.png": ((0,0), "cr/boobmod/adineboobs.png"),
        "cr/adine_annoyed_b.png": ((0,0), "cr/boobmod/adineboobs.png"),
        "cr/adine_annoyed_c.png": ((0,0), "cr/boobmod/adineboobs.png"),
        # Anna
        "cr/anna_cry.png": ((0,0), "cr/boobmod/annaboobs.png"),
        "cr/anna_despair.png": ((0,0), "cr/boobmod/annaboobs.png"),
        "cr/anna_disgust.png": ((0,0), "cr/boobmod/annaboobs.png"),
        "cr/anna_normal.png": ((0,0), "cr/boobmod/annaboobs.png"),
        "cr/anna_rage.png": ((0,0), "cr/boobmod/annaboobs.png"),
        "cr/anna_sad.png": ((0,0), "cr/boobmod/annaboobs.png"),
        "cr/anna_smirk.png": ((0,0), "cr/boobmod/annaboobs.png"),
        # Emera
        "cr/emera_frown.png": ((0,0), "cr/boobmod/emeraboobs.png"),
        "cr/emera_frown_b.png": ((0,0), "cr/boobmod/emeraboobs.png"),
        "cr/emera_laugh.png": ((0,0), "cr/boobmod/emeraboobs.png"),
        "cr/emera_laugh_b.png": ((0,0), "cr/boobmod/emeraboobs.png"),
        "cr/emera_mean.png": ((0,0), "cr/boobmod/emeraboobs.png"),
        "cr/emera_mean_b.png": ((0,0), "cr/boobmod/emeraboobs.png"),
        "cr/emera_normal.png": ((0,0), "cr/boobmod/emeraboobs.png"),
        "cr/emera_normal_b.png": ((0,0), "cr/boobmod/emeraboobs.png"),
        "cr/emera_ques.png": ((0,0), "cr/boobmod/emeraboobs.png"),
        "cr/emera_ques_b.png": ((0,0), "cr/boobmod/emeraboobs.png"),
        # Kalinth
        "cr/kalinth_normal.png": ((0,0), "cr/boobmod/kalinthboobs.png"),
    }

    # The below code should never be written.
    # But now that we've begun, how does it work?

    import renpy.display.im as im

    # First, we import Ren'Py's image base classes, so we can abuse them.
    # The key idea is to find all the images we're targeting and to replace
    # them with Composite objects that will allow us to slap a boob on top.

    # Step one: find the Image manipulator that loads from files for each
    # image. This is the class that loads the image from disk, so replacing
    # it with our own behavior will allow us to swap it for the composite.

    # Because Ren'Py keeps no references to random Image manipulators that
    # may never be loaded, we have to sift through the Python garbage
    # collector's list of all objects to find the ones we want.
    import gc
    images = [img for img in gc.get_objects() if isinstance(img, im.Image) and img.filename in boobify]

    # Step two: transmute each of the Image manipulators into Composite
    # manipulators by replacing their class with the Composite class
    # and their __dict__ with an equivalent behaviour Composite instance's
    # __dict__, but with the boob layer added.
    for img in images:
        filename = img.filename

        print("Boobmod: boobifying", filename)

        img.__class__ = im.Composite
        # Pro tip! If an im.Composite does not know its size, it will
        # default to the size of the first layer. This is why we can
        # just add the boob layer to the end and have it work.
        img.__dict__ = im.Composite(None, (0,0), filename, *boobify[img.filename]).__dict__

    # Step three: ???
    # Jk, we're done. The images will now be loaded as Composites, which
    # will draw the boob layer on top of the original image, but before
    # any other manipulations are applied.
    # This absolutely will not work for any other mod, but for this kind
    # of nonsense that's not supposed to be consistent, it's fine.

    # Note that if the base filename isn't in the boobify dict, it will
    # just load as a normal image. This means any mod-added expressions
    # for characters that provide entirely new images will not be affected.
    # This is a good thing, because it means we don't have to worry about
    # breaking other mods with weird clipping for alternative character
    # arm positions or whatever.

    # Boobify dict also doesn't draw the boobs for characters with neck
    # items (Anna's goggles) or wounds (Adine's blood, Anna's bullet wounds.)

    # Step four: profit.
    # Or, in this case, enjoy the boobs.